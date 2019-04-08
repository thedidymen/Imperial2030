
def createbonds(superpowers, interests, bonds):
	"""
	Returns dict {'Superpower' : {[number of bonds] : {'Owner' : ['Bank' or 'player'], 'Interest' : [amount of interest]}}}. 
	Interests and bonds should have the same length and a list with corresponding values. 
	"""
	allbonds = {}
	for sp in superpowers:
		allbonds[sp] = {bonds[index] : {'Rente' : interests[index], 'Owner' : 'Bank'} for index in range(len(interests))}
	return allbonds

def createmap(areas, homecities):
	'''
	Returns dict {'Area' : {'ConnectedTo' : [list of areas], 'ControledBy' : '['Superpower' or None]', 'HomeCountry' : '['Superpower' or none]', 
	'Tanks' : [number of tanks], 'Boats' : [number of boats]}}. Takes a dict areas: {'Area' : [list of connected areas]} and 
	dict homecities {'Superpower' : ['Area' ... ]}. In this case Areas and cities are the same, homeareas are named by the present cities.
	'''
	map = {}
	for area in areas.keys():
		for city in homecities.keys():
			if area in homecities[city]:
				hc = city
				cb = city
				break
			else:
				hc = None
				cb = None
		map[area] = {'ConnectedTo' : areas[area], 'ControledBy' : cb, 'HomeCountry' : hc, 'Tanks' : 0, 'Boats' : 0}
	return map


def printbonds():
	Superpowers = ['Russia', 'China', 'India', 'Brazil', 'USA', 'Europe']
	rentes = range(1,10)
	bond = [2, 4, 6, 9, 12, 16, 20, 25, 30]
	bonds = createbonds(superpowers=Superpowers, interests=rentes, bonds=bond)
	for sp in Superpowers:
		print
		print "{} :".format(sp)
		for numberofbond in bonds[sp].keys():
			print 'Number of bonds: \t{}\tOwner: \t{}\tInterest\t{}'.format(numberofbond, bonds[sp][numberofbond]['Owner'], bonds[sp][numberofbond]['Rente'])


