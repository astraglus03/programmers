import string

a = str(input())
time=0
alphabet = string.ascii_uppercase

for i in a:
    if(ord(i)>=65 and ord(i)<68):
        time+=2
    if(ord(i)>=68 and ord(i)<71):
        time+=3
    if(ord(i)>=71 and ord(i)<74):
        time+=4
    if(ord(i)>=74 and ord(i)<77):
        time+=5
    if(ord(i)>=77 and ord(i)<80):
        time+=6
    if(ord(i)>=80 and ord(i)<84):
        time+=7
    if(ord(i)>=84 and ord(i)<87):
        time+=8
    if(ord(i)>=87 and ord(i)<91):
        time+=9

print(time+len(a))
