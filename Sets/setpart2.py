#main code
n=int(input())
countryset=set()
for i in range(n):
    name=input()
    countryset.add(name)
print(len(countryset))

#one line code
print(len(set([str(input()) for x in range(int(input()))])))

