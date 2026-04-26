# atcoder practice

# NとMを読み込む
N, M = map(int, input().split())

# 服のリスト F を読み込む
F = list(map(int, input().split()))

# 質問 1: N 人全員が異なる種類の服を着ていますか？
# diff = 1 - (1/M)^(N - 1)
diff = set(F)


print(diff)
print("\n")
