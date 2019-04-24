
class CreateGame(object):
	"""docstring for CreateGame"""
	def __init__(self, superpowers=None, interests=None, bonds=None, areas=None, homecities=None, naval=None, army=None, players=None):
		super(CreateGame, self).__init__()
		if superpowers == None:
			self.superpowers = ['Russia', 'China', 'India', 'Brazil', 'USA', 'Europe']
		else:
			self.superpowers = superpowers

		if interests == None:
			self.interests = range(1,10)
		else:
			self.interests = interests

		if bonds == None:
			self.bonds = [2, 4, 6, 9, 12, 16, 20, 25, 30]
		else:
			self.bonds = bonds

		if areas == None:
			self.areas = {'Canada': ['Alaska', 'Quebec', 'San Francisco', 'Chicago', 'New York', 'North Pacific', 'North Atlantic'], 'Manaus': ['Colombia', 'Peru', 'Brasillia', 'Fortaleza', 'Caribbean Sea'], 'Gulf of Guinea': ['Guinea', 'Nigeria', 'Congo', 'South-Africa', 'Indian Ocean', 'South Atlantic', 'Caribbean Sea', 'North Atlantic'], 'Paris': ['London', 'Berlin', 'Rome', 'Mediterranean Sea', 'North Atlantic'], 'Guinea': ['Gulf of Guinea', 'Nigeria', 'North-Africa', 'North Atlantic'], 'Rio de Janeiro': ['Argentina', 'South Atlantic', 'Brasillia', 'Fortaleza'], 'Fortaleza': ['Manaus', 'Brasillia', 'Caribbean Sea', 'Rio de Janeiro'], 'San Francisco': ['Canada', 'Mexico', 'North Pacific', 'Chicago', 'New Orleans'], 'Argentina': ['Peru', 'South Pacific', 'South Atlantic', 'Rio de Janeiro', 'Brasillia'], 'Australia': ['Tasman Sea'], 'Iran': ['Moscow', 'Indian Ocean', 'Near East', 'Turkey', 'Afghanistan', 'Mumbai'], 'North-Africa': ['Guinea', 'Mediterranean Sea', 'Near East', 'East-Africa', 'Nigeria', 'North Atlantic', 'Indian Ocean'], 'Chicago': ['Canada', 'San Francisco', 'New York', 'New Orleans'], 'East-Africa': ['Indian Ocean', 'Congo', 'South-Africa', 'Near East', 'North-Africa', 'Nigeria'], 'Caribbean Sea': ['Mexico', 'Gulf of Guinea', 'Manaus', 'South Atlantic', 'Fortaleza', 'New Orleans', 'Colombia', 'Manaus', 'North Atlantic', 'North Pacific'], 'Near East': ['Indian Ocean', 'Iran', 'Turkey', 'Mediterranean Sea', 'North-Africa', 'East-Africa'], 'New Delhi': ['Afghanistan', 'Urumqi', 'Kolkata', 'Mumbai'], 'Alaska': ['North Pacific', 'Canada'], 'Rome': ['Paris', 'Berlin', 'Ukraine', 'Turkey', 'Mediterranean Sea'], 'Tasman Sea': ['Australia', 'New-Zeeland', 'Indonesia', 'South Pacific', 'Indian Ocean', 'China Sea'], 'Beijing': ['China Sea', 'Mongolia', 'Urumqi', 'Chongging', 'Shanghai', 'Vladivostok', 'Korea'], 'South-Africa': ['Gulf of Guinea', 'Indian Ocean', 'Congo', 'East-Africa'], 'Mexico': ['North Pacific', 'San Francisco', 'New Orleans', 'Caribbean Sea', 'Colombia'], 'Mediterranean Sea': ['Indian Ocean', 'Paris', 'North-Africa', 'Near East', 'Rome', 'Turkey', 'North Atlantic'], 'New Orleans': ['Mexico', 'San Francisco', 'Caribbean Sea', 'Chicago', 'New York'], 'London': ['Paris', 'North Atlantic'], 'Colombia': ['Mexico', 'Manaus', 'North Pacific', 'Caribbean Sea', 'Peru'], 'Brasillia': ['Argentina', 'Manaus', 'Rio de Janeiro', 'Fortaleza', 'Peru'], 'Turkey': ['Moscow', 'Iran', 'Near East', 'Rome', 'Mediterranean Sea'], 'Afghanistan': ['Iran', 'New Delhi', 'Kazakhstan', 'Urumqi', 'Mumbai'], 'Indochina': ['Kolkata', 'Chongging', 'Shanghai', 'China Sea', 'Indian Ocean'], 'Vladivostok': ['Beijing', 'Novasibirsk', 'Sea of Japan', 'Korea', 'Mongolia'], 'North Atlantic': ['Canada', 'Quebec', 'Gulf of Guinea', 'Paris', 'Guinea', 'North-Africa', 'Caribbean Sea', 'Mediterranean Sea', 'London', 'Berlin', 'Paris', 'New York', 'Murmansk'], 'Mumbai': ['Indian Ocean', 'Iran', 'New Delhi', 'Afghanistan', 'Chennai', 'Kolkata'], 'Shanghai': ['Indochina', 'China Sea', 'Beijing', 'Chongging'], 'Mongolia': ['Beijing', 'Novasibirsk', 'Vladivostok', 'Urumqi', 'Kazakhstan'], 'Philppines': ['China Sea'], 'Peru': ['Argentina', 'Manaus', 'Brasillia', 'South Pacific', 'Colombia'], 'China Sea': ['Sea of Japan', 'North Pacific', 'South Pacific', 'Philppines', 'Indonesia', 'Korea', 'Beijing', 'Shanghai', 'Indochina', 'Indian Ocean', 'Tasman Sea'], 'Kolkata': ['Indochina', 'Indian Ocean', 'New Delhi', 'Chongging', 'Urumqi', 'Mumbai', 'Chennai'], 'Nigeria': ['Gulf of Guinea', 'Congo', 'Guinea', 'North-Africa', 'East-Africa'], 'Korea': ['China Sea', 'Beijing', 'Vladivostok', 'Sea of Japan'], 'South Pacific': ['Argentina', 'China Sea', 'Tasman Sea', 'South Atlantic', 'North Pacific', 'Peru'], 'Moscow': ['Murmansk', 'Novasibirsk', 'Kazakhstan', 'Iran', 'Turkey', 'Ukraine'], 'Berlin': ['Paris', 'Rome', 'North Atlantic', 'Ukraine', 'Murmansk'], 'New York': ['Canada', 'Quebec', 'Chicago', 'New Orleans', 'North Atlantic'], 'Kazakhstan': ['Moscow', 'Novasibirsk', 'Afghanistan', 'Mongolia', 'Urumqi'], 'Chongging': ['Indochina', 'Beijing', 'Shanghai', 'Kolkata', 'Urumqi'], 'Ukraine': ['Moscow', 'Rome', 'Berlin', 'Murmansk'], 'Murmansk': ['Moscow', 'Novasibirsk', 'Berlin', 'Ukraine', 'North Atlantic'], 'Indonesia': ['China Sea', 'Tasman Sea', 'Indian Ocean'], 'Urumqi': ['Beijing', 'New Delhi', 'Afghanistan', 'Mongolia', 'Kolkata', 'Kazakhstan', 'Chongging'], 'Chennai': ['Indian Ocean', 'Mumbai', 'Kolkata'], 'Sea of Japan': ['China Sea', 'North Pacific', 'Japan', 'Vladivostok', 'Korea'], 'North Pacific': ['Canada', 'Alaska', 'Mexico', 'China Sea', 'Sea of Japan', 'Colombia', 'San Francisco', 'South Pacific', 'Caribbean Sea'], 'New-Zeeland': ['Tasman Sea'], 'South Atlantic': ['Gulf of Guinea', 'Argentina', 'Caribbean Sea', 'Rio de Janeiro', 'Indian Ocean', 'South Pacific'], 'Indian Ocean': ['South Atlantic', 'Gulf of Guinea', 'Indochina', 'Mumbai', 'Chennai', 'Kolkata', 'Indonesia', 'Tasman Sea', 'South-Africa', 'East-Africa', 'North-Africa', 'Near East', 'Iran', 'Mediterranean Sea', 'China Sea'], 'Novasibirsk': ['Moscow', 'Murmansk', 'Vladivostok', 'Mongolia', 'Kazakhstan'], 'Congo': ['Gulf of Guinea', 'Nigeria', 'East-Africa', 'South-Africa'], 'Quebec': ['Canada', 'North Atlantic', 'New York'], 'Japan': ['Sea of Japan']}
		else:
			self.areas = areas

		if homecities == None:
			self.homecities = {
			'USA' : ['San Francisco', 'New Orleans', 'New York', 'Chicago'], 
			'Europe' : ['Paris', 'London', 'Berlin', 'Rome'], 
			'Russia' : ['Moscow', 'Murmansk', 'Novasibirsk', 'Vladivostok'], 
			'China' : ['Urumqi', 'Beijing', 'Chongging', 'Shanghai'], 
			'India' : ['New Delhi', 'Kolkata', 'Numbai', 'Chennai'], 
			'Brazil' : ['Manaus', 'Fortaleza', 'Brasillia', 'Rio de Janeiro']}
		else:
			self.homecities = homecities

		if naval == None:
			self.naval = {'San Francisco' : False, 'New Orleans' : True, 'New York' : False, 'Fortaleza' : False, 'Rio de Janeiro' : True, 'London' : True, 'Rome' : False, 'Murmansk' : False, 'Vladivostok' : True, 'Shanghai' : True, 'Kolkata' : False, 'Mumbai' : True}
		else:
			self.naval = naval

		if army == None:
			self.army = {'Chicago' : True, 'Manaus' : False, 'Brasillia' : True, 'Paris' : True, 'Berlin' : False, 'Moscow' : True, 'Novasibirsk' : False, 'Urumqi' : False, 'Chongging' : False, 'Beijing' : True, 'New Delhi' : True, 'Chennai' : False}
		else:
			self.army = army

		if players == None:
			self.players = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6']
		else:
			self.players = players

	def nationorder(self):
		return self.superpowers


	def createbonds(self):
		"""
		Returns dict {'Superpower' : {[number of bonds] : {'Owner' : ['Bank' or 'player'], 'Interest' : [amount of interest]}}}. 
		Interests and bonds should have the same length and a list with corresponding values. 
		"""
		allbonds = {}
		for sp in self.superpowers:
			allbonds[sp] = {self.bonds[index] : {'Rente' : self.interests[index], 'Owner' : 'Bank'} for index in range(len(self.interests))}
		return allbonds

	def createmap(self):
		'''
		Returns dict {'Area' : {'ConnectedTo' : [list of areas], 'ControledBy' : '['Superpower' or None]', 'HomeCountry' : '['Superpower' or none]', 
		'Tanks' : [number of tanks], 'Boats' : [number of boats]}}. Takes a dict areas: {'Area' : [list of connected areas]} and 
		dict homecities {'Superpower' : ['Area' ... ]}. In this case Areas and cities are the same, homeareas are named by the present cities.
		'''
		map = {}
		for area in self.areas.keys():
			for city in self.homecities.keys():
				if area in self.homecities[city]:
					hc = city
					cb = city
					break
				else:
					hc = None
					cb = None
			map[area] = {'ConnectedTo' : self.areas[area], 'ControledBy' : cb, 'HomeCountry' : hc, 'Tanks' : {superpower : 0 for superpower in self.superpowers}, 'Boats' : {superpower : 0 for superpower in self.superpowers}}
		return map


	def createsuperpowers(self):
		'''
		Returns dict {'Money' : [amount of money], 'Powerlevel' : [0-25], 'Controls' : [list of areas], 'ControledBy' : '[Player]', 
		'Cities' : {'Factory' : [True/False], 'Navalbase' : [True/False], 'Build' : [True/False]}}. Takes dict homecities {'Superpower' : ['Area' ... ]}, 
		dict naval {Area : [True/False]}, dict army {Area : [True/False]}, in which in the areas it's possilbe to build an naval or army factory 
		and True or False wheter it's build.
		'''
		nations = {}
		for sp in self.superpowers:
			cities = {}
			for city in self.homecities[sp]:
				factory = city in self.army.keys()
				navalb = city in self.naval.keys()
				if city in self.army.keys():
					build = self.army[city]
				elif city in self.naval.keys():
					build = self.naval[city]
				else:
					build = False
				cities[city] = {'Factory' : factory, 'Navalbase' : navalb, 'Build' : build}
			nations[sp] = {'Money' : 0, 'Powerlevel' : 0, 'Controls' : [], 'ControledBy' : '', 'Cities' : cities}
		return nations

	def createplayers(self):
		p = {}
		for player in self.players:
			p[player] = {'Money' : 0, 'Investor' : False, 'ControlsSuperpower' : []}
		return p

	def printplayers(self):
		p = self.createplayers()
		string = '{:10}\t{}\t{}\t{}\t\n'.format('Player', 'Money', 'Investor', 'Biggest shareholder')
		for player in p.keys():
			string += '{:10}\t{}\t{}\t{}\t\n'.format(player, p[player]['Money'], p[player]['Investor'], ', '.join(sp for sp in p[player]['ControlsSuperpower']))
		print string


	def printbonds(self):
		bonds = self.createbonds()
		for sp in self.superpowers:
			print
			print "{} :".format(sp)
			for numberofbond in bonds[sp].keys():
				print 'Number of bonds: \t{}\tOwner: \t{}\tInterest\t{}'.format(numberofbond, bonds[sp][numberofbond]['Owner'], bonds[sp][numberofbond]['Rente'])


	def printmap(self):
		map = self.createmap()
		string = '{:10}\t{:10}\t{:10}\t{:5}\t{:5}\t{:20}\n'.format('Area', 'Controlled By', 'Home City', 'Tanks', 'Boats', 'Connected to')
		for area in map.keys():
			string += '{:10}\t{:10}\t{:10}\t{:5}\t{:5}\t{:20}\n'.format(area, map[area]['ControledBy'], map[area]['HomeCountry'], map[area]['Tanks'], map[area]['Boats'], ', '.join(connection for connection in map[area]['ConnectedTo']))
		print string

	def printsuperpowers(self):
		Superpowers = self.createsuperpowers()
		string = '{:<10}\t{:<10}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\n'.format('Superpower', 'City', 'Factory', 'Naval', 'Build', 'Money', 'Powerlevel', 'Controled by', 'Controls')
		for sp in Superpowers.keys():
			for city in Superpowers[sp]['Cities'].keys():
				string += '{:<10}\t{:<10}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\n'.format(sp, city, Superpowers[sp]['Cities'][city]['Factory'], Superpowers[sp]['Cities'][city]['Navalbase'], Superpowers[sp]['Cities'][city]['Build'], Superpowers[sp]['Money'], Superpowers[sp]['Powerlevel'], Superpowers[sp]['ControledBy'], Superpowers[sp]['Controls'])
		print string



if __name__ == '__main__':
	create = CreateGame()
	create.printbonds()
	print
	create.printmap()
	print
	create.printsuperpowers()
	print
	create.printplayers()
	print

	