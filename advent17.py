import itertools

rf = open('advent17.txt', 'r')
i = len(rf.readlines())
rf.seek(0)
nums = []
mini = 100
combinations = []
count = 0
for i in range(0, i):
        line = rf.readline().replace('\n','')
        nums.append(int(line))




for i in range(0, len(nums)+1):
        for subset in itertools.combinations(nums, i):
                if sum(subset) == 150 and len(subset) == 4:
                        count = count + 1
print count
