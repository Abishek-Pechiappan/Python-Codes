#Greedy
coins = [1, 50, 500, 20, 5, 2, 100, 200, 10]
coins.sort()
amount = int(input("Enter the amount : "))
while amount > 0:
    for coin in reversed(coins):
        if amount >= coin:
            print(coin, end=' ')
            amount -= coin
            break

