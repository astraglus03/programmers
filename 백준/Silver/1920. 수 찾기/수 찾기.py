import sys

first_input = int(sys.stdin.readline())
first_output = set(list(map(int, sys.stdin.readline().split())))
second_input = int(sys.stdin.readline())
second_output = list(map(int, sys.stdin.readline().split()))

for i in second_output:
    print(1 if i in first_output else 0)