	# Superpowers : [
	# 	Superpower: {
	# 		Money : 0,
	# 		Cities : {
	# 			City : {
	# 				Factory : False,
	# 				NavalBase : False,
	# 				Build : False
	# 				}
	# 			}
	# 		Powerlvl : 0,
	# 		OwnsArea : [],
	# 		ControledBy : Player
	# 		}
	# 	],




def createsuperpowers():
	naval = {'San Francisco' : False, 'New Orleans' : True, 'New York' : False, 'Fortaleza' : False, 'Rio de Janeiro' : True, 'London' : True, 'Rome' : False, 'Murmansk' : False, 'Vladivostok' : True, 'Shanghai' : True, 'Kolkata' : False, 'Mumbai' : True}
	army = {'Chicago' : True, 'Manaus' : False, 'Brasillia' : True, 'Paris' : True, 'Berlin' : False, 'Moscow' : True, 'Novasibirsk' : False, 'Urumqi' : False, 'Chongging' : False, 'Beijing' : True, 'New Delhi' : True, 'Chennai' : False}
	superpowers = ['Russia', 'China', 'India', 'Brazil', 'USA', 'Europe']
	HomeCities = {
		'USA' : ['San Francisco', 'New Orleans', 'New York', 'Chicago'], 
		'Europe' : ['Paris', 'London', 'Berlin', 'Rome'], 
		'Russia' : ['Moscow', 'Murmansk', 'Novasibirsk', 'Vladivostok'], 
		'China' : ['Urumqi', 'Beijing', 'Chongging', 'Shanghai'], 
		'India' : ['New Delhi', 'Kolkata', 'Numbai', 'Chennai'], 
		'Brazil' : ['Manaus', 'Fortaleza', 'Brasillia', 'Rio de Janeiro']}
	rentes = range(1,10)
	bonds = [2, 4, 6, 9, 12, 16, 20, 25, 30]
	A = {'Canada': ['Alaska', 'Quebec', 'San Francisco', 'Chicago', 'New York', 'North Pacific', 'North Atlantic'], 'Manaus': ['Colombia', 'Peru', 'Brasillia', 'Fortaleza', 'Caribbean Sea'], 'Gulf of Guinea': ['Guinea', 'Nigeria', 'Congo', 'South-Africa', 'Indian Ocean', 'South Atlantic', 'Caribbean Sea', 'North Atlantic'], 'Paris': ['London', 'Berlin', 'Rome', 'Mediterranean Sea', 'North Atlantic'], 'Guinea': ['Gulf of Guinea', 'Nigeria', 'North-Africa', 'North Atlantic'], 'Rio de Janeiro': ['Argentina', 'South Atlantic', 'Brasillia', 'Fortaleza'], 'Fortaleza': ['Manaus', 'Brasillia', 'Caribbean Sea', 'Rio de Janeiro'], 'San Francisco': ['Canada', 'Mexico', 'North Pacific', 'Chicago', 'New Orleans'], 'Argentina': ['Peru', 'South Pacific', 'South Atlantic', 'Rio de Janeiro', 'Brasillia'], 'Australia': ['Tasman Sea'], 'Iran': ['Moscow', 'Indian Ocean', 'Near East', 'Turkey', 'Afghanistan', 'Mumbai'], 'North-Africa': ['Guinea', 'Mediterranean Sea', 'Near East', 'East-Africa', 'Nigeria', 'North Atlantic', 'Indian Ocean'], 'Chicago': ['Canada', 'San Francisco', 'New York', 'New Orleans'], 'East-Africa': ['Indian Ocean', 'Congo', 'South-Africa', 'Near East', 'North-Africa', 'Nigeria'], 'Caribbean Sea': ['Mexico', 'Gulf of Guinea', 'Manaus', 'South Atlantic', 'Fortaleza', 'New Orleans', 'Colombia', 'Manaus', 'North Atlantic', 'North Pacific'], 'Near East': ['Indian Ocean', 'Iran', 'Turkey', 'Mediterranean Sea', 'North-Africa', 'East-Africa'], 'New Delhi': ['Afghanistan', 'Urumqi', 'Kolkata', 'Mumbai'], 'Alaska': ['North Pacific', 'Canada'], 'Rome': ['Paris', 'Berlin', 'Ukraine', 'Turkey', 'Mediterranean Sea'], 'Tasman Sea': ['Australia', 'New-Zeeland', 'Indonesia', 'South Pacific', 'Indian Ocean', 'China Sea'], 'Beijing': ['China Sea', 'Mongolia', 'Urumqi', 'Chongging', 'Shanghai', 'Vladivostok', 'Korea'], 'South-Africa': ['Gulf of Guinea', 'Indian Ocean', 'Congo', 'East-Africa'], 'Mexico': ['North Pacific', 'San Francisco', 'New Orleans', 'Caribbean Sea', 'Colombia'], 'Mediterranean Sea': ['Indian Ocean', 'Paris', 'North-Africa', 'Near East', 'Rome', 'Turkey', 'North Atlantic'], 'New Orleans': ['Mexico', 'San Francisco', 'Caribbean Sea', 'Chicago', 'New York'], 'London': ['Paris', 'North Atlantic'], 'Colombia': ['Mexico', 'Manaus', 'North Pacific', 'Caribbean Sea', 'Peru'], 'Brasillia': ['Argentina', 'Manaus', 'Rio de Janeiro', 'Fortaleza', 'Peru'], 'Turkey': ['Moscow', 'Iran', 'Near East', 'Rome', 'Mediterranean Sea'], 'Afghanistan': ['Iran', 'New Delhi', 'Kazakhstan', 'Urumqi', 'Mumbai'], 'Indochina': ['Kolkata', 'Chongging', 'Shanghai', 'China Sea', 'Indian Ocean'], 'Vladivostok': ['Beijing', 'Novasibirsk', 'Sea of Japan', 'Korea', 'Mongolia'], 'North Atlantic': ['Canada', 'Quebec', 'Gulf of Guinea', 'Paris', 'Guinea', 'North-Africa', 'Caribbean Sea', 'Mediterranean Sea', 'London', 'Berlin', 'Paris', 'New York', 'Murmansk'], 'Mumbai': ['Indian Ocean', 'Iran', 'New Delhi', 'Afghanistan', 'Chennai', 'Kolkata'], 'Shanghai': ['Indochina', 'China Sea', 'Beijing', 'Chongging'], 'Mongolia': ['Beijing', 'Novasibirsk', 'Vladivostok', 'Urumqi', 'Kazakhstan'], 'Philppines': ['China Sea'], 'Peru': ['Argentina', 'Manaus', 'Brasillia', 'South Pacific', 'Colombia'], 'China Sea': ['Sea of Japan', 'North Pacific', 'South Pacific', 'Philppines', 'Indonesia', 'Korea', 'Beijing', 'Shanghai', 'Indochina', 'Indian Ocean', 'Tasman Sea'], 'Kolkata': ['Indochina', 'Indian Ocean', 'New Delhi', 'Chongging', 'Urumqi', 'Mumbai', 'Chennai'], 'Nigeria': ['Gulf of Guinea', 'Congo', 'Guinea', 'North-Africa', 'East-Africa'], 'Korea': ['China Sea', 'Beijing', 'Vladivostok', 'Sea of Japan'], 'South Pacific': ['Argentina', 'China Sea', 'Tasman Sea', 'South Atlantic', 'North Pacific', 'Peru'], 'Moscow': ['Murmansk', 'Novasibirsk', 'Kazakhstan', 'Iran', 'Turkey', 'Ukraine'], 'Berlin': ['Paris', 'Rome', 'North Atlantic', 'Ukraine', 'Murmansk'], 'New York': ['Canada', 'Quebec', 'Chicago', 'New Orleans', 'North Atlantic'], 'Kazakhstan': ['Moscow', 'Novasibirsk', 'Afghanistan', 'Mongolia', 'Urumqi'], 'Chongging': ['Indochina', 'Beijing', 'Shanghai', 'Kolkata', 'Urumqi'], 'Ukraine': ['Moscow', 'Rome', 'Berlin', 'Murmansk'], 'Murmansk': ['Moscow', 'Novasibirsk', 'Berlin', 'Ukraine', 'North Atlantic'], 'Indonesia': ['China Sea', 'Tasman Sea', 'Indian Ocean'], 'Urumqi': ['Beijing', 'New Delhi', 'Afghanistan', 'Mongolia', 'Kolkata', 'Kazakhstan', 'Chongging'], 'Chennai': ['Indian Ocean', 'Mumbai', 'Kolkata'], 'Sea of Japan': ['China Sea', 'North Pacific', 'Japan', 'Vladivostok', 'Korea'], 'North Pacific': ['Canada', 'Alaska', 'Mexico', 'China Sea', 'Sea of Japan', 'Colombia', 'San Francisco', 'South Pacific', 'Caribbean Sea'], 'New-Zeeland': ['Tasman Sea'], 'South Atlantic': ['Gulf of Guinea', 'Argentina', 'Caribbean Sea', 'Rio de Janeiro', 'Indian Ocean', 'South Pacific'], 'Indian Ocean': ['South Atlantic', 'Gulf of Guinea', 'Indochina', 'Mumbai', 'Chennai', 'Kolkata', 'Indonesia', 'Tasman Sea', 'South-Africa', 'East-Africa', 'North-Africa', 'Near East', 'Iran', 'Mediterranean Sea', 'China Sea'], 'Novasibirsk': ['Moscow', 'Murmansk', 'Vladivostok', 'Mongolia', 'Kazakhstan'], 'Congo': ['Gulf of Guinea', 'Nigeria', 'East-Africa', 'South-Africa'], 'Quebec': ['Canada', 'North Atlantic', 'New York'], 'Japan': ['Sea of Japan']}


	Superpowers = {}
	for sp in HomeCities.keys():
		cities = {}
		for city in HomeCities[sp]:
			factory = city in army.keys()
			navalb = city in naval.keys()
			if factory or navalb:
				build = True
			else:
				build = False
			cities[city] = {'Factory' : factory, 'Navalbase' : navalb, 'Build' : build}
		Superpowers[sp] = {'Money' : 0, 'Powerlevel' : 0, 'Controls' : [], 'ControledBy' : '', 'Cities' : cities}

	string = '{:<10}\t{:<10}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\n'.format('Superpower', 'City', 'Factory', 'Naval', 'Build', 'Money', 'Powerlevel', 'Controled by', 'Controls')
	for sp in Superpowers.keys():
		for city in Superpowers[sp]['Cities'].keys():
			string += '{:<10}\t{:<10}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\t{:^7}\n'.format(sp, city, Superpowers[sp]['Cities'][city]['Factory'], Superpowers[sp]['Cities'][city]['Navalbase'], Superpowers[sp]['Cities'][city]['Build'], Superpowers[sp]['Money'], Superpowers[sp]['Powerlevel'], Superpowers[sp]['ControledBy'], Superpowers[sp]['Controls'])
	print string








