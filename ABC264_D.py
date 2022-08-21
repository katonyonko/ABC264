import io
from re import I
import sys

_INPUT = """\
6
catredo
atcoder
redocta
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import permutations
  from collections import deque
  def bfs(G,s):
    inf=10**20
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  dd={'a':0,'t':1,'c':2,'o':3,'d':4,'e':5,'r':6}
  S=input()
  i=0
  d={}
  G=[]
  for k in permutations(range(7)):
    d[k]=i
    i+=1
    G.append([])
  for k in permutations(range(7)):
    for i in range(6):
      tmp=list(k)
      tmp[i],tmp[i+1]=tmp[i+1],tmp[i]
      G[d[k]].append(d[tuple(tmp)])
  print(bfs(G,0)[d[tuple([dd[S[i]] for i in range(7)])]])