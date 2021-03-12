for _ in range(int(input())):
	n=int(input())
	array=[int(i) for i in input().split()]
	array.sort()
	i,j,k,l=array[0],array[1],array[-1],array[-2]
	print(max(i*j+abs(j-i),k*l+abs(l-k)))

