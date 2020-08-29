from itertools import combinations
for _ in range(int(input())):
	input()
	count=0
	arr=list(map(int,input().split()))
	if len(arr)==1:
		print(count)

	else:
		for i in combinations(arr,2):
			if i[0]&i[1]==i[0]:
				count+=1
		print(count)