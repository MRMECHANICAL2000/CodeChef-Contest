for _ in range(int(input())):
	delivery,coupon=[int(i) for i in input().split()]
	day1=[int(i) for i in input().split()]
	day2=[int(i) for i in input().split()]

	cost1=True if sum(day1)>=150 else False
	cost2=True if sum(day2)>=150 else False

	cur=2*delivery
	if 2*delivery>coupon:
		if cost2 and cost1:
			print("YES")
		elif cost1 and 2*delivery>coupon+delivery:
			print("YES")
		elif cost2 and 2*delivery>coupon+delivery:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")



