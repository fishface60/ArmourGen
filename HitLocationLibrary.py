### HIT LOCATION LIBRARY ###

	# NOT CURRENTLY IMPLEMENTED; THIS IS STORAGE FOR FUTURE CODE ##

# This file stores hit location objects. The constructions are instatiated using keyword arguments on multiple lines so that the format is clear.

# New hit location code

#Examples
Torso = HitLocation(
		name="Torso",
		surfaceArea=7.0,
		contains="[Chest,Abdomen,Groin,Vitals]",
		partOf="",
		adjacent="[Neck,Arms,legs]",
		)

Vitals = HitLocation(
		name="Vitals",
		surfaceArea=1.0,
		contains="[]",
		partOf="Torso",		# This is a chicken-and-egg problem; can't be defined until Torso is defined but Torso cannot be defined until Vitals is defined because it has to be instantiated with Vitals in its self.contains property.
		adjacent="[]",
		)

# This re-evalutes the components of each HitLocation object, since we can't instantiate an object untill all of the object it references are instantiated, which is impossible.
for each in HitLocationMasterList:
	each.contains = eval(each.contains)
	each.partOf = eval(each.partOf)
	each.adjacent = eval(each.adjacent)

# Old hit location code

def CreateHitLocations():

	Vitals = HitLocation(1.0,[])
	Groin = HitLocation(0.35,[])

	Skull = HitLocation(1.4,[])
	Face = HitLocation(0.7,[])
	Neck = HitLocation(0.35,[])
	Chest = HitLocation(5.25,[Vitals])
	Abdomen = HitLocation(1.75,[Groin])
	Shoulders = HitLocation(0.7,[])
	UpperArms = HitLocation(0.7,[])
	Elbows = HitLocation(0.35,[])
	Forearms = HitLocation(1.75,[])
	Hands = HitLocation(0.7,[])
	Thighs = HitLocation(3.15,[])
	Knees = HitLocation(0.35,[])
	Shins = HitLocation(3.5,[])
	Feet = HitLocation(0.7,[])

	Head = HitLocation(2.1,[Skull,Face])
	Torso = HitLocation(7.0,[Chest,Abdomen])
	Arms = HitLocation(3.5,[Shoulders,UpperArms,Elbows,Forearms])
	Legs = HitLocation(7.0,[Thighs,Knees,Shins])

	Skull.adj([Face])
	Face.adj([Skull,Neck])
	Neck.adj([Face,Chest])
	Chest.adj([Neck,Shoulders,Abdomen])
	Abdomen.adj([Chest,Thighs])
	Shoulders.adj([Chest,UpperArms])
	UpperArms.adj([Shoulders,Elbows])
	Elbows.adj([UpperArms,Forearms])
	Forearms.adj([Elbows,Hands])
	Hands.adj([Forearms])
	Thighs.adj([Abdomen,Knees])
	Knees.adj([Thighs,Shins])
	Shins.adj([Knees,Feet])
	Feet.adj([Shins])

	Head.adj([Neck])
	Torso.adj([Neck,Arms,Legs])
	Arms.adj([Torso,Hands])
	Legs.adj([Torso,Feet])

	#Directional *= 0.5
	#HalfCoverage *= 0.5
	#Skimpy *= 0.25

def SurfaceAreaSum(LocationList):
	total = 0.0
	for each in LocationList:
		total += each.surfaceArea
	return total

