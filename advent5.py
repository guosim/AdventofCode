import re
rf = open('advent5.txt', 'r')
i = len(rf.readlines())
rf.seek(0)

nice = 0

for i in range(0, i):
    line = rf.readline()
    ab = re.compile('^(?!.*(ab|cd|pq|xy)).*$')
    b = ab.search(line)
    if b == None:
        print line
 #length = 16
 
 #3 vowels
 #one double
 #no special string
 #ab, cd, pq, or xy,
