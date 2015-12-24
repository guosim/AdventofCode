class deer:
        def __init__(self, fly, second, rest):
                self.fly = fly
                self.second = second
                self.rest = rest
                self.distance = 0
                self.point = 0
                self.restState = False
                self.counter = 0

rein = []
rein.append(deer(8,8,53))
rein.append(deer(13,4,49))
rein.append(deer(20,7,132))
rein.append(deer(12,4,43))
rein.append(deer(9,5,38))
rein.append(deer(10,4,37))
rein.append(deer(3,37,76))
rein.append(deer(9,12,97))
rein.append(deer(37,1,36))
for j in range(0, 2503):
        for i in rein:
                if i.restState == False:#if not tired, fly, increment fly counter
                        i.distance = i.distance + i.fly
                        i.counter = i.counter + 1
                        if i.counter == i.second:
                                i.restState = True
                                i.counter = 0
                else:#else, rest, increment rest counter, once fully rested (modulus), rest counter = 0, not tired
                        i.counter = i.counter + 1
                        if i.counter % i.rest == 0:
                                i.counter = 0
                                i.restState = False

for i in rein:
        print i.distance
