### CLASS LIBRARY ###

# This file stores definitions of the classes used this program. This file does not instantiate any of these objects; these are done in separate libraries.

## Construction ##

class ArmourConstruction:
	def __init__(self, name = "BLANK CONSTRUCTION", desc = "", TL = 0, CW = 0.0, CC = 0.0, don = 0.0, minDR = 0, keywords = []):
		self.name = name
		self.desc = desc
		self.TL = TL
		self.CW = CW
		self.CC = CC
		self.don = don
		self.minDR = minDR
		self.keywords = keywords

# Keyword definitions:
	#HalfVsNonCrushing - normal DR vs. crushing, half against anything else.
	#WeakToCrushing - suffers reduced DR to crushing attacks (usually mail or scale, etc.).
	#WeakToImpaling - suffers reduced DR to impaling attacks (usually fabric armours).

## Material ##

class ArmourMaterial:
	def __init__(self, name = "BLANK MATERIAL", desc = "", TL = 0, WM = 0, CM = 0, DRperInch = 0.0, minDR = 0, maxDR = 0, specDRMult = 1.0, costBreakTL = 1000, costBreakMult = 1.0, constructions = [], keywords = []):
		self.name = name
		self.desc = desc
		self.TL = TL
		self.WM = WM
		self.CM = CM
		self.DRperInch = DRperInch
		self.minDR = minDR
		self.maxDR = maxDR
		self.specDRMult = specDRMult
		self.costBreakTL = costBreakTL
		self.costBreakMult = costBreakMult
		self.constructions = constructions
		self.keywords = keywords

# Keyword definitions:
	# Ballistic - has increased DR against piercing and cutting attacks; the multiplier is defined at the bottom of this section.
	# Bio - has 3x DR against burning and cutting attacks and can self-repair.
	# Combustible - if DR is penetrated by burning damage, can catch on fire.
	# EnergyAblative - 6x DR against lasers but increased DR is ablative.
	# FireResistant - 4x DR against burning damage.
	# Flexible - if the armour has less than a quarter of the material's DR per inch it's flexible but quicker to don.
	# Laminate - DR is doubled vs. shaped-charge warheads and plasma bolts.
	# LaserOnly - DR protects against lasers only; no DR against any other attacks.
	# ReactionsP2 - gives +2 to reactions.
	# ReactionsP3 - gives +3 to reactions.
	# SemiAblative - DR is semi-ablative.
	# SilkBenefits - has benefits against infection, barbed attacks, and blood agents and contact poisons.
	# Transparent - the material can be transparent, providing no DR vs visible-light lasers for double cost.

## Hit Location ##

# NOT FULLY IMPLEMENTED #

class HitLocation:
	def __init__(self, name = "", surfaceArea = 0.0, contains = "[]", partOf = "", adjacent = "[]"):
		self.name = name
		self.surfaceArea = SurfaceArea
		self.contains = contains
		self.partOf = partOf
		self.adjacent = adjacent
