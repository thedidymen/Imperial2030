import defaults 
from random import shuffle, choice
from collections import Counter
# import pdb; pdb.set_trace()


class Area(object):
	"""docstring for area"""
	def __init__(self, name, connection, owned=None):
		super(Area, self).__init__()
		self.connection = connection
		self.owned = owned
		self.name = name
		self.units = []

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def owner(self):
		return self.owned

	def getareamoveoptions(self):
		return self.connection

	def getenemyunits(self, nation):
		return [unit for unit in self.units if unit.nation != nation]

	def unitfreqnation(self):
		return Counter([unit.nation for unit in self.units])

	# def getnotconveyedboats(self, nation):
	# 	# a fleet must be at sea to convey
	# 	return []


class Sea(Area):
	"""docstring for sea"""
	def __init__(self, name, connection, owned=None):
		super(Sea, self).__init__(name, connection, owned)

	def getnotconveyedboats(self, nation):
		return [unit for unit in self.units if not unit.conveyed if unit.nation == nation]


class Land(Area):
	"""docstring for land"""
	def __init__(self, name, connection, owned=None):
		super(Land, self).__init__(name, connection, owned)


class City(Land):
	"""docstring for city"""
	def __init__(self, name, connection, nation, factory, owned=None):
		super(City, self).__init__(name, connection, owned)
		self.nation = nation
		self.factory = factory
		self.occupied = False

	def buildunit(self):
		'''returns unit if factory is build and area is not occupied'''
		if self.factory.isbuild() and not self.occupied:
			return self.factory.buildunit(self.nation, self)


class Canal(Land):
	"""docstring for canal"""
	def __init__(self, name, connection):
		super(Canal, self).__init__(name, connection)

		
class Factory(object):
	"""docstring for factory"""
	def __init__(self, build):
		super(Factory, self).__init__()
		self.build = build

	def __repr__(self):
		return self.kind

	def buildunit(self):
		return None

	def isbuild(self):
		return self.build

	def build(self):
		self.build = True


class Armarent(Factory):
	"""docstring for Armerent"""
	def __init__(self, build):
		super(Armarent, self).__init__(build)

	def buildunit(self, nation, location):
		u = Tank(nation, location)
		location.units.append(u)
		return u


class Shipyard(Factory):
	"""docstring for shipyard"""
	def __init__(self, build):
		super(Shipyard, self).__init__(build)

	def buildunit(self, nation, location):
		u = Boat(nation, location)
		location.units.append(u)
		return u


class Unit(object):
	"""docstring for unit"""

	number = 0

	def __init__(self, nation, location):
		super(Unit, self).__init__()
		self.nation = nation
		self.friendly = False
		self.kind = None
		self.moved = False
		self.location = location
		Unit.number += 1
		self.number = Unit.number


	def __repr__(self):
		return self.kind + " " + str(self.number) + " " + str(self.nation)

	def moved(self):
		return self.moved

	def ismoved(self):
		self.moved = True

	def gainmovement(self):
		self.moved = False

	def setlocation(self, location):
		self.location = location

	def getlocation(self):
		return self.location

	def moveoptions(self):
		return self.location.getareamoveoptions()

	def move(self, location):
		if not self.moved:
			self.location.units.remove(self)
			self.setlocation(location)
			self.location.units.append(self)
			self.ismoved()
			return self.location.getenemyunits(self.nation)

	def kill(self, unit=None):
		if unit != None:
			unit.kill()
		self.location.units.remove(self)

	def conveyoptions(self, currentpath=None):
		'''returns dict with eindpoints as key and a list containing a chain of seaareas'''
		convoypath = {}
		landingareas = [area for area in self.location.getareamoveoptions() if isinstance(area, Land)]
		seaareas = [area for area in self.moveoptions() if len(area.units) > 0 if isinstance(area, Sea)]
		if currentpath == None:
			currentpath = []
		currentpath.append(self.location)
		for area in landingareas:
			convoypath[area] = currentpath
		for area in seaareas:
			units = area.getnotconveyedboats(self.nation)
			# lets not go loops on the map
			if area not in currentpath and len(units) > 0:
				convoypath.update(units[0].conveyoptions(currentpath))
		return convoypath


class Boat(Unit):
	"""docstring for boat"""
	def __init__(self, nation, location):
		super(Boat, self).__init__(nation, location)
		self.conveyed = False
		self.kind = 'Boat'

	def moveoptions(self):
		return [a for a in self.location.getareamoveoptions() if isinstance(a, Sea)]

	def gainconvey(self):
		self.conveyed = False


