from  itertools import permutations
str,per=input().split()
lis=sorted(''.join(i) for i in permutations(str,int(per)))
for k in lis:
    print(k)

# SMART SOLUTIONS
s="HACK"
n=2
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
print