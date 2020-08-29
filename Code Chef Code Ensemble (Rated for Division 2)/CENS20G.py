#Fast IO Libraries
import os
import sys
from io import BytesIO, IOBase

#Library for our use
# import math
from collections import Counter
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
	    string=Counter(input())
	    x,y=list(map(int,input().split()))
	    ans=[]

	    for j in range(int(input())):
		    x2,y2=list(map(int,input().split()))
		    count=0
		    a,b=x2-x,y2-y
		    if a>=0 and string["R"]<abs(a):
			    print("NO")
			    continue
		    elif a<0 and string["L"]<abs(a):
			    print("NO")
			    continue
		    if b>=0 and string["U"]<abs(b):
			    print("NO")
			    continue
		    elif b<0 and string["D"]<abs(b):
			    print("NO")
			    continue
		    print("YES",abs(a)+abs(b))



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