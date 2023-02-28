#! /usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
out = 0
for i in A:
    out += A[i]
print(out)