def Areas():
	superpowers = ['Russia', 'China', 'India', 'Brazil', 'USA', 'Europe']
	HomeCountry = {
		'USA' : ['San Francisco', 'New Orleans', 'New York', 'Chicago'], 
		'Europe' : ['Paris', 'London', 'Berlin', 'Rome'], 
		'Russia' : ['Moscow', 'Murmansk', 'Novasibirsk', 'Vladivostok'], 
		'China' : ['Urumqi', 'Beijing', 'Chongging', 'Shanghai'], 
		'India' : ['New Delhi', 'Kolkata', 'Numbai', 'Chennai'], 
		'Brazil' : ['Manaus', 'Fortaleza', 'Brasillia', 'Rio de Janeiro']}
	rentes = range(1,10)
	bonds = [2, 4, 6, 9, 12, 16, 20, 25, 30]
	A = {'Canada': ['Alaska', 'Quebec', 'San Francisco', 'Chicago', 'New York', 'North Pacific', 'North Atlantic'], 'Manaus': ['Colombia', 'Peru', 'Brasillia', 'Fortaleza', 'Caribbean Sea'], 'Gulf of Guinea': ['Guinea', 'Nigeria', 'Congo', 'South-Africa', 'Indian Ocean', 'South Atlantic', 'Caribbean Sea', 'North Atlantic'], 'Paris': ['London', 'Berlin', 'Rome', 'Mediterranean Sea', 'North Atlantic'], 'Guinea': ['Gulf of Guinea', 'Nigeria', 'North-Africa', 'North Atlantic'], 'Rio de Janeiro': ['Argentina', 'South Atlantic', 'Brasillia', 'Fortaleza'], 'Fortaleza': ['Manaus', 'Brasillia', 'Caribbean Sea', 'Rio de Janeiro'], 'San Francisco': ['Canada', 'Mexico', 'North Pacific', 'Chicago', 'New Orleans'], 'Argentina': ['Peru', 'South Pacific', 'South Atlantic', 'Rio de Janeiro', 'Brasillia'], 'Australia': ['Tasman Sea'], 'Iran': ['Moscow', 'Indian Ocean', 'Near East', 'Turkey', 'Afghanistan', 'Mumbai'], 'North-Africa': ['Guinea', 'Mediterranean Sea', 'Near East', 'East-Africa', 'Nigeria', 'North Atlantic', 'Indian Ocean'], 'Chicago': ['Canada', 'San Francisco', 'New York', 'New Orleans'], 'East-Africa': ['Indian Ocean', 'Congo', 'South-Africa', 'Near East', 'North-Africa', 'Nigeria'], 'Caribbean Sea': ['Mexico', 'Gulf of Guinea', 'Manaus', 'South Atlantic', 'Fortaleza', 'New Orleans', 'Colombia', 'Manaus', 'North Atlantic', 'North Pacific'], 'Near East': ['Indian Ocean', 'Iran', 'Turkey', 'Mediterranean Sea', 'North-Africa', 'East-Africa'], 'New Delhi': ['Afghanistan', 'Urumqi', 'Kolkata', 'Mumbai'], 'Alaska': ['North Pacific', 'Canada'], 'Rome': ['Paris', 'Berlin', 'Ukraine', 'Turkey', 'Mediterranean Sea'], 'Tasman Sea': ['Australia', 'New-Zeeland', 'Indonesia', 'South Pacific', 'Indian Ocean', 'China Sea'], 'Beijing': ['China Sea', 'Mongolia', 'Urumqi', 'Chongging', 'Shanghai', 'Vladivostok', 'Korea'], 'South-Africa': ['Gulf of Guinea', 'Indian Ocean', 'Congo', 'East-Africa'], 'Mexico': ['North Pacific', 'San Francisco', 'New Orleans', 'Caribbean Sea', 'Colombia'], 'Mediterranean Sea': ['Indian Ocean', 'Paris', 'North-Africa', 'Near East', 'Rome', 'Turkey', 'North Atlantic'], 'New Orleans': ['Mexico', 'San Francisco', 'Caribbean Sea', 'Chicago', 'New York'], 'London': ['Paris', 'North Atlantic'], 'Colombia': ['Mexico', 'Manaus', 'North Pacific', 'Caribbean Sea', 'Peru'], 'Brasillia': ['Argentina', 'Manaus', 'Rio de Janeiro', 'Fortaleza', 'Peru'], 'Turkey': ['Moscow', 'Iran', 'Near East', 'Rome', 'Mediterranean Sea'], 'Afghanistan': ['Iran', 'New Delhi', 'Kazakhstan', 'Urumqi', 'Mumbai'], 'Indochina': ['Kolkata', 'Chongging', 'Shanghai', 'China Sea', 'Indian Ocean'], 'Vladivostok': ['Beijing', 'Novasibirsk', 'Sea of Japan', 'Korea', 'Mongolia'], 'North Atlantic': ['Canada', 'Quebec', 'Gulf of Guinea', 'Paris', 'Guinea', 'North-Africa', 'Caribbean Sea', 'Mediterranean Sea', 'London', 'Berlin', 'Paris', 'New York', 'Murmansk'], 'Mumbai': ['Indian Ocean', 'Iran', 'New Delhi', 'Afghanistan', 'Chennai', 'Kolkata'], 'Shanghai': ['Indochina', 'China Sea', 'Beijing', 'Chongging'], 'Mongolia': ['Beijing', 'Novasibirsk', 'Vladivostok', 'Urumqi', 'Kazakhstan'], 'Philppines': ['China Sea'], 'Peru': ['Argentina', 'Manaus', 'Brasillia', 'South Pacific', 'Colombia'], 'China Sea': ['Sea of Japan', 'North Pacific', 'South Pacific', 'Philppines', 'Indonesia', 'Korea', 'Beijing', 'Shanghai', 'Indochina', 'Indian Ocean', 'Tasman Sea'], 'Kolkata': ['Indochina', 'Indian Ocean', 'New Delhi', 'Chongging', 'Urumqi', 'Mumbai', 'Chennai'], 'Nigeria': ['Gulf of Guinea', 'Congo', 'Guinea', 'North-Africa', 'East-Africa'], 'Korea': ['China Sea', 'Beijing', 'Vladivostok', 'Sea of Japan'], 'South Pacific': ['Argentina', 'China Sea', 'Tasman Sea', 'South Atlantic', 'North Pacific', 'Peru'], 'Moscow': ['Murmansk', 'Novasibirsk', 'Kazakhstan', 'Iran', 'Turkey', 'Ukraine'], 'Berlin': ['Paris', 'Rome', 'North Atlantic', 'Ukraine', 'Murmansk'], 'New York': ['Canada', 'Quebec', 'Chicago', 'New Orleans', 'North Atlantic'], 'Kazakhstan': ['Moscow', 'Novasibirsk', 'Afghanistan', 'Mongolia', 'Urumqi'], 'Chongging': ['Indochina', 'Beijing', 'Shanghai', 'Kolkata', 'Urumqi'], 'Ukraine': ['Moscow', 'Rome', 'Berlin', 'Murmansk'], 'Murmansk': ['Moscow', 'Novasibirsk', 'Berlin', 'Ukraine', 'North Atlantic'], 'Indonesia': ['China Sea', 'Tasman Sea', 'Indian Ocean'], 'Urumqi': ['Beijing', 'New Delhi', 'Afghanistan', 'Mongolia', 'Kolkata', 'Kazakhstan', 'Chongging'], 'Chennai': ['Indian Ocean', 'Mumbai', 'Kolkata'], 'Sea of Japan': ['China Sea', 'North Pacific', 'Japan', 'Vladivostok', 'Korea'], 'North Pacific': ['Canada', 'Alaska', 'Mexico', 'China Sea', 'Sea of Japan', 'Colombia', 'San Francisco', 'South Pacific', 'Caribbean Sea'], 'New-Zeeland': ['Tasman Sea'], 'South Atlantic': ['Gulf of Guinea', 'Argentina', 'Caribbean Sea', 'Rio de Janeiro', 'Indian Ocean', 'South Pacific'], 'Indian Ocean': ['South Atlantic', 'Gulf of Guinea', 'Indochina', 'Mumbai', 'Chennai', 'Kolkata', 'Indonesia', 'Tasman Sea', 'South-Africa', 'East-Africa', 'North-Africa', 'Near East', 'Iran', 'Mediterranean Sea', 'China Sea'], 'Novasibirsk': ['Moscow', 'Murmansk', 'Vladivostok', 'Mongolia', 'Kazakhstan'], 'Congo': ['Gulf of Guinea', 'Nigeria', 'East-Africa', 'South-Africa'], 'Quebec': ['Canada', 'North Atlantic', 'New York'], 'Japan': ['Sea of Japan']}

	areas = {}
	for area in A.keys():
		for country in HomeCountry.keys():
			if area in HomeCountry[country]:
				hc = country
				cb = country
				break
			else:
				hc = None
				cb = None
		areas[area] = {'ConnectedTo' : A[area], 'ControledBy' : cb, 'HomeCountry' : hc, 'Tanks' : 0, 'Boats' : 0}

	for area in areas.keys():
		print
		print area
		print 'Connected to: ' + ', '.join(areas[area]['ConnectedTo'])
		if areas[area]['ControledBy']:
			print 'Controled by: {}'.format(areas[area]['ControledBy'])
		if areas[area]['HomeCountry']:
			print 'HomeCountry of: {}'.format(areas[area]['HomeCountry'])
		print 'Tanks : {}'.format(areas[area]['Tanks'])
		print 'Boats : {}'.format(areas[area]['Boats'])

	# for area in areas.keys():
	# 	for country in HomeCountry:
	# 		if area in HomeCountry[country]:
	# 			print 'Connected to: ' + ', '.join(areas[area]['ConnectedTo'])
	# 			if areas[area]['ControledBy']:
	# 				print 'Controled by: {}'.format(areas[area]['ControledBy'])
	# 			if areas[area]['HomeCountry']:
	# 				print 'HomeCountry of: {}'.format(areas[area]['HomeCountry'])
	# 			print 'Tanks : {}'.format(areas[area]['Tanks'])
	# 			print 'Boats : {}'.format(areas[area]['Boats'])








