import defaults 
from random import shuffle, choice
from collections import Counter
# import pdb; pdb.set_trace()


class Area(object):
	"""docstring for area"""
	def __init__(self, name, connection, owner=None):
		super(Area, self).__init__()
		self.connection = connection
		self.owner = owner
		self.name = name
		self.units = []

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def getareamoveoptions(self):
		return self.connection

	def getenemyunits(self, nation):
		return [unit for unit in self.units if unit.nation != nation]

	def unitfreqnation(self):
		return Counter([unit.nation for unit in self.units])


class Sea(Area):
	"""docstring for sea"""
	def __init__(self, name, connection, owner=None):
		super(Sea, self).__init__(name, connection, owner)

	def getnotconveyedboats(self, nation):
		return [unit for unit in self.units if not unit.conveyed if unit.nation == nation]


class Land(Area):
	"""docstring for land"""
	def __init__(self, name, connection, owner=None):
		super(Land, self).__init__(name, connection, owner)


class City(Land):
	"""docstring for city"""
	def __init__(self, name, connection, nation, factory, owner=None):
		super(City, self).__init__(name, connection, owner)
		self.nation = nation
		self.factory = factory

	def buildunit(self):
		'''returns unit if factory is build and area is not occupied'''
		if self.factory.isbuild() and not self.occupied():
			return self.factory.buildunit(self.nation, self)

	def occupied(self):
		return self.owner != self.nation


class Canal(object):
	"""docstring for canal"""
	def __init__(self, name, connection, controlledby):
		super(Canal, self).__init__()
		self.name = name
		self.connection = connection
		self.controlledby = controlledby

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def controlledmovement(self):
		return self.connection

	def controlingnation(self):
		return controlledby.nation

		
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

	def activate(self):
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
		return "{} bonds of {}".format(self.share, self.nation)

	def buybond(self, player):
		self.owner = player
		self.nation.deposit(self.owner.withdraw(self.share))


class Entity(object):
	"""docstring for entity"""
	def __init__(self, name):
		super(Entity, self).__init__()
		self.name = name
		self.money = 0
	
	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def getsaldo(self):
		return self.money

	def liquidity(self, amount):
		"""returns True is amount is lower than self.money"""
		return (self.money - amount) > 0

	def withdraw(self, amount):
		'''returns True if saldo + amount > 0 and gain amount to current saldo, else False and does not gain amount to saldo'''
		self.money -= amount
		return amount

	def deposit(self, amount):
		self.money += amount



class Bank(Entity):
	"""docstring for  Bank"""
	def __init__(self, name, bonds):
		super( Bank, self).__init__(name)
		self.name = name
		self.bonds = bonds

	def liquidity(self, amount):
		"""the bank is always has liquidity"""
		return True

	def withdraw(self, amount):
		"""the bank always has more money"""
		return amount

	def deposit(self, amount):
		"""A bank will always accept money"""
		pass

	def getbonds(self, nation, owner):
		return [bond for bond in self.bonds[nation] if bond.owner == owner]

	def getbondsowners(self, nation):
		return Counter([bond.owner for bond in self.bonds[nation]]).keys()

	def getbondsperowner(self, nation):
		return {owner : sum(bond.share for bond in self.getbonds(nation, owner)) for owner in self.getbondsowners(nation)}

	def shareoptions(self, amount):
		return [bond for nation in self.bonds.keys() for bond in self.bonds[nation] if bond.share <= amount]

class Nation(Entity):
	"""
	to do:

	"""
	def __init__(self, homeareas, name):
		super(Nation, self).__init__(name)
		self.homeareas = homeareas
		self.powerlvl = 0
		self.areas = []
		self.player = None

	def numberofflags(self):
		number = 0
		for area in self.areas:
			if not isinstance(area, City):
				number += 1
		return number

	def gainpower(self, amount, winningscore):
		"""adds amount to powerlvl, capped at 25. returns True if powerlvl >= 25"""
		self.powerlvl += amount
		if self.powerlvl > 25:
			self.powerlvl = 25
		return self.powerlvl >= 25

	def getpowerfactor(self):
		return self.powerlvl/5

	# def paymentbalance(self, amount):

	# 	return {self: }





