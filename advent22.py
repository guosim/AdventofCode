bosshp = 51
bossdmg = 9
hp = 50
alive = True
yourTurn = True
manaExhausted = 0
mana = 500
shield = False
shieldcounter = 0
poison = False
poisoncounter = 0
recharge = False
rechargecounter = 0

def fight(bosshp, bossdmg, hp, alive, yourTurn, manaE, mana, shield, shieldcounter, poison, poisoncounter, recharge, rechargecounter):
        while alive:
                if yourTurn == True:
                        hp = hp - 1
                        if hp == 0:
                                alive = False
                                print "you died to hard mode!"
                        print "Boss HP: ", bosshp
                        print "\tYour Stats: "
                        print "\tHP: ", hp
                        print "\tMana" , mana
                        print "\tSpent mana", manaE
                        print "\tShield", shield
                        print "\tPoison", poison
                        print "\tRecharge", recharge
                        if shield == True:
                                shieldcounter = shieldcounter - 1
                                if shieldcounter == 0:
                                        shield = False
                                        print "Shield gone"
                        if poison == True:
                                bosshp = bosshp - 3
                                poisoncounter = poisoncounter - 1
                                if poisoncounter == 0:
                                        poison = False
                                        print "Poison gone"
                        if recharge == True:
                                mana = mana + 101
                                rechargecounter = rechargecounter - 1
                                if rechargecounter == 0:
                                        recharge = False
                                        print "Recharge gone"
                                        
                        action = raw_input("ACTION!")
                        if action == "1":
                                mana = mana - 53
                                manaE = manaE + 53
                                bosshp = bosshp - 4
                        elif action == "2":
                                mana = mana - 73
                                manaE = manaE + 73
                                bosshp = bosshp - 2
                                hp = hp + 2
                        elif action == "3":
                                mana = mana - 113
                                manaE = manaE + 113
                                shield = True
                                shieldcounter = 6
                        elif action == "4":
                                mana = mana - 173
                                manaE = manaE + 173
                                poison = True
                                poisoncounter = 6
                        elif action == "5":
                                mana = mana - 229
                                manaE = manaE + 229
                                recharge = True
                                rechargecounter = 5
                                
                        bosshp = bosshp
                        if bosshp <= 0:
                                alive = False
                                print hp, bosshp, manaE
                        yourTurn = False
                else:
                        print "BOSS TURN"
                        print "Boss HP: ", bosshp
                        print "Your Stats: ",
                        print "\tHP: ", hp
                        print "\tMana" , mana
                        print "\tSpent mana", manaE
                        print "\tShield", shield
                        print "\tPoison", poison
                        print "\tRecharge", recharge


                                        
                        if poison == True:
                                bosshp = bosshp - 3
                                if bosshp <= 0:
                                        print hp, bosshp, "mana used ", manaE
                                poisoncounter = poisoncounter - 1
                                if poisoncounter == 0:
                                        poison = False
                        if recharge == True:
                                mana = mana + 101
                                rechargecounter = rechargecounter - 1
                                if rechargecounter == 0:
                                        recharge = False

                        hp = hp - bossdmg
                        if shield == True:
                                hp = hp + 7
                                shieldcounter = shieldcounter - 1
                                if shieldcounter == 0:
                                        shield = False
                        if hp <= 0 or bosshp <= 0:
                                alive = False
                                print hp, bosshp, "mana used ", manaE
                        yourTurn = True


fight(bosshp, bossdmg, hp, alive, yourTurn, manaExhausted, mana, shield, shieldcounter, poison, poisoncounter, recharge, rechargecounter)
