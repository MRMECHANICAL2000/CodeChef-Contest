#Fast IO Libraries
import os
import sys
from io import BytesIO, IOBase

#Library for our use
# import math
# from collections import Counter
# from collections import defaultdict
# from collections import deque
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import accumulate,permutations as perm,combinations as comb
# import heapq
# from functools import reduce
# from fractions import Fraction
# import sys


def main():
	for _ in range(int(input())):
		n,m,k=list(map(int,input().split()))
		state=[]
		for i in range(n*m):
			x,y=list(map(int,input().split()))
			state.append([x-1,y-1])

		board=[[0 for i in range(m)] for j in range(n)]
		prefix=[[0 for i in range(m)] for j in range(n)]

		low=1
		high=n*m
		winState=None
		while low<=high:
			mid=low+(high-low)//2
			for i in range(n):
				for j in range(m):
					prefix[i][j]=0
					board[i][j]=0

			#creating Board
			for i in range(mid):
				x,y=state[i]
				if i%2==0:
					board[x][y]=1
				else:
					board[x][y]=-1
					
			'''
			#My Move - got TLE
			#Creating Prefix Matrix
			for i in range(n):
				for j in range(m):
					top,left,topLeft=(i,j-1),(i-1,j),(i-1,j-1)

					prefix[i][j]=board[i][j]
					if 0<=top[0]<n and 0<=top[1]<m:
						prefix[i][j]+=prefix[top[0]][top[1]]

					if 0<=left[0]<n and 0<=left[1]<m:
						prefix[i][j]+=prefix[left[0]][left[1]]

					if 0<=topLeft[0]<n and 0<=topLeft[1]<m:
						prefix[i][j]-=prefix[topLeft[0]][topLeft[1]]

					#Formula : prefix[i][j]=board[i][j]+prefix[i][j-1]+prefix[i-1][j]-prefix[i-1][j-1]

			#checking if someone Wins
			flag=0
			for i in range(n):
				for j in range(m):
					top,left,topLeft=(i,j-k),(i-k,j),(i-k,j-k)
					check=prefix[i][j]
					if 0<=top[0]<n and 0<=top[1]<m:
						check-=prefix[top[0]][top[1]]

					if 0<=left[0]<n and 0<=left[1]<m:
						check-=prefix[left[0]][left[1]]

					if 0<=topLeft[0]<n and 0<=topLeft[1]<m:
						check+=prefix[topLeft[0]][topLeft[1]]

					if abs(check)==k*k:
						flag=1
						break

				if flag==1:
					break
			'''

			#Best CP Approach
			#Creating Prefix Matrix

			prefix[0][0]=board[0][0]
			for i in range(1,m):
				prefix[0][i]=prefix[0][i-1]+board[0][i]
			for i in range(1,n):
				prefix[i][0]=prefix[i-1][0]+board[i][0]
			for i in range(1,n):
				for j in range(1,m):
					prefix[i][j]=board[i][j]+prefix[i][j-1]+prefix[i-1][j]-prefix[i-1][j-1]

			flag=0
			for i in range(k-1,n):
				for j in range(k-1,m):
					top,left,topLeft=(i,j-k),(i-k,j),(i-k,j-k)
					check=prefix[i][j]
					if 0<=top[1]:
						check-=prefix[top[0]][top[1]]

					if 0<=left[0] :
						check-=prefix[left[0]][left[1]]

					if 0<=topLeft[0] and 0<=topLeft[1]:
						check+=prefix[topLeft[0]][topLeft[1]]

					if abs(check)==k*k:
						flag=1
						break

				if flag==1:
					break
			'''
			#checking if someone Wins
			flag=0
			for i in range(k-1,n):
				for j in range(k-1,m):
					check=prefix[i][j]-prefix[i][j-k]-prefix[i-k][j]+prefix[i-k][j-k]

					if abs(check)==k*k:
						print("i,j : "i,j)
						flag=1
						break

				if flag==1:
					break '''

			#print()
			#print(low,mid,high)
			#print("Board :")
			#[print(i) for i in board]
			#print("Prefix:")
			#[print(i) for i in prefix]

			if abs(check)==k*k:
				#print("here",check,k)
				winState=mid
				high=mid-1
			else:
				low=mid+1

		if winState==None:
			print("Draw")
		elif winState%2==0:
			print("Bob")
		else:
			print("Alice")


# shortcut for functions
def I(): return input()

def Iint(): return int(input())

def Ilist(): return list(map(int, input().split()))   # int list

def Imap(): return map(int, input().split())   # int map

def Plist(li, s=' '): print(s.join(map(str, li)))   # non string list



# Region fastio functions

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()


