### MATERIALS LIBRARY ###

# This file stores material objects. The materials are grouped by TL and instatiated using keyword arguments on multiple lines so that the format is clear.

from ConstructionLibrary import *
from ClassLibrary import ArmourMaterial

BlankMaterial = ArmourMaterial(
			name="Name",						# Material's name as a string.
			desc="Description.",					# Description of the material (be brief).
			TL=0,							# Tech level.
			WM=0.0,							# Weight modifer - the weight of a slab of 1 square foot providing DR 1.
			CM=0.0,							# Cost modifier - the cost per pound.
			DRperInch=0,						# DR provided by one inch of the material. 
			minDR=0,						# Minimum DR possible for the material; defaults to 0 (no minimum).
			maxDR=0,						# Maximum DR possible for the material.
			specDRMult=1.0,						# Multiplier for split or special DR.
			costBreakTL=1000,					# The TL at which cost is reduced. Use 1000 for no reduction.
			costBreakMult=1.0,					# The cost multiple when cost is reduced by TL.
			constructions=[Construction1,Construction2],		# Valid construction types the material can use.
			keywords=["Keyword1","Keyword2"]			# Keywords used to define more complex behaviour. See below for more information.
			)

# Implement new keyword behaviour:
#	Powered (requires power, work out that stuff)

# Add a PowerUse variable to the armour class so that we can do things like electromagnetic armour, magnetic armour, etc. Will be helpful for custom armour too.

# Add the costBreakTL and costBreakMult variables to allow for systemic reduction in price at higher TLs:
  # At +1 TL:
    # 1/2 (ElasticPolymer, Nomex, LaserAblativePolymer, MagneticLiquidArmour, ShearThickeningFluidArmour, BasicCeramic, Fibreglass, HighStrengthAluminium, Polycarbonate, LaminatedPolycarbonate, Bioplas, NanoAblativePolymer, AdvancedNanoweave, Monocrys, AdvancedNanoLaminate, AdvancedPolymerComposite, ElectromagneticArmour, Diamondoid, DiamondoidLaminate)
    # 1/2.5 (ImpBallisticPolymer)
    # 1/3 (Improved Kevlar)
    # *0.26666 (UltraStengthSteel)
    # 1/4 (BallisticPolymer, Kevlar, PolymerComposite, CeramicNanocomposite, PolymerNanocomposite)
    # *0.24 (Nylon, TitaniumNanocomposite)
    # 1/5 (Arachnoweave, BasicNanoweave, TitaniumAlloy, ImprovedCeramic)
    # 1/10 (TitaniumComposite)


###  TL0 ###

Bone = ArmourMaterial(
			name="Bone",
			desc="Animal bone is strong but brittle, and can be made into scale armour or helmets.",
			TL=0,
			WM=1.0,
			CM=12.5,
			DRperInch=8,
			maxDR=4,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Scale,Solid],
			keywords=["SemiAblative"]
			)

Cloth = ArmourMaterial(
			name="Cloth",
			desc="Tough padded cloth fabric.",
			TL=0,
			WM=0.85,
			CM=8.0,
			DRperInch=4,
			maxDR=4,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric],
			keywords=["Combustible","Flexible"]
			)

Horn = ArmourMaterial(
			name="Horn",
			desc="Horns and various natural materials such as ivory, shells, and hooves.",
			TL=0,
			WM=1.0,
			CM=12.5,
			DRperInch=8,
			maxDR=4,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Scale,Solid],
			keywords=[]
			)

Leather = ArmourMaterial(
			name="Leather",
			desc="Prepared and cured animal hide.",
			TL=0,
			WM=0.9,
			CM=10.0,
			DRperInch=8,
			maxDR=4,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric,LayeredFabric,Scale],
			keywords=["Combustible","Flexible"]
			)

Silk = ArmourMaterial(
			name="Silk",
			desc="Silk can be used to make cloth armour that helps to prevent infection, and reduces the effectiveness of some barbed weapons.",
			TL=0,
			WM=0.85,
			CM=160,
			DRperInch=4,
			maxDR=4,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric],
			keywords=["Combustible","Flexible","SilkBenefits"]
			)

