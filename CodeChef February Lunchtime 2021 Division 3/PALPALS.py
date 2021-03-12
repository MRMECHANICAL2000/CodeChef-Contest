from collections import defaultdict
for _ in range(int(input())):
	string=input()
	hashTable=defaultdict(list)
	for idx,val in enumerate(string):
		hashTable[val].append(idx)

	idx=0
	maxPalin=0
	while idx<len(string):
		flag=0
		possible=hashTable[string[idx]]
		possible.sort()
		for i in possible:
			if i>maxPalin:
				if string[idx:i+1]==string[idx:i+1][::-1]:
					maxPalin=i
					flag=1
		#if flag==0:
		#	print(idx,"NO_ME")
		#	break
		idx=maxPalin+1

	else:
		if maxPalin==len(string)-1:
			print("YES")
		else:
			print("NO")

