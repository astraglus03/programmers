a = input().strip()
dict1 = set()

for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        dict1.add(a[i:j])

print(len(dict1))