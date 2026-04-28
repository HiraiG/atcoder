import sys
A, B, C, X = map(int, sys.stdin.read().split())

count = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1): 
            500*i + 100*j + 50*k == X

print(A, B, C, X)
