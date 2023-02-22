#! /usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
x = A.pop(0)
sum_in_unary = '1'*x
for i in range(len(A)):
    i_in_unary = '1'*A[i]
    if i == 0:
        i_in_unary = list(i_in_unary)
        while len(i_in_unary):
            sum_in_unary += i_in_unary.pop()
    else:
        while len(i_in_unary):
            j_in_unary = list('1' * A[i-1])
            sum_in_unary += j_in_unary.pop()
print(len(sum_in_unary))