import io
import sys

_INPUT = """\
6
3 4
4 3 5
2 6 7 4
0100
1011
1010
15 20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78
39 97 12 53 62 32 38 84 49 93 53 26 13 25 2 76 32 42 34 18
01011100110000001111
10101111100010011000
11011000011010001010
00010100011111010100
11111001101010001011
01111001100101011100
10010000001110101110
01001011100100101000
11001000100101011000
01110000111011100101
00111110111110011111
10101111111011101101
11000011000111111001
00011101011110001101
01010000000001000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def min2(a,b):
      if a==-1: return b
      else: return min(a,b)
  inf=-1
  H,W=map(int,input().split())
  R=list(map(int,input().split()))
  C=list(map(int,input().split()))
  A=[list(map(int,list(input()))) for _ in range(H)]
  dp=[inf]*(H*W*4)
  dp[0]=0
  dp[1]=R[0]
  dp[2]=C[0]
  dp[3]=R[0]+C[0]
  for i in range(H):
      for j in range(W):
          for k in range(4):
              p=4*W*i+4*j+k
              if i<H-1:
                  t=A[i][j]^A[i+1][j]^(k&1)
                  m=4*W*(i+1)+4*j+(k&2)+t
                  if t==0: dp[m]=min2(dp[m],dp[p])
                  else: dp[m]=min2(dp[m],dp[p]+R[i+1])
              if j<W-1:
                  t=A[i][j]^A[i][j+1]^((k>>1)&1)
                  m=4*W*i+4*(j+1)+(t<<1)+(k&1)
                  if t==0: dp[m]=min2(dp[m],dp[p])
                  else: dp[m]=min2(dp[m],dp[p]+C[j+1])
  print(min(dp[-4:]))