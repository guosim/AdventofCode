def turnOff(i, j, i2, j2, array):
        for x in range(i,i2+1):
                for y in range(j, j2+1):
                        if (array[x][y] > 0):
                                array[x][y] += -1
        return array

def turnOn(i, j, i2, j2, array):
        for x in range(i,i2+1):
                for y in range(j, j2+1):
                        array[x][y] += 1
        return array

def toggle(i, j, i2, j2, array):
        for x in range(i,i2 + 1):
                for y in range(j, j2+1):
                        array[x][y] += 2
        return array

def count(array):
        count = 0
        for i in range(0,1000):
                for j in range(0,1000):
                        count += array[i][j]
        return count

array = [[0 for col in range(1000)] for row in range(1000)]
rf = open('advent6.txt', 'r')
i = len(rf.readlines())
rf.seek(0)

for i in range(0, i):
        line = rf.readline().replace('turn', '').replace(',',' ').strip().split(' ')
        if line[0] == "on":
                array = turnOn(int(line[1]), int(line[2]),int(line[4]),int(line[5]),array)  
        elif line[0] == "off":
                array = turnOff(int(line[1]), int(line[2]),int(line[4]),int(line[5]),array)  
        elif line[0] == "toggle":
                array = toggle(int(line[1]), int(line[2]),int(line[4]),int(line[5]),array)
        
print count(array)
                

 