class Tank(Unit):
	"""docstring for tank"""
	def __init__(self, nation, location):
		super(Tank, self).__init__(nation, location)
		self.kind = 'Tank'

	def moveoptions(self):
		return [a for a in self.location.getareamoveoptions() if isinstance(a, Land)]

	def conveyoptions(self):
		seaareas = [a for a in self.location.getareamoveoptions() if isinstance(a, Sea)]
		conveypath = {}
		for area in seaareas:
			units = area.getnotconveyedboats(self.nation)
			# lets not go loops on the map
			if len(units) > 0:
				conveypath.update(units[0].conveyoptions())
		conveypath.pop(self.location, None)
		return conveypath

	def move(self, location):
		if location in self.moveoptions():
			return super(Tank, self).move(location)
		if location in self.conveyoptions().keys():
			b = False
			for area in self.conveyoptions()[location]:
				for unit in area.getnotconveyedboats(self.nation):
					if not unit.conveyed:
						unit.conveyed = True
						break
			return super(Tank, self).move(location)


class Bond(object):
	"""docstring for bond"""
	def __init__(self, share, interest, nation, owner='bank'):
		super(Bond, self).__init__()
		self.owner = owner
		self.nation = nation
		self.share = share
		self.interest = interest

	def __repr__(self):
		return "{} bonds of {}".format(self.bonds, self.nation)


class Entity(object):
	"""docstring for entity"""
	def __init__(self, name, bonds=None):
		super(Entity, self).__init__()
		self.name = name
		self.money = 0
		if bonds == None:
			self.bonds = []
		else:
			self.bonds = bonds
	
	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def getsaldo(self):
		return self.money

	def changesaldo(self, amount):
		'''returns True if saldo + amount > 0 and gain amount to current saldo, else False and does not gain amount to saldo'''
		if self.money + amount > 0:
			self.money += amount
			return True
		else: 
			return False	


class Nation(Entity):
	"""docstring for nation"""
	def __init__(self, homeareas, name, bonds):
		super(Nation, self).__init__(name, bonds)
		self.homeareas = homeareas
		self.powerlvl = 0
		self.areas = []
		self.controlledby = None

	def numberofflags(self):
		number = 0
		for area in self.areas:
			if not isinstance(area, City):
				number += 1
		return number

	def occupyingcities(self):
		# If a city only has enemy units of the unfriendly kind, the city becomes occupied.
		pass

	def placingflags(self):
		''''''
		# needs to change the owner of an area, if only one nation has units in the area. 
		# Also the number of flags should not exceed 15. Cities should not count to this number.
		
		# numberofflags...
		pass


class Player(Entity):
	"""docstring for player"""
	def __init__(self, name):
		super(Player, self).__init__(name)
		self.investor = False
		self.swissbank = False
		self.controlsnation = []


class Game(object):
	"""docstring for game"""
	def __init__(self, default=True):
		super(Game, self).__init__()
		if default:
			cg = creategame()
			self.players = cg.createplayers()
			shuffle(self.players)
			self.nations = cg.createnations()
			self.areas = cg.createareas(self.nations)
			self.units = {nation : [] for nation in self.nations}
		else:
			print 'no none default settings implemented.'

	def __str__(self):
		return str(self.players + self.nations + self.areas)

	def getareas(self, nation):
		'''returns list of areas controlled by nation, including homecities'''
		# return [area for area in self.areas if area.owner() == str(nation)]
		return [area for area in self.areas if area.owner() == nation]

	def getareamoveoptions(self, area, areatype=None):
		'''returns list of area objects with possible destinations from current area. With areatype it is possible to make sub selection'''
		if areatype != None:
		# 	return [dest for dest in self.areas if str(dest) in area.getareamoveoptions() if isinstance(dest, areatype)]
		# return [dest for dest in self.areas if str(dest) in area.getareamoveoptions()]
			return [dest for dest in self.areas if dest in area.getareamoveoptions() if isinstance(dest, areatype)]
		return [dest for dest in self.areas if dest in area.getareamoveoptions()]

	def buildunits(self, nation):
		# optimize... use nation.homecities?
		for area in self.areas:
			if isinstance(area, City) and area.owned == nation:
				unit = area.buildunit()
				if unit != None:
					print "building unit @ {}".format(unit.location)
					self.units[nation].append(unit)

	def getfleets(self, nation):
		return [unit for unit in self.units[nation] if isinstance(unit, Boat)]

	def getarmies(self, nation):
		return [unit for unit in self.units[nation] if isinstance(unit, Tank)]

	def gainmovement(self, nation):
		for unit in self.getfleets(nation):
			unit.gainmovement()
		for unit in self.getarmies(nation):
			unit.gainmovement()

	def gainconvey(self, nation):
		for unit in self.getfleets(nation):
			unit.gainconvey()

	def battle(self, unit, enemy):
		# need to implement check if current area is still owned by current nation. 
		# for example blue invades an area occupied by green and yellow and red, which is owned
		# by green. Green gets destroyed by blue. Yellow and red remain. Ownership
		# should be returned to None
		self.units[unit.nation].remove(unit)
		self.units[enemy.nation].remove(enemy)
		unit.kill(enemy)

	def getareatype(self):
		pass


	

