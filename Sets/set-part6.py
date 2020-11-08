from collections import Counter
a=int(input())
k=Counter(map(int,input().split()))
for l,m in k.items():
    if m==1:
        print(l)

        #counter function will take as set and also in built function has two function items() which will stored data as 
        #key and value pair.Key will be the record from set and Value will be number of times recordrs get repeated.


