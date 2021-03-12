for _ in range(int(input())):
	array=list(map(int,input().split()))
	k=int(input())
	idx=9

	while k>0:
		if k<array[idx]:
			array[idx]-=k
			k=0
		else:
			temp=array[idx]
			array[idx]=0
			k-=temp
		idx-=1
	for idx,val in enumerate(array[::-1]):
		if val>0:
			print(10-idx)
			break