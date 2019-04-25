from random import shuffle
import CreateGame as cg 


class gameStats(object):
	"""docstring for gameStats"""
	def __init__(self):
		create = cg.CreateGame()
		super(gameStats, self).__init__()
		self.players = create.createplayers()
		self.nations = create.createsuperpowers()
		self.areas = create.createmap()
		self.bonds = create.createbonds()
		self.nationorder = create.nationorder()
		self.playerorder = self.players.keys()
		shuffle(self.playerorder)


	def nextcountry(self, nation):
		return self.nationorder[self.nationorder.index(nation)+1-len(self.nationorder)]


	def nextplayer(self, player):	
		return self.playerorder[self.playerorder.index(player)+1-len(self.playerorder)]


	def buidunits(self, area, country):
		pass

	
	def gainmoney(self, player=None, nation=None):
		pass


	def factorybuildpositions(self, nation):
		pass


	def buildfactory(self, area):
		pass


	def getimportoptions(self, nation):
		pass


	def getunitmoveoptions(self, area, country):
		pass


	def getboats(self, country):
		pass

	
	def getarmy(self, country):
		pass


	def returninvestor(self):
		pass


	def returnrulernation(self, nation):
		pass


	def raisepowerlvl(self, country, amount):
		pass


	def getpowerlvl(self, country):
		pass


	def areagainunit(self, area, amount=1):
		pass


	def areaoccupied(self, area):
		pass


	def getbonds(self, player='Bank'):
		pass

	def buybonds(self, numberofbonds, player, returnedbonds=0):
		pass


	def getinterestpayout(self, country):
		pass


	def getsaldo(self, player=None, Country=None):
		pass


	def raisetax(self, country):
		# ???
		pass


	def unitspresent(self, area):
		pass


	def unitsnations(self, country):
		pass
	

def test(game):
	print "test GameStats.nextcountry"
	for nation in game.nationorder:
		print "current: {}, next {}".format(nation, game.nextcountry(nation))
	print
	print "test Game.Stats.nextplayer"
	for player in game.playerorder:
		print "current: {}, next {}".format(player, game.nextplayer(player))
	print
	player = game.playerorder[2]
	print player
	print game.nextplayer(player)



if __name__ == '__main__':
	game = gameStats()
	test(game)
  		