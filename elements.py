import defaults 
from random import shuffle


class area(object):
	"""docstring for area"""
	def __init__(self, name, connection, owned=None):
		super(area, self).__init__()
		self.connection = connection
		self.owned = owned
		self.name = name

	def __repr__(self):
		return self.name


class sea(area):
	"""docstring for sea"""
	def __init__(self, name, connection, owned=None):
		super(sea, self).__init__(name, connection)
		self.boats = []

class land(area):
	"""docstring for land"""
	def __init__(self, name, connection):
		super(land, self).__init__(name, connection)
		self.tanks = []
		
class city(area):
	"""docstring for city"""
	def __init__(self, name, connection, nation, factory, owned=None):
		super(city, self).__init__(name, connection)
		self.boats = []
		self.tanks = []
		self.nation = nation
		self.factory = factory
		self.occupied = False

class canal(land):
	"""docstring for canal"""
	def __init__(self, name, connection):
		super(canal, self).__init__(name, connection)

		

class factory(object):
	"""docstring for factory"""
	def __init__(self, build, kind):
		super(factory, self).__init__()
		self.build = build
		self.kind = kind

	def __repr__(self):
		return self.kind

	def buildunit():
		pass

class unit(object):
	"""docstring for unit"""
	def __init__(self, nation):
		super(unit, self).__init__()
		self.nation = nation
		self.friendly = False
		self.kind = None
		self.moved = False

	def __repr__(self):
		return self.kind

class boat(unit):
	"""docstring for boat"""
	def __init__(self):
		super(boat, self).__init__()
		self.kind = 'Boat'
		self.conveyed = False


class tank(unit):
	"""docstring for tank"""
	def __init__(self):
		super(tank, self).__init__()
		self.kind = 'Tank'

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
		else:
			print 'no, none default settings implemented.'

	def __str__(self):
		return str(self.players + self.nations + self.areas)

	def getareas(self, areatype):
		pass

	def getunitmoveoptions(self, unittype):
		pass

	def getsaldo(self, entity):
		pass

	def getfreecities(self, nation):
		pass

	def getfreebuildingspots(self, nation):
		pass

	def buildfactory(self, area):
		pass

	def changesaldo(self, entity, amount):
		pass

	def getbuildfactories(self, nation):
		pass

	def buildunit(self, area):
		# perhaps area property or use for import?
		pass

	def buildunits(self, nation):
		pass

	def getfleets(self, nation):
		pass

	def getarmies(self, nation):
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
				if city in self.navalyard.keys():
					h.append(city(name=ci, connection=self.connections[ci], factory=factory(kind='Navalyard', build=self.navalyard[ci]), nation=nation))
				if city in self.factory.keys():
					h.append(city(name=ci, connection=self.connections[ci], factory=factory(kind='Factory', build=self.factory[ci]), nation=nation))
		c = [canal(name=area, connection=self.connections[area]) for area in self.canals]
		return l + s + h + c

if __name__ == '__main__':
	g = game()
	print g
	print g.players
	print g.nations
	print g.areas

		





		
		



		
		

		
		


		
		
		
		
		
