#make 1000x1000 array
array =[[0 for col in range(5000)] for row in range(5000)]
	
santaX = 2500
santaY = 2500
roboX = 2500
roboY = 2500
array[2500][2500] = 1
total = 0 #500,500 = visited

rf = open('advent3input.txt', 'r')
manual = rf.readline()
for a in xrange(0, len(manual), 2):
	if manual[a] == "<":
		santaX = santaX - 1
		array[santaX][santaY] = 1
	elif manual[a] == ">":
		santaX = santaX + 1
		array[santaX][santaY] = 1
	elif manual[a] == "^":
		santaY = santaY + 1
		array[santaX][santaY] = 1
	elif manual[a] == "v":
		santaY = santaY - 1
		array[santaX][santaY] = 1
	if manual[a+1]  == "<":
		roboX = roboX - 1
		array[roboX][roboY] = 1
	elif manual[a+1] == ">":
		roboX = roboX + 1
		array[roboX][roboY] = 1
	elif manual[a+1]== "^":
		roboY = roboY + 1
		array[roboX][roboY] = 1
	elif manual[a+1]== "v":
		roboY = roboY - 1
		array[roboX][roboY] = 1


for i in range(5000):
	for j in range(5000):
		if array[i][j] == 1:
			total = total + 1
			
print total
