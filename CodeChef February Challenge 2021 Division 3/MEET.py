def converter(time):
	HM,zone=time.split(" ")
	H,M=list(map(int,HM.split(":")))
	if H==12 and zone=="AM":
		H=0
	elif H==12 and zone=="PM":
		H=12
	elif zone=="PM":
		H+=12

		#print(H)
	return(float(str(H)+"."+str(M)))

for _ in range(int(input())):
	shefTime=converter(input())
	ans=""
	for i in range(int(input())):
		temp=input()
		start=converter(temp[:8])
		end=converter(temp[9:])
		#print(temp[:8],temp[9:])
		#print(shefTime,start,end)
		if start<=shefTime<=end:
			ans+="1"
		else:
			ans+="0"
	print(int(ans))
