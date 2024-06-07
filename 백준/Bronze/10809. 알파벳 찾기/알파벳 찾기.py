a = str(input()).lower()
b=[-1]*26

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for index,char in enumerate(a):
    if char in alphabet:
        c = ord(char)-97
        if(b[c]==-1):
            b[c] =index
for i in b:
    print(i, end=' ')