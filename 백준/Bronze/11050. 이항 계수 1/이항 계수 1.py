def bio_coef(n,k):
    if k==0 or n==k:
        return 1
    else:
        return bio_coef(n-1,k-1) + bio_coef(n-1,k)

a,b = map(int,input().split())

print(bio_coef(a,b))