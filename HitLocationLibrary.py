### HIT LOCATION LIBRARY ###

# This file stores hit location objects. The constructions are instatiated using keyword arguments on multiple lines so that the format is clear.

def _combine_hit_locations(args):
	s = set()
	for component in args:
		if isinstance(component, _HitLocation):
			s.add(component)
		elif isinstance(component, _CombinedHitLocation):
			s.update(component.components)
		else:
			assert False
	return frozenset(s)
def _add_hit_locations(*args):
	components = _combine_hit_locations(args)
	names = sorted(component.name for component in components)
	if len(names) == 1:
		full_name = names[0]
	else:
		full_name = '{} and {}'.format(', '.join(names[:-1]), names[-1])
	return _CombinedHitLocation(name=full_name, components=components)

class NoGCSName(Exception):
	def __init__(self, name):
		self.name = name
		super().__init__(self, "Hit Location {} has no corresponding location in GCS".format(name))

class _HitLocation:
	def __init__(self, name, surfaceArea, GCSName=None):
		self.name = name
		self.surfaceArea = surfaceArea
		self.GCSName = GCSName
	@property
	def GCSNames(self):
		if self.GCSName is None:
			raise NoGCSName(self.name)
		yield self.GCSName
	def __add__(self, other):
		return _add_hit_locations(self, other)

class _CombinedHitLocation:
	def __init__(self, name, components):
		self.name = name
		self.components = _combine_hit_locations(components)
	@property
	def surfaceArea(self):
		return sum(component.surfaceArea
		           for component in self.components)
	@property
	def GCSNames(self):
		for component in self.components:
			yield from component.GCSNames
	def __add__(self, other):
		return _add_hit_locations(self, other)


Skull = _HitLocation(name="Skull", surfaceArea=1.4, GCSName="skull")
Face = _CombinedHitLocation(name="Face", components=(
		_HitLocation(name="Face", surfaceArea=0.7, GCSName="face"),
		_HitLocation(name="Eyes", surfaceArea=0, GCSName="eyes"),
	))
Head = _CombinedHitLocation(name="Head", components=(Skull, Face))

Neck = _HitLocation(name="Neck", surfaceArea=0.35, GCSName="neck")

Vitals = _HitLocation(name="Vitals only", surfaceArea=1, GCSName="vitals")
Chest = _CombinedHitLocation(name="Chest", components=(
		_HitLocation(name="Chest without Vitals", surfaceArea=4.25),
		Vitals,
	))
Groin = _HitLocation(name="Groin only", surfaceArea=0.35, GCSName="groin")
Abdomen = _CombinedHitLocation(name="Abdomen", components=(
		_HitLocation(name="Abdomen without Groin", surfaceArea=1.4),
		Groin,
	))
Torso = _CombinedHitLocation(name="Torso", components=(
		Groin,
		_HitLocation(name="Torso without Groin", surfaceArea=5.65,
                            GCSName="torso"),
	))

Shoulders = _HitLocation(name="Both Shoulders", surfaceArea=0.7)
UpperArms = _HitLocation(name="Both Upper Arms", surfaceArea=0.7)
Elbows = _HitLocation(name="Both Elbows", surfaceArea=0.35)
Forearms = _HitLocation(name="Both Forearms", surfaceArea=1.75)
Arms = _HitLocation(name="Both Arms", surfaceArea=3.5, GCSName="arms")

Hands = _HitLocation(name="Both Hands", surfaceArea=0.7, GCSName="hands")

Thighs = _HitLocation(name="Both Thighs", surfaceArea=3.15)
Knees = _HitLocation(name="Both Knees", surfaceArea=0.35)
Shins = _HitLocation(name="Both Shins", surfaceArea=3.5)
Legs = _HitLocation(name="Both Legs", surfaceArea=7, GCSName="legs")

Feet = _HitLocation(name="Both Feet", surfaceArea=0.7, GCSName="feet")

All = _HitLocation(name="All locations except eyes", surfaceArea=21.35,
                  GCSName="full body except eyes")
Bodysuit = _CombinedHitLocation(name="Bodysuit", components=(
		Torso, Arms, Hands, Legs, Feet,
	))
Suit = _CombinedHitLocation(name="Full suit", components=(
		Neck, Torso, Arms, Hands, Legs, Feet,
	))
Coverall = _CombinedHitLocation(name="Coverall", components=(
		Torso, Arms, Legs,
	))
Jacket = _CombinedHitLocation(name="Jacket", components=(
		Torso, Arms,
	))
Trousers = _CombinedHitLocation(name="Trousers", components=(
		Groin, Legs,
	))