def printmap():
	A = {'Canada': ['Alaska', 'Quebec', 'San Francisco', 'Chicago', 'New York', 'North Pacific', 'North Atlantic'], 'Manaus': ['Colombia', 'Peru', 'Brasillia', 'Fortaleza', 'Caribbean Sea'], 'Gulf of Guinea': ['Guinea', 'Nigeria', 'Congo', 'South-Africa', 'Indian Ocean', 'South Atlantic', 'Caribbean Sea', 'North Atlantic'], 'Paris': ['London', 'Berlin', 'Rome', 'Mediterranean Sea', 'North Atlantic'], 'Guinea': ['Gulf of Guinea', 'Nigeria', 'North-Africa', 'North Atlantic'], 'Rio de Janeiro': ['Argentina', 'South Atlantic', 'Brasillia', 'Fortaleza'], 'Fortaleza': ['Manaus', 'Brasillia', 'Caribbean Sea', 'Rio de Janeiro'], 'San Francisco': ['Canada', 'Mexico', 'North Pacific', 'Chicago', 'New Orleans'], 'Argentina': ['Peru', 'South Pacific', 'South Atlantic', 'Rio de Janeiro', 'Brasillia'], 'Australia': ['Tasman Sea'], 'Iran': ['Moscow', 'Indian Ocean', 'Near East', 'Turkey', 'Afghanistan', 'Mumbai'], 'North-Africa': ['Guinea', 'Mediterranean Sea', 'Near East', 'East-Africa', 'Nigeria', 'North Atlantic', 'Indian Ocean'], 'Chicago': ['Canada', 'San Francisco', 'New York', 'New Orleans'], 'East-Africa': ['Indian Ocean', 'Congo', 'South-Africa', 'Near East', 'North-Africa', 'Nigeria'], 'Caribbean Sea': ['Mexico', 'Gulf of Guinea', 'Manaus', 'South Atlantic', 'Fortaleza', 'New Orleans', 'Colombia', 'Manaus', 'North Atlantic', 'North Pacific'], 'Near East': ['Indian Ocean', 'Iran', 'Turkey', 'Mediterranean Sea', 'North-Africa', 'East-Africa'], 'New Delhi': ['Afghanistan', 'Urumqi', 'Kolkata', 'Mumbai'], 'Alaska': ['North Pacific', 'Canada'], 'Rome': ['Paris', 'Berlin', 'Ukraine', 'Turkey', 'Mediterranean Sea'], 'Tasman Sea': ['Australia', 'New-Zeeland', 'Indonesia', 'South Pacific', 'Indian Ocean', 'China Sea'], 'Beijing': ['China Sea', 'Mongolia', 'Urumqi', 'Chongging', 'Shanghai', 'Vladivostok', 'Korea'], 'South-Africa': ['Gulf of Guinea', 'Indian Ocean', 'Congo', 'East-Africa'], 'Mexico': ['North Pacific', 'San Francisco', 'New Orleans', 'Caribbean Sea', 'Colombia'], 'Mediterranean Sea': ['Indian Ocean', 'Paris', 'North-Africa', 'Near East', 'Rome', 'Turkey', 'North Atlantic'], 'New Orleans': ['Mexico', 'San Francisco', 'Caribbean Sea', 'Chicago', 'New York'], 'London': ['Paris', 'North Atlantic'], 'Colombia': ['Mexico', 'Manaus', 'North Pacific', 'Caribbean Sea', 'Peru'], 'Brasillia': ['Argentina', 'Manaus', 'Rio de Janeiro', 'Fortaleza', 'Peru'], 'Turkey': ['Moscow', 'Iran', 'Near East', 'Rome', 'Mediterranean Sea'], 'Afghanistan': ['Iran', 'New Delhi', 'Kazakhstan', 'Urumqi', 'Mumbai'], 'Indochina': ['Kolkata', 'Chongging', 'Shanghai', 'China Sea', 'Indian Ocean'], 'Vladivostok': ['Beijing', 'Novasibirsk', 'Sea of Japan', 'Korea', 'Mongolia'], 'North Atlantic': ['Canada', 'Quebec', 'Gulf of Guinea', 'Paris', 'Guinea', 'North-Africa', 'Caribbean Sea', 'Mediterranean Sea', 'London', 'Berlin', 'Paris', 'New York', 'Murmansk'], 'Mumbai': ['Indian Ocean', 'Iran', 'New Delhi', 'Afghanistan', 'Chennai', 'Kolkata'], 'Shanghai': ['Indochina', 'China Sea', 'Beijing', 'Chongging'], 'Mongolia': ['Beijing', 'Novasibirsk', 'Vladivostok', 'Urumqi', 'Kazakhstan'], 'Philppines': ['China Sea'], 'Peru': ['Argentina', 'Manaus', 'Brasillia', 'South Pacific', 'Colombia'], 'China Sea': ['Sea of Japan', 'North Pacific', 'South Pacific', 'Philppines', 'Indonesia', 'Korea', 'Beijing', 'Shanghai', 'Indochina', 'Indian Ocean', 'Tasman Sea'], 'Kolkata': ['Indochina', 'Indian Ocean', 'New Delhi', 'Chongging', 'Urumqi', 'Mumbai', 'Chennai'], 'Nigeria': ['Gulf of Guinea', 'Congo', 'Guinea', 'North-Africa', 'East-Africa'], 'Korea': ['China Sea', 'Beijing', 'Vladivostok', 'Sea of Japan'], 'South Pacific': ['Argentina', 'China Sea', 'Tasman Sea', 'South Atlantic', 'North Pacific', 'Peru'], 'Moscow': ['Murmansk', 'Novasibirsk', 'Kazakhstan', 'Iran', 'Turkey', 'Ukraine'], 'Berlin': ['Paris', 'Rome', 'North Atlantic', 'Ukraine', 'Murmansk'], 'New York': ['Canada', 'Quebec', 'Chicago', 'New Orleans', 'North Atlantic'], 'Kazakhstan': ['Moscow', 'Novasibirsk', 'Afghanistan', 'Mongolia', 'Urumqi'], 'Chongging': ['Indochina', 'Beijing', 'Shanghai', 'Kolkata', 'Urumqi'], 'Ukraine': ['Moscow', 'Rome', 'Berlin', 'Murmansk'], 'Murmansk': ['Moscow', 'Novasibirsk', 'Berlin', 'Ukraine', 'North Atlantic'], 'Indonesia': ['China Sea', 'Tasman Sea', 'Indian Ocean'], 'Urumqi': ['Beijing', 'New Delhi', 'Afghanistan', 'Mongolia', 'Kolkata', 'Kazakhstan', 'Chongging'], 'Chennai': ['Indian Ocean', 'Mumbai', 'Kolkata'], 'Sea of Japan': ['China Sea', 'North Pacific', 'Japan', 'Vladivostok', 'Korea'], 'North Pacific': ['Canada', 'Alaska', 'Mexico', 'China Sea', 'Sea of Japan', 'Colombia', 'San Francisco', 'South Pacific', 'Caribbean Sea'], 'New-Zeeland': ['Tasman Sea'], 'South Atlantic': ['Gulf of Guinea', 'Argentina', 'Caribbean Sea', 'Rio de Janeiro', 'Indian Ocean', 'South Pacific'], 'Indian Ocean': ['South Atlantic', 'Gulf of Guinea', 'Indochina', 'Mumbai', 'Chennai', 'Kolkata', 'Indonesia', 'Tasman Sea', 'South-Africa', 'East-Africa', 'North-Africa', 'Near East', 'Iran', 'Mediterranean Sea', 'China Sea'], 'Novasibirsk': ['Moscow', 'Murmansk', 'Vladivostok', 'Mongolia', 'Kazakhstan'], 'Congo': ['Gulf of Guinea', 'Nigeria', 'East-Africa', 'South-Africa'], 'Quebec': ['Canada', 'North Atlantic', 'New York'], 'Japan': ['Sea of Japan']}
	HomeCountry = {
		'USA' : ['San Francisco', 'New Orleans', 'New York', 'Chicago'], 
		'Europe' : ['Paris', 'London', 'Berlin, Rome'], 
		'Russia' : ['Moscow', 'Murmansk', 'Novasibirsk', 'Vladivostok'], 
		'China' : ['Urumqi', 'Beijing', 'Chongging', 'Shanghai'], 
		'India' : ['New Delhi', 'Kolkata', 'Numbai', 'Chennai'], 
		'Brazil' : ['Manaus', 'Fortaleza', 'Brasillia', 'Rio de Janeiro']}
	map = createmap(areas=A, homecities=HomeCountry)
	# for area in map.keys():
	# 	print
	# 	print area
	# 	print 'Connected to: ' + ', '.join(map[area]['ConnectedTo'])
	# 	if map[area]['ControledBy']:
	# 		print 'Controled by: {}'.format(map[area]['ControledBy'])
	# 	if map[area]['HomeCountry']:
	# 		print 'HomeCountry of: {}'.format(map[area]['HomeCountry'])
	# 	print 'Tanks : {}'.format(map[area]['Tanks'])
	# 	print 'Boats : {}'.format(map[area]['Boats'])

	string = '{:10}\t{:10}\t{:10}\t{:5}\t{:5}\t{:20}\n'.format('Area', 'Controlled By', 'Home City', 'Tanks', 'Boats', 'Connected to')
	for area in map.keys():
		string += '{:10}\t{:10}\t{:10}\t{:5}\t{:5}\t{:20}\n'.format(area, map[area]['ControledBy'], map[area]['HomeCountry'], map[area]['Tanks'], map[area]['Boats'], map[area]['ConnectedTo'])
	print string

if __name__ == '__main__':
	printbonds()
	printmap()


	