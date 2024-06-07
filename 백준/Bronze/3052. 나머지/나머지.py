a=[]

for i in range(10):
    b = int(input())
    a.append(b%42)

list1 = set(a)
list2 = list(list1)
print(len(list2))