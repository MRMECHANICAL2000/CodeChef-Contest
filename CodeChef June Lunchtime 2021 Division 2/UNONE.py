for _ in range(int(input())):
	n=int(input())
	array=list(map(int,input().split()))
	odd=[]
	even=[]
	for i in array:
		if i%2==0:
			odd.append(i)
		else:
			even.append(i)
	print(*even,*odd)
