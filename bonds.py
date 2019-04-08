


def main():
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




	allbonds = {}
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
	main()