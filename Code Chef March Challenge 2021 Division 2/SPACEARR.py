for _ in range(int(input())):
	c=int(input())

	finalArray=list(map(int,input().split()))
	finalNumber=[i for i in range(1,c+1)]
	totalPossibleMove=0
	finalArray.sort()
	finalNumber.sort()
	for idx in range(len(finalArray)):
		if finalArray[idx]<=finalNumber[idx]:
			totalPossibleMove+=finalNumber[idx]-finalArray[idx]
		else:
			print("Second")
			break

	else:
		if totalPossibleMove%2==0:
			print("Second")
		else:
			print("First")
