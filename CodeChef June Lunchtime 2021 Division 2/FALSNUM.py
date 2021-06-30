for _ in range(int(input())):
	array=list(input())
	#array.sort()
	if array[0]=='1':
		print("".join([array[0]]+['0']+array[1:]))
	else:
		print("".join(['1']+array))

