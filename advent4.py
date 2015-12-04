import hashlib
key = "iwrupvqb"
i = 0

while True:
	hash1 = hashlib.md5(key + str(i)).hexdigest()
	if (hash1[0] == '0' and hash1[1] == '0' and hash1[2] == '0' and hash1[3] == '0' and hash1[4] == '0' and hash1[5] == '0' and hash1[6] == '0'):
		print i
		break
	else:
		i = i + 1