Wood = ArmourMaterial(
			name="Wood",
			desc="Dense wood such as oak or teak.",
			TL=0,
			WM=1.4,
			CM=3.0,
			DRperInch=1.5,
			maxDR=2,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Scale,Solid],
			keywords=["Combustible","SemiAblative"]
			)

###  TL1 ###

CheapBronze = ArmourMaterial(
			name="Cheap bronze",
			desc="Bronze is a copper-tin alloy and is the most common material for TL1 armour. Rarer at higher TLs due to its cost.",
			TL=1,
			WM=0.9,
			CM=60.0,
			DRperInch=48,
			maxDR=9,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

GoodBronze = ArmourMaterial(
			name="Good bronze",
			desc="Typical quality of bronze used in most armour",
			TL=1,
			WM=0.6,
			CM=100.0,
			DRperInch=68,
			maxDR=14,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

Copper = ArmourMaterial(
			name="Copper",
			desc="Copper is too soft to make good armour but useful for ceremonial armor or for some fey folk or mages who cannot abide the touch of iron.",
			TL=1,
			WM=1.6,
			CM=80.0,
			DRperInch=30,
			maxDR=5,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

Jade = ArmourMaterial(
			name="Jade",
			desc="Jade can be used to make scale armour, like stone, but is visually impressive and expensive.",
			TL=1,
			WM=1.2,
			CM=62.5,
			DRperInch=13,
			maxDR=5,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Scale,Solid],
			keywords=["ReactionsP2","SemiAblative"]
			)

GemJade = ArmourMaterial(
			name="Gem-quality jade",
			desc="Gem-quality jade can be used to make scale armour, like stone, but is visually impressive and very expensive.",
			TL=1,
			WM=1.2,
			CM=125.0,
			DRperInch=13,
			maxDR=5,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Scale,Solid],
			keywords=["ReactionsP3","SemiAblative"]
			)

Stone = ArmourMaterial(
			name="Stone",
			desc="Stone chipped into scales for armour.",
			TL=1,
			WM=1.2,
			CM=12.5,
			DRperInch=13,
			maxDR=5,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Scale,Solid],
			keywords=["SemiAblative"]
			)

###  TL2 ###

