N = int(input())

A = list(map(int, input().split()))


count = 0

while True:
    flag = False
    for i in range(N):
        if A[i] % 2 != 0:
            flag = True
            break
    
    if flag:
        break

    for i in range(N):
        A[i] = A[i]//2

    count += 1

print(count)    


