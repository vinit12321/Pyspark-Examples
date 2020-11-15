setA=set(map(int,input().split()))
n=int(input())
flag=True
for _ in range(n):
    setn=set(map(int,input().split()))
    if not setA.issuperset(setn):
        flag=False
    
print(flag) 

