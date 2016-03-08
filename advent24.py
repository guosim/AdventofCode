rf = open('advent24.txt','r')
num = len(rf.readlines())
rf.seek(0)
gift = []
gifts = gift
group = []
for i in range(0,num):
    line = int(rf.readline())
    gift.append(line)

print gift
    
#group weight = 512
#greedy algo to make groups?
