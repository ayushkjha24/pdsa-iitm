#simple recursive
def fibrec(n):
    if n <= 1:
        return n 
    return fibrec(n - 1) + fibrec(n - 2)

# memoization topdown
memo ={}
def fibmem(n):
    if n <= 1:
        memo[n] = n
    if n not in memo:
        memo[n] = fibmem(n-1) + fibmem(n-2)
    return memo[n]

# DP tabulation bottom up
def fibtab(n):
    T = [0] * (n + 1)
    T[1] = 1
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]


n=int(input())
import time
t1 = time.perf_counter()
res1 = fibrec(n)
ft1 = time.perf_counter() - t1

t1 = time.perf_counter()
res2 = fibmem(n)
ft2 = time.perf_counter() - t1

t1 = time.perf_counter()
res3 = fibtab(n)
ft3 = time.perf_counter() - t1

print(res1,ft1)
print(res2,ft2)
print(res3,ft3)