a= int(input())
seta= set(input().split())
b= int(input())
setb= set(input().split())

print(len(seta.intersection(setb)))
print(len(seta.union(setb)))
print(len(seta.difference(setb)))