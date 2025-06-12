import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().strip().split()))

set_lst = set(b)
sorted_set = sorted(set_lst)
tmp_dict = dict()

for i in range(len(sorted_set)):
    tmp_dict[sorted_set[i]]= i

for i in b:
    print(tmp_dict[i],end=' ')
