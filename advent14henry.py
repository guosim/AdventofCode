#Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
#Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
#Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
#Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
#Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
#Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
#Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
#Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
#Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.

vix = 0
vixrest = False
vixcounter = 0

rud = 0
rudrest = False
rudcounter = 0

don = 0
donrest = False
doncounter = 0

blitz = 0
blitzrest = False
blitzcounter = 0

com = 0
comrest = False
comcounter = 0

cup = 0
cuprest = False
cupcounter = 0

dash = 0
dashrest = False
dashcounter = 0

danc = 0
dancrest = False
danccounter = 0

pranc = 0
prancrest = False
pranccounter = 0

dist = []
dist.append(vix)
dist.append(rud)
dist.append(don)
dist.append(blitz)
dist.append(com)
dist.append(cup)
dist.append(dash)
dist.append(danc)
dist.append(pranc)

points = []
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)

for i in range(0,2503):
    if (vixrest == False):
        dist[0] = dist[0] + 8
        vixcounter = vixcounter + 1
        if (vixcounter == 8):
            vixrest = True
            vixcounter = 0
    else:
        vixcounter = vixcounter + 1
        if (vixcounter == 53):
            vixrest = False
            vixcounter = 0
    #print vix       
    if (rudrest == False):
        dist[1] = dist[1] + 20
        rudcounter = rudcounter + 1
        if (rudcounter == 7):
            rudrest = True
            rudcounter = 0
    else:
        rudcounter = rudcounter + 1
        if (rudcounter == 132):
            rudrest = False
            rudcounter = 0
    #print rud
    if (donrest == False):
        dist[2] = dist[2] + 9
        doncounter = doncounter + 1
        if (doncounter == 5):
            donrest = True
            doncounter = 0
    else:
        doncounter = doncounter + 1
        if (doncounter == 38):
            donrest = False
            doncounter = 0
    #print don
    if (blitzrest == False):
        dist[3] = dist[3] + 13
        blitzcounter = blitzcounter + 1
        if (blitzcounter == 4):
            blitzrest = True
            blitzcounter = 0
    else:
        blitzcounter = blitzcounter + 1
        if (blitzcounter == 49):
            blitzrest = False
            blitzcounter = 0
    #print blitz
    if (comrest == False):
        dist[4] = dist[4] + 3
        comcounter = comcounter + 1
        if (comcounter == 37):
            comrest = True
            comcounter = 0
    else:
        comcounter = comcounter + 1
        if (comcounter == 76):
            comrest = False
            comcounter = 0
    #print com
    if (cuprest == False):
        dist[5] = dist[5] + 12
        cupcounter = cupcounter + 1
        if (cupcounter == 4):
            cuprest = True
            cupcounter = 0
    else:
        cupcounter = cupcounter + 1
        if (cupcounter == 43):
            cuprest = False
            cupcounter = 0
    #print cup
    if (dashrest == False):
        dist[6] = dist[6] + 10
        dashcounter = dashcounter + 1
        if (dashcounter == 4):
            dashrest = True
            dashcounter = 0
    else:
        dashcounter = dashcounter + 1
        if (dashcounter == 37):
            dashrest = False
            dashcounter = 0
    #print dash
    if (dancrest == False):
        dist[7] = dist[7] + 37
        danccounter = danccounter + 1
        if (danccounter == 1):
            dancrest = True
            danccounter = 0
    else:
        danccounter = danccounter + 1
        if (danccounter == 36):
            dancrest = False
            danccounter = 0
    #print danc
    if (prancrest == False):
        dist[8] = dist[8] + 9
        pranccounter = pranccounter + 1
        if (pranccounter == 12):
            prancrest = True
            pranccounter = 0
    else:
        pranccounter = pranccounter + 1
        if (pranccounter == 97):
            prancrest = False
            pranccounter = 0
    #print pranc
    maxi = 0
    index = 0
    for j in range(0,9):
        if (dist[j] > maxi):
            maxi = dist[j]
            index = j
    for k in range(0,9):
        if (dist[k] == maxi):
            points[k] = points[k] + 1

maxi = 0
for i in range(0,9):
    if (points[i] > maxi):
        maxi = points[i]

print maxi
