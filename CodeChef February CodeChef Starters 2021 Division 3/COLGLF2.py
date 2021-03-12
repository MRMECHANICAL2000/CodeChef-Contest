for _ in range(int(input())):
	season=int(input())
	intro=[int(i) for i in input().split()]
	episodeCount=[]
	episode=[]
	for i in range(season):
		temp=[int(i) for i in input().split()]
		episodeCount.append(temp[0])
		episode.append(temp[1:])

	watchTime=0

	for idx,val in enumerate(episode):
		watchTime+=sum(val)-(len(val)-1)*intro[idx]
	print(watchTime)

