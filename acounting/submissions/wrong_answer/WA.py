#! /usr/bin/env python3

n = int(input())
A = map(int, input().split())
prod = 1
for x in A:
    prod *=x
print(prod)