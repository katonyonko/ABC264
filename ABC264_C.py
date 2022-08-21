import io
import sys

_INPUT = """\
6
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19
3 3
1 1 1
1 1 1
1 1 1
1 1
2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import combinations
  H1,W1=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(H1)]
  H2,W2=map(int,input().split())
  B=[list(map(int,input().split())) for _ in range(H2)]
  ans='No'
  for k1 in combinations(range(H1),H2):
    for k2 in combinations(range(W1),W2):
      flag=0
      for i in range(H2):
        for j in range(W2):
          if A[k1[i]][k2[j]]!=B[i][j]: flag=1
      if flag==0:
        ans='Yes'
  print(ans)