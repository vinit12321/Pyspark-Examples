#from sortedcontainers import SortedList, SortedSet, SortedDict 
str1="BAANANAS"
staurt=set()
kevin=set()

for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        if str1[i] in ('A','E','I','O','U'):
            kevin.add(str1[i:j])
        else :
            staurt.add(str1[i:j])

def count_substr(str,sub):
    start=0
    count=0
    while start<len(str):
        pos=str.find(sub,start)
        if pos !=-1  :
            start=pos+1
            count+=1
        else :
            break
    return count


staurt_score=[count_substr(str1,n) for n in staurt]
kevin_score=[count_substr(str1,k) for k in kevin]
#print(staurt)
#print(kevin)
if sum(staurt_score)>sum(kevin_score):
    print("Stuart",sum(staurt_score))
elif sum(staurt_score)<sum(kevin_score):
    print("Kevin",sum(kevin_score))
else:
    print("Draw")