class creategame(object):
	"""docstring for creategame"""
	def __init__(self):
		super(creategame, self).__init__()
		self.nations = defaults.nations
		self.bonds = defaults.bonds
		self.connections = defaults.connections
		self.landareas = defaults.landareas
		self.seaareas = defaults.seaareas
		self.canals = defaults.canals
		self.homecities = defaults.homecities
		self.navalyard = defaults.navalyard
		self.factory = defaults.factory
		self.players = defaults.players

	def createplayers(self):
		return [Player(name=p) for p in self.players]

	def createbonds(self, nation):
		return [Bond(share=b, interest=self.bonds[b], nation=nation) for b in self.bonds.keys()]

	def createnations(self):
		return [Nation(name=natie, bonds=self.createbonds(nation=natie), homeareas=self.homecities[natie]) for natie in self.nations]

	def createareas(self, nationsobj):
		l = [Land(name=area, connection=self.connections[area]) for area in self.landareas]
		s = [Sea(name=area, connection=self.connections[area]) for area in self.seaareas]
		h = []
		# making the nation variable in cities the nationobject, used in game.battle. needs refactoring?
		for nation in self.nations:
			for nationob in nationsobj:
				if nation == str(nationob):
					nationobj = nationob
			for ci in self.homecities[nation]:
				if ci in self.navalyard.keys():
					h.append(City(name=ci, connection=self.connections[ci], factory=Shipyard(build=self.navalyard[ci]), nation=nationobj, owned=nationobj))
					nationobj.areas.append(h[-1])
				if ci in self.factory.keys():
					h.append(City(name=ci, connection=self.connections[ci], factory=Armarent(build=self.factory[ci]), nation=nationobj, owned=nationobj))
					nationobj.areas.append(h[-1])
		c = [Canal(name=area, connection=self.connections[area]) for area in self.canals]
		a = l + s + h + c

		# making connections objects instead of strings
		for area in a:
			connectionsobj = []
			for connectto in area.connection:
				for areaobj in a:
					if str(areaobj) == connectto:
						connectionsobj.append(areaobj)
						break
			area.connection = connectionsobj

		return l + s + h + c

