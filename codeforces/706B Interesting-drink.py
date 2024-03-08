from bisect import bisect_right

def drink(shops, amount):
    return  bisect_right(shops, amount)
   
n = int(input())
shops = list(map(int, input().split()))
shops.sort()

for _ in range(int(input())):
    amount = int(input())
    print(drink(shops, amount))