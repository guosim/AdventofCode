from copy import deepcopy

rf = open('advent18.txt','r')
num = len(rf.readlines())
rf.seek(0)
grid = []

for i in range(0,num):
    line = list(rf.readline().replace('\n',''))
    grid.append(line)

grid[0][0] = '#'
grid[0][99] = '#'
grid[99][0] = '#'
grid[99][99] = '#'
newgrid = deepcopy(grid)
for x in range(0, 100):
    for i in range(0, 100):
        for j in range(0, 100):
            if grid[i][j] == '#':
                neighbor = 0
                if i != 0: #not on top 0 is top, 0 is left
                    if grid[i-1][j] == '#':
                        neighbor = neighbor + 1
                if i != 99: # not on bottom
                    if grid[i+1][j] == '#':
                        neighbor = neighbor + 1
                if j != 0: # not on left
                    if grid[i][j-1] == '#':
                        neighbor = neighbor + 1
                if j != 99: # not on right
                    if grid[i][j+1] == '#':
                        neighbor = neighbor + 1
                if i != 0 and j != 0: # not top left corner
                    if grid[i-1][j-1] == '#':
                        neighbor = neighbor + 1
                if i != 99 and j != 0: #not bottom left
                    if grid[i+1][j-1] == '#':
                        neighbor = neighbor + 1
                if i != 0 and j != 99: #not top right
                    if grid[i-1][j+1] == '#':
                        neighbor = neighbor + 1
                if i != 99 and j != 99: #not bottom right
                    if grid[i+1][j+1] == '#':
                        neighbor = neighbor + 1
                if neighbor == 2 or neighbor == 3:
                    newgrid[i][j] = '#'
                else:
                    newgrid[i][j] = '.'
                newgrid[0][0] = '#'
                newgrid[0][99] = '#'
                newgrid[99][0] = '#'
                newgrid[99][99] = '#'
            else:
                neighbor = 0
                if i != 0: #not on top 0 is top, 0 is left
                    if grid[i-1][j] == '#':
                        neighbor = neighbor + 1
                if i != 99: # not on bottom
                    if grid[i+1][j] == '#':
                        neighbor = neighbor + 1
                if j != 0: # not on left
                    if grid[i][j-1] == '#':
                        neighbor = neighbor + 1
                if j != 99: # not on right
                    if grid[i][j+1] == '#':
                        neighbor = neighbor + 1
                if i != 0 and j != 0: # not top left corner
                    if grid[i-1][j-1] == '#':
                        neighbor = neighbor + 1
                if i != 99 and j != 0: #not bottom left
                    if grid[i+1][j-1] == '#':
                        neighbor = neighbor + 1
                if i != 0 and j != 99: #not top right
                    if grid[i-1][j+1] == '#':
                        neighbor = neighbor + 1
                if i != 99 and j != 99: #not bottom right
                    if grid[i+1][j+1] == '#':
                        neighbor = neighbor + 1
                if neighbor == 3:
                    newgrid[i][j] = '#'
                else:
                    newgrid[i][j] = '.'
                grid[0][0] = '#'
                grid[0][99] = '#'
                grid[99][0] = '#'
                grid[99][99] = '#'
    grid = deepcopy(newgrid)

count = 0
for i in range(0, 100):
    for j in range(0, 100):
        if grid[i][j] == '#':
            count = count + 1
print count
#3890, 3791 too high #928 wrong
#780 low