class Player(Entity):
	"""docstring for player"""
	def __init__(self, name):
		super(Player, self).__init__(name)
		self.investor = False
		self.swissbank = False
		self.controlsnation = []


class Game(object):
	"""docstring for game

	to do:
		add winningscore is setup

	"""
	def __init__(self, default=True):
		super(Game, self).__init__()
		if default:
			cg = creategame()
			self.players = cg.createplayers()
			shuffle(self.players)
			self.nations = cg.createnations()
			self.areas = cg.createareas(self.nations)
			self.units = {nation : [] for nation in self.nations}
			self.canals = cg.createcanals(areas=self.areas)
			self.winningscore = cg.winningscore
			self.tax = cg.tax
			self.bank = cg.createbank(self.nations)
			self.factorycost = 5
		else:
			print 'no none default settings implemented.'

	def __str__(self):
		return str(self.players + self.nations + self.areas)

	def getbuildfactoryoptions(self, nation):
		return [area for area in self.areas if isinstance(area, City) and area.owner == nation and not area.factory.isbuild()]

	def buildfactory(self, area):
		if area.nation.liquidity(self.factorycost):
			self.bank.deposit(area.nation.withdraw(self.factorycost))
			area.factory.activate()

	def getareas(self, nation):
		'''returns list of areas controlled by nation, including homecities'''
		# return [area for area in self.areas if area.owner == str(nation)]
		return [area for area in self.areas if area.owner == nation]

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
			if isinstance(area, City) and area.owner == nation:
				unit = area.buildunit()
				if unit != None:
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
		location = unit.location
		self.units[unit.nation].remove(unit)
		self.units[enemy.nation].remove(enemy)
		unit.kill(enemy)
		# need to implement check if current area is still owned by current nation. 
		# for example blue invades an area occupied by green and yellow and red, which is owned
		# by green. Green gets destroyed by blue. Yellow and red remain. Ownership
		# should be returned to None
		if location.owner != None and location.unitfreqnation()[location.owner] == 0 and len(location.unitfreqnation()) >= 1:
			# this wil might need an if statement for the unlikely event a battle starts without first having a claimed areas... but that should not happen right;)
			location.owner.areas.remove(location)
			location.owner = None

	def getareatype(self, type):
		return [area for area in self.areas if isinstance(area, type)]

	def claimareas(self):
		# needs to change the owner of an area, if only one nation has units in the area. 
		# Also the number of flags should not exceed 15. Cities should not count to this number.

		# loop over sea and land areas, exculde cities. An exception that occurs with 4 nations is handled in game.battle().
		for area in self.areas:
			unitfreq = area.unitfreqnation()
			if isinstance(area, City) and len(unitfreq.keys()) == 0 and area.owner != area.nation:
				# if city is no longer occupied it'll return to nation
				nation = area.nation
				self.changeclaim(area, nation)
			elif len(unitfreq.keys()) == 1 and area.owner != unitfreq.keys()[0]:
				# if only 1 nation occupies a area, it'll claim ownership
				nation = unitfreq.keys()[0]
				if nation.numberofflags() < 15:
					self.changeclaim(area, nation)

	def changeclaim(self, area, nation):
		# remove area from current owners area list
		if area.owner != None:
			area.owner.areas.remove(area)
		# only 1 nation has units in area and takes ownership of area
		area.owner = nation
		nation.areas.append(area)

	def gettax(self, nation):
		return nation.numberofflags() + 2 * len([city for city in self.getareatype(City) if not city.occupied])

	def getupkeep(self, nation):
		return len(self.units[nation])

	def getbonus(self, tax):
		if tax > 18:
			tax = 18
		return self.tax["bonus"][tax]

	def getpowerlvl(self, tax):
		if tax > 18:
			tax = 18
		return self.tax["powerlvl"][tax]

	def getpowerfactornations(self):
		return {nation:nation.getpowerfactor() for nation in self.nations}

	def investorbonus(self, player):
		"""checks if player is the investor and gives 2 million bonus if so."""
		if player.investor:
			player.deposit(self.bank.withdraw(2))

	def investoroptions(self, player):
		return self.bank.shareoptions(player.getsaldo())




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
		self.tax = defaults.tax
		self.winningscore = defaults.winningscore

	def createplayers(self):
		return [Player(name=p) for p in self.players]

	def createbonds(self, nation):
		return [Bond(share=b, interest=self.bonds[b], nation=nation) for b in self.bonds.keys()]

	def createnations(self):
		return [Nation(name=natie, homeareas=self.homecities[natie]) for natie in self.nations]

	def createbank(self, nations):
		return Bank(name='Bank', bonds={nation : self.createbonds(nation) for nation in nations})

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
					h.append(City(name=ci, connection=self.connections[ci], factory=Shipyard(build=self.navalyard[ci]), nation=nationobj, owner=nationobj))
					nationobj.areas.append(h[-1])
				if ci in self.factory.keys():
					h.append(City(name=ci, connection=self.connections[ci], factory=Armarent(build=self.factory[ci]), nation=nationobj, owner=nationobj))
					nationobj.areas.append(h[-1])
		a = l + s + h

		# making connections objects instead of strings
		for area in a:
			connectionsobj = []
			for connectto in area.connection:
				for areaobj in a:
					if str(areaobj) == connectto:
						connectionsobj.append(areaobj)
						break
			area.connection = connectionsobj
		return l + s + h

	def createcanals(self, areas):
		l = []
		for canal in self.canals.keys():
			connection = [area for area in areas if str(area) in self.canals[canal][1]]
			controlledby = [area for area in areas if str(area) in self.canals[canal][0]]
			l.append(Canal(name=canal, connection=connection, controlledby=controlledby[0]))
		return l
		# pass