CheapIron = ArmourMaterial(
			name="Cheap iron",
			desc="Average-quality smith-forged iron, roughly the equivalent of mass-produced mild steel of today.",
			TL=2,
			WM=0.8,
			CM=15.0,
			DRperInch=52,
			maxDR=10,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

GoodIron = ArmourMaterial(
			name="Good iron",
			desc="Low-tech, high-quality smith-forged iron. Limitations on the technology mean that larger iron plates are unavailable until TL4.",
			TL=2,
			WM=0.6,
			CM=25.0,
			DRperInch=68,
			maxDR=14,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

Lead = ArmourMaterial(
			name="Lead",
			desc="Lead is too soft and heavy to make good metal armour but some super-strong races that don’t like the touch of iron may use it anyway.",
			TL=2,
			WM=2.0,
			CM=12.5,
			DRperInch=30,
			maxDR=4,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

###  TL3 ###

StrongSteel = ArmourMaterial(
			name="Strong steel",
			desc="Roughly equivalent to modern RHA steel, but requiring a lot more effort to make.",
			TL=3,
			WM=0.58,
			CM=50.0,
			DRperInch=70,
			maxDR=14,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

###  TL4 ###

HardSteel = ArmourMaterial(
			name="Hard steel",
			desc="Highest-quality smith forged steel.",
			TL=4,
			WM=0.5,
			CM=250.0,
			DRperInch=81,
			maxDR=16,
			specDRMult=1.0,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[]
			)

###  TL5 ###



###  TL6 ###

Aluminium = ArmourMaterial(
			name="Aluminium",
			desc="One-third the density of steel but only half as strong.",
			TL=6,
			WM=0.45,
			CM=15.0,
			DRperInch=31,
			maxDR=5.0,
			specDRMult=1.0,
			costBreakTL=7,		# Using same numbers from HighStrengthAluminium
			costBreakMult=0.5,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[]
			)

HardSteel = ArmourMaterial(
			name="Hard steel",
			desc="Face-hardened high-strength steel or high-hardness alloys.",
			TL=6,
			WM=0.5,
			CM=3.5,
			DRperInch=82,
			maxDR=16,
			specDRMult=1.0,
			costBreakTL=6,
			costBreakMult=0.04,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

HighStrengthSteel = ArmourMaterial(
			name="High-strength steel",
			desc="Rolled homogenous armour plate.",
			TL=6,
			WM=0.58,
			CM=3.0,
			DRperInch=70,
			maxDR=14,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

Rubber = ArmourMaterial(
			name="Rubber",
			desc="Natural or synthetic rubber.",
			TL=6,
			WM=0.45, #check
			CM=5.0,
			DRperInch=14,
			maxDR=7,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Combustible","Flexible","SemiAblative"],
			)


###  TL7 ###

BallisticResin = ArmourMaterial(
			name="Ballistic resin",
			desc="Various rigid fibre-reinforced composites.",
			TL=7,
			WM=0.55,
			CM=2.5,
			DRperInch=15,
			maxDR=6,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

BasicCeramic = ArmourMaterial(
			name="Basic ceramic",
			desc="Boron carbide or aluminium oxide ceramics (or for transparent armour, possibly quartz).",
			TL=7,
			WM=0.2,
			CM=25.0,
			DRperInch=83,
			maxDR=25,
			specDRMult=1.0,
			costBreakTL=8,
			costBreakMult=0.5,
			constructions=[Solid],
			keywords=["SemiAblative","Transparent"],
			)

ElasticPolymer = ArmourMaterial(
			name="Elastic polymer",
			desc="Synthetic elastomer materials like neoprene or Spandex and various blends. Commonly used in wetsuits, lightweight protective gear and superhero costumes.",
			TL=7,
			WM=0.16,
			CM=100.0,
			DRperInch=16,
			maxDR=8,
			specDRMult=1.0,
			costBreakTL=8,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Flexible"],
			)

Fibreglass = ArmourMaterial(
			name="Fibreglass",
			desc="Tough glass-reinforced plastic, e.g. S-glass.",
			TL=7,
			WM=0.6,
			CM=8.0,
			DRperInch=17,
			maxDR=7,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["SemiAblative"],
			)

HighStrengthAluminium = ArmourMaterial(
			name="High-strength aluminium",
			desc="Aerospace-grade aluminium alloy.",
			TL=7,
			WM=0.4,
			CM=12.0,
			DRperInch=35,
			maxDR=10,
			specDRMult=1.0,
			costBreakTL=8,
			costBreakMult=0.5,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

Nomex = ArmourMaterial(
			name="Nomex",
			desc="Flame-resistant meta-aramids, often reinforced with nylon or neoprene.",
			TL=7,
			WM=0.264,
			CM=50.0,
			DRperInch=3,
			maxDR=2,
			specDRMult=4.0,
			costBreakTL=8,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["FireResistant","Flexible"],
			)

Nylon = ArmourMaterial(
			name="Nylon",
			desc="Silky synthetic thermoplastic fabric; stronger ballistic-weave nylon was used in early body armour and protective gear.",
			TL=7,
			WM=1.0,
			CM=25.0,
			DRperInch=6,
			maxDR=3,
			specDRMult=1.0,
			costBreakTL=8,
			costBreakMult=0.24,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Flexible"],
			)

Plastic = ArmourMaterial(
			name="Plastic",
			desc="Ordinary thermoplastic material.",
			TL=7,
			WM=0.75,
			CM=1.8,
			DRperInch=12,
			maxDR=3,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Transparent"],
			)

Polycarbonate = ArmourMaterial(
			name="Polycarbonate",
			desc="Tough high-impact moulded plastic; may be transparent at extra cost.",
			TL=7,
			WM=0.45,
			CM=10.0,
			DRperInch=10,
			maxDR=3,
			specDRMult=1.0,
			costBreakTL=8,
			costBreakMult=0.5,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["SemiAblative"],
			)

Titanium = ArmourMaterial(
			name="Titanium",
			desc="Titanium is very strong for its weight, and retains that strength well at high temperatures.",
			TL=7,
			WM=0.4,
			CM=50.0,
			DRperInch=57,
			maxDR=12,
			specDRMult=1.0,
			costBreakTL=8,		# Using same numbers from TitaniumAlloy
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[]
			)

TitaniumAlloy = ArmourMaterial(
			name="Titanium alloy",
			desc="Strong but costly light alloy.",
			TL=7,
			WM=0.35,
			CM=50.0,
			DRperInch=66,
			maxDR=20,
			specDRMult=1.0,
			costBreakTL=8,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=[],
			)

VeryHardSteel = ArmourMaterial(
			name="Very hard steel",
			desc="High-hardness steel alloys.",
			TL=7,
			WM=0.45,
			CM=20.0,
			DRperInch=90,
			maxDR=18,
			specDRMult=1.0,
			costBreakTL=1000,	# Does it need one?
			costBreakMult=1.0,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[]
			)

###  TL8 ###

Aramid = ArmourMaterial(
			name="Aramid fabric",
			desc="Material used in Kevlar soft body armour; can also represent ballistic plastic fabric.",
			TL=8,
			WM=0.16,
			CM=80.0,
			DRperInch=12,
			maxDR=5,
			specDRMult=4.0,
			costBreakTL=1000,	# Does it need one?
			costBreakMult=1.0,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"]
			)

BallisticPolymer = ArmourMaterial(
			name="Balllistic polymer",
			desc="Flexible plastic fibre composites such as Spectra Shield and Dyneema made from ultra-high molecular weight polyethylene. Costlier but tougher than Kevlar.",
			TL=8,
			WM=0.15,
			CM=200.0,
			DRperInch=20,
			maxDR=10,
			specDRMult=2.5,
			costBreakTL=9,
			costBreakMult=0.25,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

ImpBallisticPolymer = ArmourMaterial(
			name="Improved ballistic polymer",
			desc="Latest generation of of ballistic polymers.",
			TL=8,
			WM=0.1,
			CM=250.0,
			DRperInch=30,
			maxDR=15,
			specDRMult=2.5,
			costBreakTL=9,
			costBreakMult=0.4,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

ImpCeramic = ArmourMaterial(
			name="Improved ceramic",
			desc="Costlier ceramics, e.g. silicon carbide, either with polymer or alloy backing plate, or encapsulated in a polymer material.",
			TL=8,
			WM=0.15,
			CM=100.0,
			DRperInch=111,
			maxDR=44,
			specDRMult=1.0,
			costBreakTL=9,
			costBreakMult=0.2,
			constructions=[Solid],
			keywords=["SemiAblative"],
			)
 
ImpKevlar = ArmourMaterial(
			name="Improved kevlar",
			desc="Costlier late-TL8 para-aramid materials using more sophisticated ballistic weaves.",
			TL=8,
			WM=0.24,
			CM=120.0,
			DRperInch=12,
			maxDR=7,
			specDRMult=3.0,
			costBreakTL=9,
			costBreakMult=(2.0/3.0),
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

ImpNomex = ArmourMaterial(
			name="Improved nomex",
			desc="Meta-aramid fabric reinforced with Kevlar.",
			TL=8,
			WM=0.22,
			CM=35.0,
			DRperInch=3,
			maxDR=2,
			specDRMult=4.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric,OptimisedFabric],
			keywords=["FireResistant","Flexible"],
			)

Kevlar = ArmourMaterial(
			name="Kevlar",
			desc="Woven para-aramid fabric such as Kevlar or Twaron.",
			TL=8,
			WM=0.4,
			CM=80.0,
			DRperInch=8,
			maxDR=4,
			specDRMult=4.0,
			costBreakTL=9,
			costBreakMult=0.25,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

LaminatedPolycarbonate = ArmourMaterial(
			name="Laminated polycarbonate",
			desc="Advanced multi-layered polycarbonate and polyurethane laminate, often used for transparent armour visors.",
			TL=8,
			WM=0.25,
			CM=25.0,
			DRperInch=12,
			maxDR=5,
			specDRMult=1.0,
			costBreakTL=9,
			costBreakMult=0.5,
			constructions=[Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["SemiAblative","Transparent"],
			)

PolymerComposite = ArmourMaterial(
			name="Polymer composite",
			desc="Carbon-fibre reinforced plastic or resin-bonded Kevlar. Often used to make ballistic helmets.",
			TL=8,
			WM=0.22,
			CM=40.0,
			DRperInch=28,
			maxDR=11,
			specDRMult=1.0,
			costBreakTL=9,
			costBreakMult=0.25,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

TitaniumComposite = ArmourMaterial(
			name="Titanium composite",
			desc="Titanium metal matrix composite - alloy reinforced by high-strength ceramic particles or fibres.",
			TL=8,
			WM=0.2,
			CM=250.0,
			DRperInch=104,
			maxDR=42,
			specDRMult=1.0,
			costBreakTL=9,
			costBreakMult=0.1,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

UltraStrengthSteel = ArmourMaterial(
			name="Ultra-strength steel",
			desc="Triple hardened steel alloys or nanostructured steel.",
			TL=8,
			WM=0.35,
			CM=30.0,
			DRperInch=116,
			maxDR=23,
			specDRMult=1.0,
			costBreakTL=9,
			costBreakMult=(1.0/3.75),
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

###  TL9 ###

Arachnoweave = ArmourMaterial(
			name="Arachnoweave",
			desc="Spider silk produced using genetic engineering technology.",
			TL=9,
			WM=0.12,
			CM=600.0,
			DRperInch=24,
			maxDR=12,
			specDRMult=4.0,
			costBreakTL=10,
			costBreakMult=0.2,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

CeramicNanocomposite = ArmourMaterial(
			name="Ceramic nanocomposite",
			desc="Ceramic nanoparticles in an elastic medium.",
			TL=9,
			WM=0.1,
			CM=300.0,
			DRperInch=166,
			maxDR=66,
			specDRMult=1.0,
			costBreakTL=10,
			costBreakMult=0.25,
			constructions=[Solid],
			keywords=["SemiAblative"],
			)

EarlyNanoweave = ArmourMaterial(
			name="Early nanoweave",
			desc="Late-TL9 flexible armour using polymers reinforced by primitive carbon nanotubes.",
			TL=9,
			WM=0.09,
			CM=750.0,
			DRperInch=38,
			maxDR=19,
			specDRMult=3.0,
			costBreakTL=10,
			costBreakMult=0.2,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

LaserAblativePolymer = ArmourMaterial(
			name="Laser-ablative polymer",
			desc="Ballistic polymer built to evaporate when heated, absorbing laser fire.",
			TL=9,
			WM=0.108,
			CM=150.0,
			DRperInch=24,
			maxDR=12,
			specDRMult=6.0,
			costBreakTL=10,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["EnergyAblative","Flexible"],
			)

MagneticLiquidArmour = ArmourMaterial(
			name="Magnetic liquid armour",
			desc="Ballistic armour incorporating microtubules filled with magneto-rheological fluid (ferrous metallic particles suspended in a carrier liquid). The liquid can instantly transition from flexible to rigid metallic panels as sensors in the armor detect impacts and trigger an electric charge. The armor is self-powered (using a wearable flexible power supply that is recharged by the wearer’s muscle movements).",
			TL=9,
			WM=0.064,
			CM=200.0,
			DRperInch=45,
			maxDR=23,
			specDRMult=2.0,
			costBreakTL=10,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

PolymerNanocomposite = ArmourMaterial(
			name="Polymer nanocomposite",
			desc="Plastic reinforced by carbon or boron nanotubes.",
			TL=9,
			WM=0.1,
			CM=400.0,
			DRperInch=83,
			maxDR=33,
			specDRMult=1.0,
			costBreakTL=10,
			costBreakMult=0.25,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)
 
Reflec = ArmourMaterial(
			name="Reflec",
			desc="Highly reflective armour made from polished metallic fibers that reflects laser fire. Useless against other attacks but can be worn over other armour.",
			TL=9,
			WM=0.005,
			CM=150,
			DRperInch=833,
			maxDR=30,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric,OptimisedFabric],
			keywords=["LaserOnly","Flexible","Superscience"]
			)

ShearThickeningFluidArmour = ArmourMaterial(
			name="STF liquid armour",
			desc="Ballistic fabric whose protective qualities are enhanced by ceramic nanoparticles soaked in sheer-thickening “liquid armor” fluid. They transition to a rigid material upon impact.",
			TL=9,
			WM=0.096,
			CM=150.0,
			DRperInch=30,
			maxDR=15,
			specDRMult=3.0,
			costBreakTL=10,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

TitaniumNanocomposite = ArmourMaterial(
			name="Titanium nanocomposite",
			desc="Titanium composite reinforced by carbon or boron nanotubes.",
			TL=9,
			WM=0.12,
			CM=250.0,
			DRperInch=174,
			maxDR=70,
			specDRMult=1.0,
			costBreakTL=10,
			costBreakMult=0.24,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=[],
			)

### TL10 ###

AdvancedNanoLaminate = ArmourMaterial(
			name="Advanced nano-laminate",
			desc="Multi-layered composite armor incorporating advanced polymer, titanium, or beryllium composites; ultra-hard ceramic nanocomposites; and reactive materials over an inner layer of spall and shock-absorbing bioplas, nanoweave, or liquid armor.",
			TL=10,
			WM=0.04,
			CM=200,
			DRperInch=166,
			minDR=35,
			maxDR=66,
			specDRMult=1.0,
			costBreakTL=11,
			costBreakMult=0.5,
			constructions=[Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Laminate"],
			)

AdvancedPolymerNanocomposite = ArmourMaterial(
			name="Advanced polymer nanocomposite",
			desc="",
			TL=10,
			WM=0.08,
			CM=50,
			DRperInch=104,
			maxDR=42,
			specDRMult=1.0,
			costBreakTL=11,
			costBreakMult=0.5,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Transparent"],
			)

AdvancedNanoweave = ArmourMaterial(
			name="Advanced nanoweave",
			desc="Fabric reinforced by woven ultra-strong nanotubes.",
			TL=10,
			WM=0.024,
			CM=150,
			DRperInch=46,
			maxDR=24,
			specDRMult=3.0,
			costBreakTL=11,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

Bioplas = ArmourMaterial(
			name="Bioplas",
			desc="Smart polymer with superior damage resistance and the ability to heal tears and punctures.",
			TL=10,
			WM=0.045,
			CM=600,
			DRperInch=93,
			maxDR=31,
			specDRMult=3.0,
			costBreakTL=11,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Bio","Flexible","Transparent"]
			)

ElectromagneticArmour = ArmourMaterial(
			name="Electromagnetic armour",
			desc="Layers of thick-spaced plates or, at higher TLs, superconductor layers that generate an intense electromagnetic field, disrupting the penetrating jet and degrading or nullifying its effect.",
			TL=10,
			WM=0.01,
			CM=100,
			DRperInch=666,
			minDR=35,
			maxDR=264,
			specDRMult=1.0,
			costBreakTL=11,
			costBreakMult=0.5,
			constructions=[Plate,SegmentedPlate,Scale,Solid],
			keywords=["Powered"],
			)

NanoAblativePolymer = ArmourMaterial(
			name="Nano-ablative polymer",
			desc="Flexible composite with laser-absorbing nanotubes",
			TL=10,
			WM=0.024,
			CM=150,
			DRperInch=46,
			maxDR=22,
			specDRMult=6.0,
			costBreakTL=11,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["EnergyAblative","Flexible"]
			)

### TL11 ###

Diamondoid = ArmourMaterial(
			name="Diamondoid",
			desc="Super-hard diamond-like material created through molecular nanotechnology.",
			TL=11,
			WM=0.06,
			CM=50,
			DRperInch=232,
			maxDR=93,
			specDRMult=1.0,
			costBreakTL=12,
			costBreakMult=0.5,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Transparent"],
			)

DiamondoidLaminate = ArmourMaterial(
			name="Diamondoid laminate",
			desc="Multilayer composite of diamondoid, titanium carbide, bioplas, monocrys, and shockand radiation-absorbing reactive polymers.",
			TL=11,
			WM=0.03,
			CM=200,
			DRperInch=420,
			minDR=35,
			maxDR=168,
			specDRMult=1.0,
			costBreakTL=12,
			costBreakMult=0.5,
			constructions=[Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Laminate"],
			)

Monocrys = ArmourMaterial(
			name="Monocrys",
			desc="Flexible diamondoid ballistic molecular mesh.",
			TL=11,
			WM=0.018,
			CM=150,
			DRperInch=62,
			maxDR=31,
			specDRMult=3.0,
			costBreakTL=12,
			costBreakMult=0.5,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Ballistic","Flexible"],
			)

RetroReflective = ArmourMaterial(
			name="Retro-reflective armour",
			desc="Armor with embedded metallic fibers covering spherical micro-lenses whose mirrors reflect laser fire back at the attacker.",
			TL=11,
			WM=0.0025,
			CM=1500,
			DRperInch=1666,
			maxDR=166,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric,OptimisedFabric],
			keywords=["LaserOnly","Flexible","Superscience"],
			)

### TL12 ###

EnergyCloth = ArmourMaterial(
			name="Energy cloth",
			desc="Hyperdense exotic smart matter fabric that is both flexible and exceedingly damage-resistant.",
			TL=12,
			WM=0.014,
			CM=500,
			DRperInch=240,
			maxDR=120,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Fabric,OptimisedFabric],
			keywords=["Flexible"]
			)

Hyperdense = ArmourMaterial(
			name="Hyperdense",
			desc="Laminate of steel and exotic collapsed matter.",
			TL=12,
			WM=0.04,
			CM=50,
			DRperInch=2083,
			minDR=10,
			maxDR=417,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Laminate"],
			)

HyperdenseLaminate = ArmourMaterial(
			name="Hyperdense laminate",
			desc="Complex laminate of hyperdense exotic matter, ultra-tough synthetics and exotic shock- and energy-absorbing smart matter.",
			TL=12,
			WM=0.02,
			CM=200,
			DRperInch=1040,
			minDR=35,
			maxDR=278,
			specDRMult=1.0,
			costBreakTL=1000,
			costBreakMult=1.0,
			constructions=[Plate,SegmentedPlate,Scale,Solid,ImpactAbsorbing],
			keywords=["Laminate"],
			)

###  TL^ ###

Adamant = ArmourMaterial(
			name="Adamant",
			desc="Magical crystal or stone with triple the strength of stone, as detailed in GURPS Fantasy. It may represent other fantastic crystalline materials.",
			TL=1,
			WM=0.33,
			CM=900.0,
			DRperInch=27,
			maxDR=15,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Scale,Solid],
			keywords=["SemiAblative","Superscience"]
			)

Orichalcum = ArmourMaterial(
			name="Orichalcum",
			desc="Legendary metal with triple the strength of bronze, as detailed in GURPS Fantasy. It may represent various super-strong fantasy metals.",
			TL=1,
			WM=0.2,
			CM=3000.0,
			DRperInch=204,
			maxDR=41,
			costBreakTL=5,
			costBreakMult=0.2,
			constructions=[Mail,Plate,SegmentedPlate,Scale,Solid],
			keywords=["Superscience"]
			)
