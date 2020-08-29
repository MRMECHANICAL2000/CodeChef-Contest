#Fast IO Libraries
import os
import sys
from io import BytesIO, IOBase

#Library for our use
# import math
from collections import Counter
from collections import defaultdict
from collections import deque
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import accumulate,permutations as perm,combinations as comb
# import heapq
# from functools import reduce
# from fractions import Fraction
# import sys

class Graph():
	def __init__(self,vertex,weight):
		self.node=vertex
		self.adjList=defaultdict(list)
		self.weight=defaultdict(list)

		for i in range(1,self.node+1):
			self.adjList[i]=[]
			setbit=(bin(weight[i-1])).count('1')
			self.weight[i]=[weight[i-1],setbit,0 if setbit%2==0 else 1] #Even-0 Odd-1
			#print(self.weight[i],i,weight[i-1])


	def addEdge(self,start,end):
		self.adjList[start].append(end)
		self.adjList[end].append(start)

	def __str__(self):
		for i in range(1,self.node+1):
			print("{} -> {} : {}".format(i,self.adjList[i],self.weight[i]))
		return("")

	def BFS(self,start,visited):
		cc=[start]
		queue=deque([start])
		while queue:
			#print(queue)
			curVer=queue.popleft()
			for i in self.adjList[curVer]:
				#print(i)
				if visited[i]==False and self.weight[start][2]==self.weight[i][2]:
					queue.append(i)
					cc.append(i)
					visited[i]=True
		#print(visited)
		return(cc,visited)

	def connectedComponent(self):
		totalCC=[]
		visited=defaultdict(bool)
		for i in self.adjList.keys():
			visited[i]=False
		for i in self.adjList.keys():
			#print(i,visited)
			if visited[i]==False:
				visited[i]=True
				cc,visited=self.BFS(i,visited)
				totalCC.append(cc)
		#print(visited)
		return(totalCC)


	def parityOfCC(self,cc):
		odd=0
		even=0
		for i in cc:
			setbit=self.weight[i][2]
			#print(setbit)
			if setbit==0:
				even+=1
			else:
				odd+=1
			#print(i,setbit)
		#print(odd,even)
		return(odd,even)


def main():
	for _ in range(Iint()):
		w,n=[int(i) for i in input().split()]
		weight=Ilist()
		#print(weight)
		g=Graph(w,weight)
		for i in range(n):
			a,b=Ilist()
			g.addEdge(a,b)
		#print(g)
		ccList=g.connectedComponent()
		#print(ccList)
		oddMax=0
		evenMax=0

		for i in ccList:
			odd,even=g.parityOfCC(i)
			#print(odd,oddMax,even,evenMax,len(i),oddLen)
			if odd>oddMax:
				oddMax=odd
			if even>evenMax:
				evenMax=even
		#print("oemax",oddMax,evenMax)

		for i in range(Iint()):
			q,k=Ilist()
			setbit=(bin(k)).count('1')
			parity=1
			if setbit%2==0:
				parity=0 #Even
			if q==1:
				if parity==0:
					print(oddMax)
				else:
					print(evenMax)

			elif q==2:
				if parity==0:
					print(evenMax)
				else:
					print(oddMax)


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