def bonds():
	Superpowers = ['Russia', 'China', 'India', 'Brazil', 'USA', 'Europe']
	rentes = range(1,10)
	bonds = [2, 4, 6, 9, 12, 16, 20, 25, 30]

	# Bonds = {16: {'Rente': 6, 'Bonds': 16}, 2: {'Rente': 1, 'Bonds': 2}, 4: {'Rente': 2, 'Bonds': 4}, 30: {'Rente': 9, 'Bonds': 30}, 6: {'Rente': 3, 'Bonds': 6}, 25: {'Rente': 8, 'Bonds': 25}, 9: {'Rente': 4, 'Bonds': 9}, 12: {'Rente': 5, 'Bonds': 12}, 20: {'Rente': 7, 'Bonds': 20}}
	# print Bonds
	# Bondkeys = Bonds.keys()
	# Bondkeys.sort()
	# for bond in Bondkeys:
	# 	print 'Rente : {}, Bonds : {}'.format(Bonds[bond]['Rente'], Bonds[bond]['Bonds'])

	# for SP in Superpowers:
	# 	for bond in Bondkeys:

	# allbonds = {}
	# for sp in Superpowers:
	# 	allbonds[sp] = {bonds[index] : {'Rente' : rentes[index], 'Bond' : bonds[index]} for index in range(0, 9)}
	# for sp in Superpowers:
	# 	for bond in allbonds[sp].keys():
	# 		print sp, bond, allbonds[sp][bond]['Rente'], allbonds[sp][bond]['Bond']
	# bond = allbonds['USA'].popitem()
	# bond2 = allbonds['USA'].popitem()
	# print bond
	# print bond2
	# for sp in Superpowers:
	# 	for bond in allbonds[sp].keys():
	# 		print sp, bond, allbonds[sp][bond]['Rente'], allbonds[sp][bond]['Bond']

	# allbonds = {}
	# for sp in Superpowers:
	# 	allbonds[sp] = [{'Rente' : rentes[index], 'Bond' : bonds[index]} for index in range(0, 9)]
	# # for sp in Superpowers:
	# # 	print "{} : {}".format(sp, allbonds[sp])
	# bond = allbonds['USA'].pop(allbonds['USA'].index({'Rente': 3, 'Bond': 6}))

	# print allbonds['USA']
	# print bond

	# allbonds['USA'].append(bond)
	# allbonds['USA'].sort()

	# print allbonds['USA']

	# allbonds = {}
	for sp in Superpowers:
		allbonds[sp] = [{'Rente' : rentes[index], 'Bond' : bonds[index], 'Owner' : 'Bank'} for index in range(0, 9)]
	# for sp in Superpowers:
	# 	print "{} : {}".format(sp, allbonds[sp])
	bond = allbonds['USA'][3]['Owner'] = 'Player1'
	print allbonds['USA']

	# Bondscontent = {}
	# for index in range(9):
	# 	for sp in Superpowers:
	# 		Bondscontent[sp][bonds[index]] = {'Rente' : rentes[index], 'Bonds' : bonds[index]}}

	# Allbonds = {SP : {bond : {'Rente' : rente, 'Bonds' : bond}} for SP in Superpowers for bond in bonds for rente in rentes}
	# print Bondscontent

if __name__ == '__main__':
	sp = createsuperpowers()
	
