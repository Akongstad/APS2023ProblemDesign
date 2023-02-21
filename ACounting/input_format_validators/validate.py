import sys
import re

firstline = sys.stdin.readline()
assert re.match(r"(0|-?[1-9][0-9]*) \n", firstline), firstline

n = map(int, firstline.split())
assert 2 < n < 200001

secondline = sys.stdin.readline()
assert re.match(r"(0|-?[1-9][0-9]*)* \n", secondline), secondline

array = secondline.split()

for number in range(array):
    assert -10001 < number < 10001

assert sys.stdin.readline() == ""

sys.exit(42)