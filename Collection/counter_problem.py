from collections import Counter
no_of_shoes = int(input())
shoes_size = list(map(int, input().split()))
print(shoes_size)
no_of_cust = int(input())
shoes = Counter(shoes_size)
total = 0
for _ in range(no_of_cust):
    quant, price = map(int, input().split())
    if shoes[quant] > 0:
        shoes[quant] -= 1
        total = total+price

print(total)
