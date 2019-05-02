import defaults 
from random import shuffle, choice


class area(object):
	"""docstring for area"""
	def __init__(self, name, connection, owned=None):
		super(area, self).__init__()
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


class sea(area):
	"""docstring for sea"""
	def __init__(self, name, connection, owned=None):
		super(sea, self).__init__(name, connection, owned)


class land(area):
	"""docstring for land"""
	def __init__(self, name, connection, owned=None):
		super(land, self).__init__(name, connection, owned)


class city(land):
	"""docstring for city"""
	def __init__(self, name, connection, nation, factory, owned=None):
		super(city, self).__init__(name, connection, owned)
		self.nation = nation
		self.factory = factory
		self.occupied = False


	def buildunit(self):
		'''returns unit if factory is build and area is not occupied'''
		if self.factory.isbuild() and not self.occupied:
			return self.factory.buildunit(self.nation, self)


class canal(land):
	"""docstring for canal"""
	def __init__(self, name, connection):
		super(canal, self).__init__(name, connection)

		
class factory(object):
	"""docstring for factory"""
	def __init__(self, build):
		super(factory, self).__init__()
		self.build = build

	def __repr__(self):
		return self.kind

	def buildunit(self):
		pass

	def isbuild(self):
		return self.build

	def build(self):
		self.build = True


class armarent(factory):
	"""docstring for Armerent"""
	def __init__(self, build):
		super(armarent, self).__init__(build)

	def buildunit(self, nation, location):
		unit = tank(nation, location)
		location.units.append(unit)
		return unit


class shipyard(factory):
	"""docstring for shipyard"""
	def __init__(self, build):
		super(shipyard, self).__init__(build)

	def buildunit(self, nation, location):
		unit = boat(nation, location)
		location.units.append(unit)
		return unit


class unit(object):
	"""docstring for unit"""
	def __init__(self, nation, location):
		super(unit, self).__init__()
		self.nation = nation
		self.friendly = False
		self.kind = None
		self.moved = False
		self.location = location

	def __repr__(self):
		return self.kind

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
		if not self.moved and location in self.moveoptions():
			self.location.units.remove(self)
			self.setlocation(location)
			self.location.units.append(self)
			self.ismoved()


class boat(unit):
	"""docstring for boat"""
	def __init__(self, nation, location):
		super(boat, self).__init__(nation, location)
		self.conveyed = False
		self.kind = 'Boat'

	def moveoptions(self):
		return [a for a in self.location.getareamoveoptions() if isinstance(a, sea)]



class tank(unit):
	"""docstring for tank"""
	def __init__(self, nation, location):
		super(tank, self).__init__(nation, location)
		self.kind = 'Tank'

	def moveoptions(self):
		return [a for a in self.location.getareamoveoptions() if isinstance(a, land)]


class bond(object):
	"""docstring for bond"""
	def __init__(self, share, interest, nation, owner='bank'):
		super(bond, self).__init__()
		self.owner = owner
		self.nation = nation
		self.share = share
		self.interest = interest

	def __repr__(self):
		return "{} bonds of {}".format(self.bonds, self.nation)


class entity(object):
	"""docstring for entity"""
	def __init__(self, name, bonds=None):
		super(entity, self).__init__()
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


class nation(entity):
	"""docstring for nation"""
	def __init__(self, homeareas, name, bonds):
		super(nation, self).__init__(name, bonds)
		self.homeareas = homeareas
		self.powerlvl = 0
		self.areas = []
		self.controlledby = None


class player(entity):
	"""docstring for player"""
	def __init__(self, name):
		super(player, self).__init__(name)
		self.investor = False
		self.swissbank = False
		self.controlsnation = []


