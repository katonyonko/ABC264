import io
import sys

_INPUT = """\
6
3
a -5
ab 10
ba -20
28
a -5
ab 10
ba -20
bb -20
bc -20
bd -20
be -20
bf -20
bg -20
bh -20
bi -20
bj -20
bk -20
bl -20
bm -20
bn -20
bo -20
bp -20
bq -20
br -20
bs -20
bt -20
bu -20
bv -20
bw -20
bx -20
by -20
bz -20
26
a -1
b -1
c -1
d -1
e -1
f -1
g -1
h -1
i -1
j -1
k -1
l -1
m -1
n -1
o -1
p -1
q -1
r -1
s -1
t -1
u -1
v -1
w -1
x -1
y -1
z -1
"""
sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  G=[[] for _ in range(26**2)]
  score=[0]*(26+26**2+26**3)
  for i in range(N):
    T,P=input().split()
    idx=sum([(ord(T[j])-ord('a'))*(26**(len(T)-1-j)) for j in range(len(T))])+(0 if len(T)==1 else 26 if len(T)==2 else 26+26**2)
    score[idx]=int(P)
  for i in range(26**2):
    for j in range(26):
      a,b=i//26,i%26
      tmp=score[j]+score[26+b*26+j]+score[26+26**2+i*26+j]
      G[i].append((tmp,b*26+j))
  ans=max(score[:26])
  res=[0]*(26**2)
  for i in range(26**2):
    res[i]=score[i//26]+score[i%26]+score[26+i]
  ans=max(ans,max(res))
  for i in range(26**2):
    tmp=res.copy()
    for j in range(26**2):
      for c,v in G[j]:
        tmp[v]=max(tmp[v],res[j]+c)
    res=tmp
    ans=max(ans,max(res))
  tmp=res.copy()
  for j in range(26**2):
    for c,v in G[j]:
      tmp[v]=max(tmp[v],res[j]+c)
  if res!=tmp: ans='Infinity'
  print(ans)