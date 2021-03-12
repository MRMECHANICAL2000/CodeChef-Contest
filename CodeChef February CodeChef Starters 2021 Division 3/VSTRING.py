for _ in range(int(input())):
	n,d=[int(i) for i in input().split()]
	array=input()
	zeroCount=0
	for i in array:
		#print("Where",i)
		if i=='0':
			#print("here")
			zeroCount+=1
		else:
			break
	for i in array[::-1]:
		if i=='0':
			zeroCount+=1
		else:
			break
	#print(zeroCount,d)
	needRoot=0
	prevOne=None
	for idx,val in enumerate(array):
		if val=='1':
			if prevOne==None:
				prevOne=idx
			else:
				if idx-prevOne-1>d:
					needRoot+=1
				prevOne=idx
	if needRoot==0:
		print("YES")
	elif needRoot==1:
		if zeroCount>d:
			print("NO")
		else:
			print("YES")
	else:
		print("NO")




