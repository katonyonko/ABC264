import io
import sys

_INPUT = """\
6
5 5 10
2 3
4 10
5 10
6 9
2 9
4 8
1 7
3 6
8 10
1 8
6
3
5
8
10
2
7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #Union Find
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  N,M,E=map(int,input().split())
  edge=[list(map(int, input().split())) for _ in range(E)]
  Q=int(input())
  X=[int(input())-1 for i in range(Q)]
  s=set(X)
  uf=UnionFind(N+M+1)
  ans=[]
  tmp=0
  for i in range(M):
    uf.union(0,N+1+i)
  for i in range(E):
    if i not in s:
      u,v=edge[i]
      if uf.find(u)==uf.find(0) and uf.find(v)!=uf.find(0): tmp+=uf.size(v)
      if uf.find(u)!=uf.find(0) and uf.find(v)==uf.find(0): tmp+=uf.size(u)
      uf.union(u,v)
  ans.append(tmp)
  for i in range(Q-1,0,-1):
    u,v=edge[X[i]]
    if uf.find(u)==uf.find(0) and uf.find(v)!=uf.find(0): tmp+=uf.size(v)
    if uf.find(u)!=uf.find(0) and uf.find(v)==uf.find(0): tmp+=uf.size(u)
    uf.union(u,v)
    ans.append(tmp)
  for i in reversed(range(Q)):
    print(ans[i])