class game(object):
	"""docstring for game"""
	def __init__(self, default=True):
		super(game, self).__init__()
		if default:
			cg = creategame()
			self.players = cg.createplayers()
			shuffle(self.players)
			self.nations = cg.createnations()
			self.areas = cg.createareas()
			self.units = {nation : [] for nation in self.nations}
		else:
			print 'no none default settings implemented.'

	def __str__(self):
		return str(self.players + self.nations + self.areas)

	def getareas(self, nation):
		'''returns list of areas controlled by nation, including homecities'''
		return [area for area in self.areas if area.owner() == str(nation)]

	def getareamoveoptions(self, area, areatype=None):
		'''returns list of area objects with possible destinations from current area. With areatype it is possible to make sub selection'''
		if areatype != None:
			return [dest for dest in self.areas if str(dest) in area.getareamoveoptions() if isinstance(dest, areatype)]
		return [dest for dest in self.areas if str(dest) in area.getareamoveoptions()]

	def buildunits(self, nation):
		for area in self.areas:
			if isinstance(area, city) and area.owned == str(nation):
				unit = area.buildunit()
				if unit != None:
					self.units[nation].append(unit)

	def getfleets(self, nation):
		return [unit for unit in self.units[nation] if isinstance(unit, boat)]

	def getarmies(self, nation):
		return [unit for unit in self.units[nation] if isinstance(unit, tank)]

	# def nationhasfleets(self, nation):
	# 	return self.getfleets(nation)

	# def nationhasarmies(self, nation):
	# 	return self.getarmies(nation)

	# def getfreecities(self, nation):
	# 	pass

	# def getfreebuildingspots(self, nation):
	# 	pass

	# def buildfactory(self, area):
	# 	pass

	# def getbuildfactories(self, nation):
	# 	pass

	# def buildunit(self, area):
	# 	# perhaps area property or use for import?
	# 	pass



	# def destroyfactory(self, area):
	# 	pass


	# def convey(self):
	# 	pass
	

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
		return [player(name=p) for p in self.players]

	def createbonds(self, nation):
		return [bond(share=b, interest=self.bonds[b], nation=nation) for b in self.bonds.keys()]

	def createnations(self):
		return [nation(name=natie, bonds=self.createbonds(nation=natie), homeareas=self.homecities[natie]) for natie in self.nations]

	def createareas(self):
		l = [land(name=area, connection=self.connections[area]) for area in self.landareas]
		s = [sea(name=area, connection=self.connections[area]) for area in self.seaareas]
		h = []
		for nation in self.nations:
			for ci in self.homecities[nation]:
				if ci in self.navalyard.keys():
					h.append(city(name=ci, connection=self.connections[ci], factory=shipyard(build=self.navalyard[ci]), nation=nation, owned=nation))
				if ci in self.factory.keys():
					h.append(city(name=ci, connection=self.connections[ci], factory=armarent(build=self.factory[ci]), nation=nation, owned=nation))
		c = [canal(name=area, connection=self.connections[area]) for area in self.canals]
		a = l + s + h + c

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
	g = game()
	print g
	print "checking players"
	print g.players
	print
	print "checking nations"
	print g.nations
	print
	print "checking areas"
	print g.areas
	print
	for nation in g.nations:
		print
		print "working on ", nation
		print "checing fleet status"
		print g.getfleets(nation)
		print "checking army status"
		print g.getarmies(nation)
		print "building tanks and fleets in al possible places"
		g.buildunits(nation)
		print "fleet status"
		print g.getfleets(nation)
		print "army status"
		print g.getarmies(nation)
		print 

		for fleet in g.getfleets(nation):
			print fleet.getlocation()
			print "all surrounding areas:"
			print fleet.moveoptions()
			pick = choice(fleet.moveoptions())
			print "randomlocation: " + str(pick)
			fleet.move(pick)
			print "currently at:",
			print fleet.getlocation()
		print
		for army in g.getarmies(nation):
			print army.getlocation()
			print "all surrounding areas:"
			print army.moveoptions()
			pick = choice(army.moveoptions())
			print "randomlocation: " + str(pick)
			army.move(pick)
			print "currently at:",
			print army.getlocation()

		for i in range(100):
			for fleet in g.getfleets(nation):
				pick = choice(fleet.moveoptions())
				fleet.move(pick)
				fleet.gainmovement()
			for army in g.getarmies(nation):
				pick = choice(army.moveoptions())
				army.move(pick)
				army.gainmovement()
		print "{} has {} million".format(nation, nation.getsaldo())
		nation.changesaldo(30)
		print "{} has {} million".format(nation, nation.getsaldo())
		print "nation tries pays 31 million"
		nation.changesaldo(-31)
		print "{} has {} million".format(nation, nation.getsaldo())
	print 
	print "player stuff"
	print
	for player in g.players:
		print "{} has {} million".format(player, player.getsaldo())
		player.changesaldo(20)
		print "{} has {} million".format(player, player.getsaldo())
		player.changesaldo(-5)
		print "{} has {} million".format(player, player.getsaldo())
		print "player tries to pay 30 million"
		player.changesaldo(-30)
		print "{} has {} million".format(player, player.getsaldo())








		





		
		



		
		

		
		


		
		
		
		
		
