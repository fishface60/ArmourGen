DEBUG = False

import math
import os.path
from uuid import uuid4
import xml.etree.ElementTree as ET
from xml.dom import minidom

from ConstructionLibrary import *
from BaseMaterialLibrary import *
from HitLocationLibrary import *

# Some master lists to have all valid objects of a type in one place, for easy reference and checking.
MasterConstructionList = [Fabric, LayeredFabric, Scale, Mail, SegmentedPlate, Plate, Solid, ImpactAbsorbing, OptimisedFabric]
MasterMaterialList = [Bone, Cloth, Horn, Leather, Silk, Wood, CheapBronze, GoodBronze, Copper, Jade, GemJade, Stone, CheapIron, GoodIron, Lead,StrongSteel, HardSteel, Aluminium, HardSteel, HighStrengthSteel, Rubber, BallisticResin, BasicCeramic, ElasticPolymer, Fibreglass, HighStrengthAluminium, Nomex, Nylon, Plastic, Polycarbonate, Titanium, TitaniumAlloy, VeryHardSteel, Aramid, BallisticPolymer, ImpBallisticPolymer, ImpCeramic, ImpKevlar, ImpNomex, Kevlar, LaminatedPolycarbonate, PolymerComposite, TitaniumComposite, UltraStrengthSteel, Arachnoweave, CeramicNanocomposite, EarlyNanoweave, LaserAblativePolymer, MagneticLiquidArmour, PolymerNanocomposite, Reflec, ShearThickeningFluidArmour, TitaniumNanocomposite, AdvancedNanoLaminate, AdvancedPolymerNanocomposite, AdvancedNanoweave, Bioplas, ElectromagneticArmour, NanoAblativePolymer, Diamondoid, DiamondoidLaminate, Monocrys, RetroReflective, EnergyCloth, Hyperdense, HyperdenseLaminate, Adamant, Orichalcum]
MasterQualityList = ["QualityCheap", "QualityFine", "QualityVeryFine", "PropertyBandedMail", "PropertyElvenMail", "PropertyFluted", "PropertyHighlyArticulated", "PropertyMountainScale", "PropertyThieves"]


def _round2sf(n):
	return round(n, -int(math.floor(math.log10(abs(n))) - 1))


### ARMOUR CLASS ###
  # Defines the main armour class, along with its internal functions.

