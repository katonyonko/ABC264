import io
import sys

_INPUT = """\
6
3 6
4 4
1 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  L,R=map(int,input().split())
  print('atcoder'[L-1:R])