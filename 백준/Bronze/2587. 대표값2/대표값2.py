b = []
total =0
for i in range(0,5):
    a = int(input())
    b.append(a)
    total+=a
b.sort()
temp = int(len(b)/2)
print(int(total/5))
print(b[temp])