class Armour:
	def __init__(self, name = "BLANK NAME", TL = 0, DR = 0, locations = All, material = ArmourMaterial(), construction = ArmourConstruction()):
		self.name = name
		self.TL = TL
		self.DR = DR
		self.locations = locations
		self.material = material
		self.construction = construction

		self.keywords = []
		self.keywords.extend(self.construction.keywords)
		self.keywords.extend(self.material.keywords)

		self.CF = 1.0
		self.WF = 1.0
		self.notes = ""
		self.specDR = 0
		self.asterisk = ""
		self.flex = False
		self.errorCount = 0
	def execute(self):
		self.consistencyCheck()
		if self.errorCount < 1:
			self.donCalc()
			self.weightCalc()
			self.costCalc()
			self.keywordsCheck()
			self.qualityAdjust()
			self.LCCalc()
			self.output()
			if DEBUG == True: self.debugOutput()
		else:
			print("There were {} errors found with the input armour. Please look at the error message(s) above.".format(str(self.errorCount)))
	def appendNotes(self,AddedNotes):
		self.notes += AddedNotes + " "
	def consistencyCheck(self):
		if self.TL < self.construction.TL:
			self.errorCount += 1
			print("\nError: The given construction type was a higher TL than the armour.")
		if self.TL < self.material.TL:
			self.errorCount += 1
			print("\nError: The given material was a higher TL than the armour.")
		if self.construction not in self.material.constructions:
			self.errorCount += 1
			print("\nError: The given material and construction type are incompatible.")
		if self.DR == 0:
			self.errorCount += 1
			print("\nError: DR was set to zero.")
		else:
			if self.DR < self.construction.minDR:
				self.DR = self.construction.minDR
				print("\nWarning: The input DR was lower than the construction type's minimum DR of {}. The DR has been set to that value.".format(self.construction.minDR))
			if self.DR < self.material.minDR:
				self.DR = self.material.minDR
				print("\nWarning: The input DR was lower than the material's minimum DR of {}. The DR has been set to that value.".format(self.material.minDR))
			if self.DR > self.material.maxDR:
				self.DR = self.material.maxDR
				print("\nWarning: The input DR was higher than the material's maximum DR of {}. The DR has been set to that value.".format(self.material.maxDR))
		if self.material == Leather and self.construction == LayeredFabric and TL == 0:
			self.errorCount += 1
			print("\nError: The layered fabric construction is TL1 for leather.")
		if self.material in [CheapIron,GoodIron,StrongSteel,HardSteel] and self.construction in [Plate,Solid] and self.TL < 4:		#This needs to account for helmets.
			self.errorCount += 1
			print("\nError: Plate or solid constructions are TL4 for iron and steel armour, apart from helmets. If you were making a helmet, this is a known bug; please set the armour to TL4.")

	def keywordsCheck(self):

		# Property keywords
		if "PropertyBandedMail" in self.keywords and self.construction == Mail:
			self.appendNotes("Banded mail; no DR reduction vs. crushing.")
			self.keywords.remove("WeakToCrushing")
			self.WF += 0.5
			self.CF += 0.5
		if "PropertyElvenMail" in self.keywords:
			self.appendNotes("Elven mail; no DR reduction vs. crushing.")
			self.keywords.remove("WeakToCrushing")
			self.CF += 3.0
		if "PropertyFluted" in self.keywords:
			self.appendNotes("Fluted.")
			if self.construction in [Plate, Scale, SegmentedPlate]:
				self.appendNotes("Fluted.")
				self.WF += -0.1
				self.CF += 4.0
		if "PropertyHighlyArticulated" in self.keywords and self.construction in [Plate, Scale, SegmentedPlate]:
			self.appendNotes("Targeting chinks in armour only reduces DR to 2/3, not 1/2.")
			self.CF += 19.0
		if "PropertyMountainScale" in self.keywords:
			self.appendNotes("Mountain scale; no DR reduction vs. crushing.")
			self.keywords.remove("WeakToCrushing")
			self.CF += 1.0
		if "PropertyThieves" in self.keywords and self.construction == Mail:
			self.appendNotes("Weight does not count towards encumbrance for Climbing and Stealth.")
			self.CF += 3.0

		# Quality keywords
		if "QualityCheap" in self.keywords:
			self.appendNotes("Cheap.")
			if self.DR > 10:
				self.DR *= 0.9
			else:
				self.DR += -1
			self.CF += -0.6
		if "QualityFine" in self.keywords:
			self.appendNotes("-1 to target chinks.")
			self.WF += -0.15
			self.CF += 5.0
		if "QualityVeryFine" in self.keywords:
			self.appendNotes("-1 to target chinks.")
			self.WF += -0.35
			self.CF += 29

		# Behaviour keywords
		if "Ballistic" in self.keywords:
			self.appendNotes("Split DR: provides full protection against piercing and cutting attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR*self.material.specDRMult
		if "Bio" in self.keywords:
			self.appendNotes("Split DR: provides full protection against burning and piercing attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR*self.material.specDRMult
		if "Combustible" in self.keywords:
			self.appendNotes("Combustible: if the armour is penetrated by burning damage, it may catch fire (see B433).")
		if "EnergyAblative" in self.keywords:
			self.appendNotes("Split DR: provides full protection against laser attacks and uses its reduced DR against all other types of damage.")
			self.appendNotes("The higher DR is semi-ablative, the lower DR is not.")
			self.specDR = self.DR*self.material.specDRMult
		if "FireResistant" in self.keywords:
			self.appendNotes("Split DR: provides full protection against burning attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR*self.material.specDRMult
		if "Flexible" in self.keywords and self.DR <= self.material.DRperInch*0.25:
			self.appendNotes("Flexible: subject to blunt trauma.")
			self.flex = True
			self.asterisk = "*"
		if "LaserOnly" in self.keywords:
			self.appendNotes("Split DR: provides full protection against laser attacks and none against any other types of damage.")
		if "Laminate" in self.keywords:
			self.appendNotes("Laminate armour: double DR vs. shaped-charge warheads or plasma bolts.")
		if "ReactionsP2" in self.keywords:
			self.appendNotes("+2 to reactions.")
		if "ReactionsP3" in self.keywords:
			self.appendNotes("+3 to reactions.")
		if "SemiAblative" in self.keywords:
			self.appendNotes("DR is semi-ablative.")
		if "SilkBenefits" in self.keywords:
			self.specDR = self.DR+1
			self.appendNotes("Split DR: provides full protection against cutting and impaling attacks and uses its reduced DR against all other types of damage.")
			self.appendNotes("Negates the effect of barbed weapons and attacks that penetrate the armour do not count for blood agent or contact poisons.")
			self.appendNotes("+1 to First Aid to treat wounds inflicted through the armour. Negates -2 in HT penalties from wound infection due to dirt in the wound.")
		if "Transparent" in self.keywords:
			if str.casefold(input("This material can be transparent (double cost, no DR vs. visible-light lasers). Do you want a transparent material? Y/N")) == 'y':
				self.appendNotes("Transparent: No DR vs. visible-light lasers.")
				self.CF += 1.0
		if "HalfVsNonCrushing" in self.keywords:
			self.appendNotes("Split DR: provides full protection against crushing attacks and uses its reduced DR against all other types of damage.")
			self.specDR = self.DR/2.0
		if "WeakToImpaling" in self.keywords and self.material.TL <= 4:
			self.appendNotes("-1 DR vs. impaling.")
		if "WeakToCrushing" in self.keywords and self.construction in (Scale, UltraTechScale) and self.DR < 5:
			self.appendNotes("-1 DR vs. crushing.")
		if "WeakToCrushing" in self.keywords and self.construction == Mail:
			if self.DR > 10:
				self.appendNotes("-" + str(round(0.001+self.DR*0.2)) + "DR vs. crushing.")
			else:
				self.appendNotes("-2 DR vs. crushing.")

	def qualityAdjust(self):
		if self.CF != 1.0:
			self.cost *= self.CF
		if self.WF != 1.0:
			self.weight *= self.WF
	def donCalc(self):
		if self.flex == True:
			if self.material.TL >= 7:
				self.timeToDon = 3.0
			else:
				self.timeToDon = self.locations.surfaceArea*self.construction.don*2.0/3.0
		else:
			self.timeToDon = self.locations.surfaceArea*self.construction.don
	def weightCalc(self):
		self.weight = self.locations.surfaceArea*self.material.WM*self.construction.CW*self.DR
	def costCalc(self):
		if self.TL >= 6 and self.material in [StrongSteel,HardSteel]:
			self.cost = (self.weight*self.material.CM*self.construction.CC)*0.04
		elif self.TL >= self.material.costBreakTL:
			self.cost = (self.weight*self.material.CM*self.construction.CC)*self.material.costBreakMult
		else:
			self.cost = self.weight*self.material.CM*self.construction.CC
	def LCCalc(self):
		# NOTE: LC is pretty arbitrary. Many additional rules may be
		# introduced to make it line up with existing items, but this
		# is simple enough for full suits.
		if self.DR * 6 <= self.material.maxDR:
			self.LC = 4
		elif self.DR * 4 <= self.material.maxDR:
			self.LC = 3
		elif self.DR * 2 <= self.material.maxDR:
			self.LC = 2
		else:
			self.LC = 1
	def output(self):
		print("\nArmour Name: {}".format(self.name))
		if "Superscience" in self.material.keywords:
			print("TL: {}^".format(str(self.TL)))
		else:
			print("TL: {}".format(str(self.TL)))
		if "LaserOnly" in self.material.keywords:
			print("DR: {}/0{}".format(str(round(self.DR)),self.asterisk))
		elif self.specDR == 0:
			print("DR: {}{}".format(str(round(self.DR)),self.asterisk))
		elif self.specDR > self.DR:
			print("DR: {}/{}{}".format(str(round(self.specDR)),str(round(self.DR)),self.asterisk))
		elif self.DR > self.specDR:
			print("DR: {}/{}{}".format(str(round(self.DR)),str(round(self.specDR)),self.asterisk))
		print("Weight: {}".format(str(_round2sf(self.weight))))
		print("Cost: {}".format(str(_round2sf(self.cost))))
		print("LC: {}".format(str(self.LC)))
		print("Locations: {}".format(str(self.locations.name)))
		print("Time to Don: {}".format(str(self.timeToDon)))
		print("Notes: {}".format(str(self.notes)))
	def GCSOutput(self, f):
		et = ET.ElementTree()
		try:
			root = et.parse(f)
		except ET.ParseError:
			eqpid = uuid4()
			root = ET.Element("equipment_list", attrib={"id": str(eqpid), "version": str(1)})
			et = ET.ElementTree(element=root)

		equipment = ET.SubElement(root, "equipment", attrib={"version": str(4)})

		quantity = ET.SubElement(equipment, "quantity")
		quantity.text = "1"

		description = ET.SubElement(equipment, "description")
		description.text = self.name

		tech_level = ET.SubElement(equipment, "tech_level")
		tech_level.text = str(self.TL)

		legality_class = ET.SubElement(equipment, "legality_class")
		legality_class.text = str(self.LC)

		value = ET.SubElement(equipment, "value")
		value.text = str(_round2sf(self.cost))

		weight = ET.SubElement(equipment, "weight")
		weight.text = str(_round2sf(self.weight))

		notes = ET.SubElement(equipment, "notes")
		notes.text = str(self.notes)

		categories = ET.SubElement(equipment, "categories")
		category = ET.SubElement(categories, "category")
		category.text = "Armor"

		for locationName in self.locations.GCSNames:
			dr_bonus = ET.SubElement(equipment, "dr_bonus")
			location = ET.SubElement(dr_bonus, "location")
			location.text = locationName
			amount = ET.SubElement(dr_bonus, "amount")
			amount.text = str(self.DR)

		# Rewrite the file's contents as the new XML tree
		f.seek(0)
		f.truncate(0)
		et.write(f, xml_declaration=True)

		# Rewrite the XML tree in "pretty" form,
		# since GCS's XML parsing is line-based.
		f.seek(0)
		doc = minidom.parse(f)
		f.seek(0)
		f.truncate(0)
		f.write(doc.toprettyxml().encode())
	def debugOutput(self):
		print("\nArmour Name: {}".format(self.name))
		if "Superscience" in self.material.keywords:
			print("TL: {}^".format(str(self.TL)))
		else:
			print("TL: {}".format(str(self.TL)))
		if "LaserOnly" in self.material.keywords:
			print("DR: {}/0{}".format(str(round(self.DR)),self.asterisk))
		elif self.specDR == 0:
			print("DR: {}{}".format(str(round(self.DR)),self.asterisk))
		elif self.specDR > self.DR:
			print("DR: {}/{}{}".format(str(round(self.specDR)),str(round(self.DR)),self.asterisk))
		elif self.DR > self.specDR:
			print("DR: {}/{}{}".format(str(round(self.DR)),str(round(self.specDR)),self.asterisk))
		print("Time to Don: {}".format(str(self.timeToDon)))
		print("Weight: {}".format(str(_round2sf(self.weight))))
		print("Cost: {}".format(str(_round2sf(self.cost))))
		print("LC: {}".format(str(self.LC)))
		print("Locations: {}".format(str(self.locations.name)))
		print("Notes: {}".format(str(self.notes)))
		print("Material: {}".format(str(self.material.name)))
		print("Material TL: {}".format(str(self.material.TL)))
		print("Construction: {}".format(str(self.construction.name)))
		print("Total Surface Area: {}".format(str(self.locations.surfaceArea)))
		print("Final Cost Factor: {}".format(str(self.CF)))
		print("Keywords: {}".format(str(self.keywords)))


### INPUT & CALCULATION ###
  # Takes input from the command line/shell for user-defined properties without having to alter the code to do it.
  # Then the input information us used to instantiate an armour object, and the armour.execute() method called, which calculates all properties and prints them.
  # If you add more hit locations, materials or constructions, make sure to add them to the information here, as it is currently very important that they be formatted correctly.

print("""\n==== GURPS ArmourGen ====

    Version: 0.1 (2016-10-28)

    Part of the GURPSGen suite made by CTA. For more information see https://github.com/GURPSGen/ArmourGen

    GURPS is a trademark of Steve Jackson Games, and its rules and art are copyrighted by Steve Jackson
    Games. All rights are reserved by Steve Jackson Games. This game aid is the original creation of CTA
    and is released for free distribution, and not for resale, under the permissions granted in the Steve
    Jackson Games Online Policy (http://www.sjgames.com/general/online_policy.html).

== == == == == == == == == == == == \n""")

while True:

	TempTL = eval(input("Please enter the TL of your armour:\n"))

	print("""\nThe materials you can use are:
  TL0: Bone, Cloth, Horn, Leather, Silk, Wood
  TL1: CheapBronze, GoodBronze, Copper, Jade, GemJade, Stone
  TL2: CheapIron, GoodIron, Lead
  TL3: StrongSteel
  TL4: HardSteel
  TL6: Aluminium, HardSteel, HighStrengthSteel, Rubber
  TL7: BallisticResin, BasicCeramic, ElasticPolymer, Fibreglass, HighStrengthAluminium, Nomex, Nylon, Plastic, Polycarbonate, Titanium, TitaniumAlloy, VeryHardSteel
  TL8: Aramid, BallisticPolymer, ImpBallisticPolymer, ImpCeramic, ImpKevlar, ImpNomex, Kevlar, LaminatedPolycarbonate, PolymerComposite, TitaniumComposite, UltraStrengthSteel
  TL9: Arachnoweave, CeramicNanocomposite, EarlyNanoweave, LaserAblativePolymer, MagneticLiquidArmour, PolymerNanocomposite, Reflec, ShearThickeningFluidArmour, TitaniumNanocomposite
 TL10: AdvancedNanoLaminate, AdvancedPolymerNanocomposite, AdvancedNanoweave, Bioplas, ElectromagneticArmour, NanoAblativePolymer
 TL11: Diamondoid, DiamondoidLaminate, Monocrys, RetroReflective
 TL12: EnergyCloth, Hyperdense, HyperdenseLaminate
  TL^: Adamant, Orichalcum

Please use the exact capitalisation, spacing and spelling. Not all materials are compatible with all constructions. If in doubt, use common sense, but an error message will be printed if they are incompatible.\n""")

	TempMaterial = eval(input("Please enter the material of your armour:\n"))

	print("""\nThe construction types you can use are:
  Fabric, LayeredFabric, Scale, Mail, SegmentedPlate, Plate, Solid, OptimisedFabric, ImpactAbsorbing and UltraTechScale.

Please use the exact capitalisation, spacing and spelling, otherwise the calculations may fail.\n""")

	TempConstruction = eval(input("Please enter the construction of your armour:\n"))

	TempDR = eval(input("Please enter the DR of your armour:\n"))

	print("""The body areas you can use are: Head (which includes Skull, Face and Neck), Torso (which includes Chest, Abdomen and Groin), Arms (which includes Shoulders, UpperArms, Elbows and Forearms), Hands, Legs (which includes Thighs, Knees and Shins) and Feet.

You can use any combination of the hit locations and sub-locations, but be aware that there is currently no check to see whether you've entered the same area twice (e.g. Torso and Abdomen). Please use the exact capitalisation, spacing and spelling, and seperate locations with addition signs (+) if you are using more than one location.\n""")

	TempLocations = eval(input("Please enter the areas your armour will cover:\n"))

	print("""If you want to add qualities or properties, choose from the following:
  Quality Grades: QualityCheap, QualityFine, QualityVeryFine
  Properties: PropertyBandedMail, PropertyElvenMail, PropertyFluted, PropertyHighlyArticulated, PropertyMountainScale, PropertyThieves\n\n""")

	TempQualities = []
	while True:
		QualityInput = input("Enter any qualities or properties, one at a time. Leave blank to finish:\n")

		if QualityInput != "" and QualityInput in MasterQualityList:
			TempQualities.append(QualityInput)
			continue
		elif QualityInput != "":
			print("Error: {} is not a valid quality or property!\n".format(QualityInput))
			continue
		else:
			break

	TempName = input("Please enter the name of your armour:\n")

	UserDefinedArmour = Armour(TempName,TempTL,TempDR,TempLocations,TempMaterial,TempConstruction)
	UserDefinedArmour.keywords.extend(TempQualities)
	UserDefinedArmour.execute()

	OutFile = input("Enter file name to save output to or blank to skip writing:\n")
	if OutFile:
		with open(OutFile, "r+b" if os.path.exists(OutFile) else "w+b") as f:
			UserDefinedArmour.GCSOutput(f)

	print("\n- - - - - - - - - - - - - - -\n")

	if str.casefold(input("Do you want to generate another armour? Type y to start again, or anything else to finish.\n")) == "y":
		continue
	else:
		break

