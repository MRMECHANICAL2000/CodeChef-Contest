for _ in range(int(input())):
	n=input()
	arr=list(map(int,input().split()))
	arr.sort()
	x=arr[0]
	y=arr[len(arr)//2]
	z=arr[-1]
	print(abs(x-y)+abs(x-z)+abs(y-z))