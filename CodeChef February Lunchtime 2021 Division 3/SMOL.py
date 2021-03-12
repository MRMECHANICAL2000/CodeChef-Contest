for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	if k==0:
		print(n)
	else:
		print(n%k)