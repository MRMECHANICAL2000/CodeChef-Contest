import sys
for _ in range(int(input())):
	a,b=list(map(int,sys.stdin.readline().split()))
	#x=math.log(b,2)
	if b&(b-1)==0:
		print("YES")
	else:
		print("NO")
