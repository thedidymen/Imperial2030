from random import shuffle
import CreateGame as cg 


class gameStats(object):
	"""docstring for gameStats"""
	def __init__(self):
		create = cg.CreateGame()
		super(gameStats, self).__init__()
		self.players = create.createplayers()
		self.superpowers = create.createsuperpowers()
		self.areas = create.createmap()
		self.bonds = create.createbonds()
		self.nationorder = create.nationorder()
		self.playerorder = self.players.keys()
		shuffle(self.playerorder)



	def nextcountry(self):
		nc = self.nationorder.pop(0)
		self.nationorder.append(nc)
		return nc


	def nextplayer(self, player=None):
		if player == None:
			np = self.playerorder.pop(0)
			self.playerorder.append(np)
			return np
		else:
			currentplayer = self.nextplayer()
			while currentplayer != player:
				currentplayer = self.nextplayer()
			currentplayer = self.nextplayer()		
			return currentplayer

def test(game):
	print "test GameStats.nextcountry"
	for n in range(int(2.5*len(game.nationorder))):
		print game.nextcountry()
	print
	print "test Game.Stats.nextplayer"
	for n in range(int(2.5*len(game.playerorder))):
		print game.nextplayer()
	print
	player = game.playerorder[2]
	print player
	print game.nextplayer(player=player)



if __name__ == '__main__':
	game = gameStats()
	test(game)
  		