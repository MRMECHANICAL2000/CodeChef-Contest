import math

def helperFunction(bitMask,idx,a,b):
	if idx>=len(bitMask):
		return(a,b)
	else:
		if bitMask[idx]=='0':
			a,b=helperFunction(bitMask,idx+1,a+'1',b+'1')
		else:
			if a=="":
				a+='1'
				b+='0'
			else:
				a+='0'
				b+='1'

			a,b=helperFunction(bitMask,idx+1,a,b)

		return(a,b)

for _ in range(int(input())):
	c=int(input())
	d=math.ceil(math.log(c,2))
	d=d+1 if d<=c else d
	bitMask=bin(c)[2:]
	finaVal_1,finalVal_2=helperFunction(bitMask,0,"","")
	result=int(finaVal_1,2)*int(finalVal_2,2)
	print(result)