if __name__ == '__main__':
	print "setting up game"
	g = Game()

	n =  20
	randomtable = [True, False, False, False, False, False, False, False, False, False]

	print "playing {} rounds".format(n)
	for i in range(n):
		print 
		print "current simulation: {}".format(i)
		print
		victory = False
		round = 0
		print "setting up game"
		g = Game()
		for player in g.players:
			player.deposit(13)
		while not victory:
			round += 1
			print
			print "round: {}".format(round)
			print
			for nation in g.nations:
				if choice(randomtable):
					print "building factory for {}".format(nation)
					choices = g.getbuildfactoryoptions(nation)
					if choices:
						g.buildfactory(choice(choices))
				print "building units for {}".format(nation)
				g.buildunits(nation)
				print "moving units for {}".format(nation)
				for fleet in g.getfleets(nation):
					pick = choice(fleet.moveoptions())
					enemies = fleet.move(pick)
					if enemies:
						enemy = choice(enemies)
						g.battle(unit=fleet, enemy=enemy)
				for army in g.getarmies(nation):
					if len(army.moveoptions() + army.conveyoptions().keys()) > 0:
						pick = choice(army.moveoptions() + army.conveyoptions().keys())
						enemies = army.move(pick)
						if enemies:
							enemy = choice(enemies)
							g.battle(unit=army, enemy=enemy)
				print "gain momvement and convoy for {}".format(nation)
				g.gainmovement(nation)
				g.gainconvey(nation)
				print "claim areas"
				g.claimareas()
				print "taxation for {}".format(nation)
				tax = g.gettax(nation)
				upkeep = g.getupkeep(nation)
				bonus = g.getbonus(tax)
				powerlvl = g.getpowerlvl(tax)
				print "tax: {}, upkeep: {}, bonus: {}, powerlvl: {}".format(tax, upkeep, bonus, powerlvl)
				nation.deposit(tax)
				g.bank.deposit(nation.withdraw(upkeep))
				g.bank.deposit(nation.withdraw(bonus))
				print "some player receives {}".format(bonus)
				print "nation saldo: {}".format(nation.getsaldo())
				victory = nation.gainpower(powerlvl, g.winningscore)
				print "{} has {} power".format(nation, nation.powerlvl)

				if victory:
					print
					for nation in g.nations:
						print "{} has powerfactor of {}".format(nation, nation.powerlvl/5)
					break
				print

			for player in g.players:
				g.investorbonus(player)
				choices = g.investoroptions(player)
				print choices
				if choices:
					pick = choice(choices)
					pick.buybond(player)
					print pick

			# get majorshareholder
			# set control to majorshareholder



