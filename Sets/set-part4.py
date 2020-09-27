a= int(input())
seta= set(input().split())
b= int(input())
setb= set(input().split())

print(len(seta.intersection(setb))) # comman betwen two set
print(len(seta.union(setb))) # union unique betwen two set 
print(len(seta.difference(setb))) # present in first set but not is second set
print(len(seta.symmetric_difference(setb))) #All elements excepts command elements form both set
