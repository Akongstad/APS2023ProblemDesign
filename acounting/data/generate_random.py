#! /usr/env/python3

import random
import sys

random.seed(int(sys.argv[-1])) 

n = random.randrange(3, 200000)
print(n)

for _ in range(n):
    print(random.randrange(-10000, 10000), end=" ")