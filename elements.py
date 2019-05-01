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

	def moveunit(self, other, unittype):
		'''moves a not moved unit from self to other'''
		for unitindex in range(len(self.units)):
			if not self.units[unitindex].notmoved() and isinstance(self.units[unitindex], unittype):
				print str(other)
				print other.units
				other.units.append(self.units.pop(unitindex))
				print str(other)
				print other.units
				break

	def getfleets(self):
		return [unit for unit in self.units if isinstance(unit, boat)]

	def gettanks(self):
		return [unit for unit in self.units if isinstance(unit, tank)]


class sea(area):
	"""docstring for sea"""
	def __init__(self, name, connection, owned=None):
		super(sea, self).__init__(name, connection, owned)

	def hasboats(self):
		print "poep boat"
		return len(self.getfleets()) > 0


class land(area):
	"""docstring for land"""
	def __init__(self, name, connection, owned=None):
		super(land, self).__init__(name, connection, owned)

	def hastanks(self):
		print "poep tank"
		return len(self.gettanks()) > 0
	

class city(land):
	"""docstring for city"""
	def __init__(self, name, connection, nation, factory, owned=None):
		super(city, self).__init__(name, connection, owned)
		self.nation = nation
		self.factory = factory
		self.occupied = False

	def hasboats(self):
		return len(self.getfleets()) > 0

	def buildunit(self):
		if self.factory.isbuild():
			self.units.append(self.factory.buildunit(self.nation))



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

	def buildunit(self, nation):
		return tank(nation)

class shipyard(factory):
	"""docstring for shipyard"""
	def __init__(self, build):
		super(shipyard, self).__init__(build)

	def buildunit(self, nation):
		return boat(nation)


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

	def notmoved(self):
		return self.moved

class boat(unit):
	"""docstring for boat"""
	def __init__(self, nation):
		super(boat, self).__init__(nation)
		self.conveyed = False
		self.kind = 'Boat'


class tank(unit):
	"""docstring for tank"""
	def __init__(self, nation):
		super(tank, self).__init__(nation)
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
		else:
			print 'no none default settings implemented.'

	def __str__(self):
		return str(self.players + self.nations + self.areas)

	def getareas(self, nation):
		'''returns list of areas controlled by nation, including homecities'''
		return [area for area in self.areas if area.owner() == str(nation)]

	def getfleets(self, nation):
		'''returns list of areas controlled by nation which has boats, including homecities'''
		return [area for area in self.getareas(nation) if area.hasboats()]


	def getarmies(self, nation):
		'''returns list of areas controlled by nation which has tanks, including homecities'''
		return [area for area in self.getareas(nation) if area.hastanks()]


	def getareamoveoptions(self, area, areatype=None):
		'''returns list of area objects with possible destinations from current area. With areatype it is possible to make sub selection'''
		if areatype != None:
			return [dest for dest in self.areas if str(dest) in area.getareamoveoptions() if isinstance(dest, areatype)]
		return [dest for dest in self.areas if str(dest) in area.getareamoveoptions()]

		


	def getfreecities(self, nation):
		pass

	def getfreebuildingspots(self, nation):
		pass

	def buildfactory(self, area):
		pass



	def getbuildfactories(self, nation):
		pass

	def buildunit(self, area):
		# perhaps area property or use for import?
		pass

	def buildunits(self, nation):
		pass



	def destroyfactory(self, area):
		pass


	def convey(self):
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
				if ci in self.navalyard.keys():
					h.append(city(name=ci, connection=self.connections[ci], factory=shipyard(build=self.navalyard[ci]), nation=nation, owned=nation))
				if ci in self.factory.keys():
					h.append(city(name=ci, connection=self.connections[ci], factory=armarent(build=self.factory[ci]), nation=nation, owned=nation))
		c = [canal(name=area, connection=self.connections[area]) for area in self.canals]
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
		print
		print "getting areas of nation"
		print g.getareas(nation)
		print "fleet update, pre build"
		print g.getfleets(nation)
		print "tank update, pre build"
		print g.getarmies(nation)
		print
		print "building tanks and fleets in al possible places"
		print
		for area in g.getareas(nation):
			area.buildunit()
		print "fleet update, post build"
		print g.getfleets(nation)
		for area in g.getfleets(nation):
			print
			print "from {} all move options: {}".format(area, g.getareamoveoptions(area=area))
			print "from {} sea move options: {}".format(area, g.getareamoveoptions(area=area, areatype=sea))
			if len(g.getareamoveoptions(area=area, areatype=sea)) > 0:
				area.moveunit(choice(g.getareamoveoptions(area=area, areatype=sea)), unittype=boat)
				print "new locations:"
				print g.getfleets(nation)
		print
		print "tank update, post build"
		print g.getarmies(nation)
		for area in g.getarmies(nation):
			print
			print "from {} all move options: {}".format(area, g.getareamoveoptions(area=area))
			print "from {} land move options: {}".format(area, g.getareamoveoptions(area=area, areatype=land))
			if len(g.getareamoveoptions(area=area, areatype=land)) > 0:
				area.moveunit(choice(g.getareamoveoptions(area=area, areatype=land)), unittype=tank)
				print "new locations:"
				print g.getarmies(nation)
		print
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








		





		
		



		
		

		
		


		
		
		
		
		
