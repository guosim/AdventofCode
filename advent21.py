bosshp = 109
bossdmg = 8
bossarmor = 2
hp = 100
dmg = 8
armor = 3
alive = True
yourTurn = True

def fight(bosshp, bossdmg, bossarmor, hp, dmg, armor, alive, yourTurn):
	while alive == True:
		if yourTurn == True:
			bosshp = bosshp - (dmg - bossarmor)
			if bosshp <= 0:
				alive = False
				print hp, bosshp
			yourTurn = False
		else:
			hp = hp - (bossdmg - armor)
			if hp <= 0:
				alive = False
				print hp, bosshp
			yourTurn = True


fight(bosshp, bossdmg, bossarmor, hp, dmg, armor, alive, yourTurn)
