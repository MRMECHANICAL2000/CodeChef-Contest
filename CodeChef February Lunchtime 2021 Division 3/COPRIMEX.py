def SieveOfEratosthenes(n):
	prime=[True for i in range(n+1)]
	cur=2
	while cur*cur<=n:
		if prime[cur]==True:
			for idx in range(cur*cur,n+1,cur):
				prime[idx]=False
		cur+=1
	return(prime)


prime=SieveOfEratosthenes(2*(10**6)+1)
for _ in range(int(input())):
	array=list(map(int,input().split()))
	for i in range(array[1]+1,len(prime)):
		if prime[i]==True:
			print(i)
			break
