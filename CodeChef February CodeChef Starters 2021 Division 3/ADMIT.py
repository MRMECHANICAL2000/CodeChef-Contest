import sys
for _ in range(int(input())):
	noCollege,noStudent=list(map(int,sys.stdin.readline().strip().split()))
	collegeHT={}
	collegeRank={}
	studentHT={}
	for idx,val in enumerate(list(map(int,sys.stdin.readline().strip().split()))):
		collegeHT[val]=[idx+1,"Free"]
		collegeRank[idx+1]=val
		
	for idx,val in enumerate(list(map(int,sys.stdin.readline().strip().split()))):
		studentHT[val]=[idx+1,sorted(collegeRank[i] for i in list(map(int,sys.stdin.readline().strip().split()))[1:])]



	for rank in sorted(studentHT.keys()):
		stuID,prefCol=studentHT[rank]
		selectedCol=0
		for i in prefCol:
			if collegeHT[i][1]=="Free":
				collegeHT[i][1]="Admited"
				selectedCol=collegeHT[i][0]
				break
		if stuID==1:
			print(selectedCol)
			break
	#print(studentHT)
	#print(collegeHT)



