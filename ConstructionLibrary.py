### CONSTRUCTIONS LIBRARY ###

# This file stores construction objects. The constructions are instatiated using keyword arguments on multiple lines so that the format is clear.

from ClassLibrary import ArmourConstruction

BlankConstruction = ArmourConstruction(
			name="Name",						# Construction's name as a string.
			desc="Description.",					# Description of the construction (be brief).
			TL=0,							# Tech level.
			CW=0.0,							# Construction weight - [...]
			CC=0.0,							# Construction cost - [...]
			don=0,							# Time taken to don [...]. 
			minDR=0,						# Minimum DR possible for the material.
			keywords=["Keyword1","Keyword2"]			# Keywords used to define more complex behaviour. See below for more information.
			)

Construction1 = BlankConstruction
Construction2 = BlankConstruction

### LOW-TECH ###

Fabric = ArmourConstruction(
			name="Fabric",
			TL=0,
			CW=1.0,
			CC=1.0,
			don=2.14,
			minDR=1,
			keywords=["WeakToImpaling"]
			)

LayeredFabric = ArmourConstruction(
			name="Layered fabric",
			TL=0,
			CW=1.2,
			CC=1.5,
			don=4.28,
			minDR=2,
			keywords=[]
			)

Scale = ArmourConstruction(
			name="Scale",
			TL=1,
			CW=1.1,
			CC=0.8,
			don=4.28,
			minDR=2,
			keywords=["WeakToCrushing"]
			)

Mail = ArmourConstruction(
			name="Mail",
			TL=2,
			CW=0.9,
			CC=1.2,
			don=2.14,
			minDR=2,
			keywords=["WeakToCrushing"]
			)

SegmentedPlate = ArmourConstruction(
			name="Segmented plate",
			TL=2,
			CW=1.45,
			CC=1.5,
			don=6.42,
			minDR=3,
			keywords=[]
			)

Plate = ArmourConstruction(
			name="Plate",
			TL=1,
			CW=0.8,
			CC=5.0,
			don=6.42,
			minDR=3,
			keywords=[]
			)

Solid = ArmourConstruction(
			name="Solid",
			TL=1,
			CW=1.0,
			CC=1.0,
			don=2.0,
			minDR=10,
			keywords=[]
			)

### CUTTING EDGE ###

ImpactAbsorbing = ArmourConstruction(
			name="Impact-absorbing",
			TL=6,
			CW=0.65,
			CC=5.0,
			don=6.42,
			minDR=2,
			keywords=["HalfVsNonCrushing"]
			)

OptimisedFabric = ArmourConstruction(
			name="Optimised fabric",
			TL=6,
			CW=0.8,
			CC=2.0,
			don=2.14,
			minDR=2,
			keywords=[]
			)

### TECH AND TOYS IV ###

UltraTechScale = ArmourConstruction(
			name="Scale",
			TL=9,
			CW=1.1,
			CC=0.8,
			don=4.28,
			minDR=2,
			keywords=["Flexible"]
			)
