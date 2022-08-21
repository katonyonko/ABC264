import io
import sys

_INPUT = """\
6
3 5
4 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  R,C=map(lambda x:int(x)-1,input().split())
  if min(R,14-R,C,14-C)%2==0: print('black')
  else: print('white')