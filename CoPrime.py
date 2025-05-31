import math
def gcd(a, b):
    return math.gcd(a, b)
def coprime(numbers):
    if not isinstance(numbers, list) or len(numbers) != 3:
        return False
    a, b, c = numbers

    if gcd(a, b) == 1 and gcd(a, c) == 1 and gcd(b, c) == 1:
        return True
    else:
        return False

list1 = []
for i in range(1,4):
    a=int(input("Enter Number {} :".format(i)))
    list1.append(a)

print(f"{list1} co-prime: {coprime(list1)}")