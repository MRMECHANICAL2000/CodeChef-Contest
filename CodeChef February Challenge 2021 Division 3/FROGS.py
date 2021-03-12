import math
for _ in range(int(input())):
	n=int(input())
	weight=[int(i) for i in input().split()]
	jump=[int(i) for i in input().split()]
	count=0
	hashTable={}
	for i in range(n):
		hashTable[weight[i]]=[i,jump[i]]
	weight.sort()
	lastIdx=hashTable[weight[0]][0]
	for i in range(1,n):
		curIdx=hashTable[weight[i]][0]
		curJump=hashTable[weight[i]][1]

		#while lastIdx>=curIdx:
		k=math.ceil((lastIdx-curIdx)/curJump)
		if curIdx+curJump*k==lastIdx:
			k+=1
		curIdx+=curJump*k
		count+=k
		lastIdx=curIdx
		#print(hashTable[weight[i]][0],curIdx,weight[i])
	print(count)


