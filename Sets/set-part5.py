val = int(input())
setA = set(map(int, input().split()))

n = int(input())

for i in range(n):
    
    comm, ve = input().split()
    setB = set(map(int, input().split()))

    if comm == 'intersection_update':
        setA.intersection_update(setB) #intersection between two sets but stored the value in first set mutualble

    elif comm == 'update':
        setA.update(setB) #update between two set but stored value in first set

    elif comm == 'difference_update':
        setA.difference_update(setB) # took differnce between two sets and stored them in first one

    elif comm == 'symmetric_difference_update':
        setA.symmetric_difference_update(setB)
    
print(sum(setA))