if __name__ == '__main__':
	print "setting up game"
	g = Game()
	# print g
	# print "checking players"
	# print g.players
	# print
	# print "checking nations"
	# print g.nations
	# print
	# print "checking areas"
	# print g.areas
	# print
	# for nation in g.nations:
	# 	print
	# 	print "working on ", nation
	# 	print "checing fleet status"
	# 	print g.getfleets(nation)
	# 	print "checking army status"
	# 	print g.getarmies(nation)
	# 	print "building tanks and fleets in al possible places"
	# 	g.buildunits(nation)
	# 	g.buildunits(nation)
	# 	print "fleet status"
	# 	print g.getfleets(nation)
	# 	print "army status"
	# 	print g.getarmies(nation)
	# 	print 

	# 	for fleet in g.getfleets(nation):
	# 		print fleet.getlocation()
	# 		print "all surrounding areas:"
	# 		print fleet.moveoptions()
	# 		pick = choice(fleet.moveoptions())
	# 		print "randomlocation: " + str(pick)
	# 		enemies = fleet.move(pick)
	# 		if enemies:
	# 			g.battle(fleet, choice(enemies))
	# 		print "currently at:",
	# 		print fleet.getlocation()
	# 	print
	# 	for army in g.getarmies(nation):
	# 		print army.getlocation()
	# 		print "all surrounding areas:"
	# 		print army.moveoptions()
	# 		pick = choice(army.moveoptions())
	# 		print "randomlocation: " + str(pick)
	# 		enemies = army.move(pick)
	# 		if enemies:
	# 			g.battle(army, choice(enemies))
	# 		print "currently at:",
	# 		print army.getlocation()
	# 		print "{} has {} million".format(nation, nation.getsaldo())
	# 		nation.changesaldo(30)
	# 		print "{} has {} million".format(nation, nation.getsaldo())
	# 		print "nation tries pays 31 million"
	# 		nation.changesaldo(-31)
	# 		print "{} has {} million".format(nation, nation.getsaldo())
	# 	print 
	# 	print "player stuff"
	# 	print
	# 	for player in g.players:
	# 		print "{} has {} million".format(player, player.getsaldo())
	# 		player.changesaldo(20)
	# 		print "{} has {} million".format(player, player.getsaldo())
	# 		player.changesaldo(-5)
	# 		print "{} has {} million".format(player, player.getsaldo())
	# 		print "player tries to pay 30 million"
	# 		player.changesaldo(-30)
	# 		print "{} has {} million".format(player, player.getsaldo())

	# for i in range(200):
	# 	print
	# 	for nation in g.nations:
	# 		g.buildunits(nation)
	# 		for area in g.areas:
	# 			if area.units:
	# 				for u in area.units:
	# 					if u.nation == nation:
	# 						if not u in g.units[nation]:
	# 							pass

	# 		for fleet in g.getfleets(nation):
	# 			# print fleet.location, fleet.conveyoptions()
	# 			pick = choice(fleet.moveoptions())
	# 			enemies = fleet.move(pick)
	# 			if enemies:
	# 				enemy = choice(enemies)
	# 				g.battle(unit=fleet, enemy=enemy)
	# 		for army in g.getarmies(nation):
				# print
				# print army.location #, army.moveoptions(), army.conveyoptions().keys()
				# print "fleets: {}".format([fleet.location for fleet in g.getfleets(nation)])
				# forced convey
				# if len(army.conveyoptions().keys()) > 0:
				# 	pick = choice(army.conveyoptions().keys())
				# 	# print pick
				# 	enemies = army.move(pick)
				# 	if enemies:
				# 		enemy = choice(enemies)
				# 		print army.location
				# 		print "killing myself and {} @ {}".format(enemy, enemy.location)
				# 		g.battle(army, enemy)
				# 
				# convey and normal move
			# 	if len(army.moveoptions() + army.conveyoptions().keys()) > 0:
			# 		pick = choice(army.moveoptions() + army.conveyoptions().keys())
			# 		# print pick
			# 		enemies = army.move(pick)
			# 		# print enemies
			# 		if enemies:
			# 			enemy = choice(enemies)
			# 			g.battle(unit=army, enemy=enemy)
			# g.gainmovement(nation)
			# g.gainconvey(nation)
			# g.placingflags()

	def unitcheck(game):
		for nation in game.nations:
			areaunits = []
			gameunits = []
			for area in game.areas:
				areaunits += [unit for unit in area.units if unit.nation == nation]
			if game.units[nation]:
				gameunits = game.units[nation]
			for areaunit in areaunits:
				if not areaunit in gameunits:
					print "lost unit: {} @ {}".format(areaunit, areaunit.location)
					print "nation: ", areaunit.nation


	n =  200
	for nation in g.nations:
		print 
		print "current nation: {}".format(nation)
		print "checking units prebuild"
		unitcheck(g)
		print "building units"
		g.buildunits(nation)
		print "checking units postbuild"
		unitcheck(g)
		print
	print "playing {} rounds".format(n)
	for i in range(n):
		for nation in g.nations:
			print 
			print "current round: {}".format(i)
			print
			print "current nation: {}".format(nation)
			print "checking units prebuild"
			unitcheck(g)
			print "building units"
			g.buildunits(nation)
			print "checking units postbuild"
			unitcheck(g)
			print
			print "fleet movement"
			for fleet in g.getfleets(nation):
				print "checking units prepick/fleet.moveoptions"
				unitcheck(g)
				print str(fleet) + " from " + str(fleet.nation)
				print "fleet located @ {}".format(fleet.location)
				pick = choice(fleet.moveoptions())
				print "checking units postpick/fleet.moveoptions"
				print "premove"
				unitcheck(g)
				print "moving to {}".format(pick)
				enemies = fleet.move(pick)
				print "checking units postmove/ prepick enemy"
				unitcheck(g)
				print "moved to {}".format(fleet.location)
				if enemies:
					print "enemies at current location {}".format([str(u) + " from " + str(u.nation) for u in enemies])
					enemy = choice(enemies)
					print "checking units postpick enemy/prebattle"
					unitcheck(g)
					print "will battle {}".format(str(enemy) + " from " + str(enemy.nation) + " @ " + str(enemy.location))
					print "enemy exits in game.units: {}".format(enemy in g.units[nation])
					print "fleet exits in game.units: {}".format(fleet in g.units[nation])
					g.battle(unit=fleet, enemy=enemy)
					print "checking units postbattle"
					unitcheck(g)
				print
			print
			for army in g.getarmies(nation):
				if len(army.moveoptions() + army.conveyoptions().keys()) > 0:
					pick = choice(army.moveoptions() + army.conveyoptions().keys())
					enemies = army.move(pick)
					if enemies:
						enemy = choice(enemies)
						g.battle(unit=army, enemy=enemy)
			print "checking prereset next round"
			unitcheck(g)
			print "Reseting movement"
			g.gainmovement(nation)
			print "checking units postpick enemy"
			unitcheck(g)
			print "resetting convoyment"
			g.gainconvey(nation)
			print "checking units postpick enemy"
			unitcheck(g)
			print "gaining areas"
			g.placingflags()
			print "checking units postpick enemy"
			unitcheck(g)
			print
			print


		
		



		
		

		
		


		
		
		
		
		
