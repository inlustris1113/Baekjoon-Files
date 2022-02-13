# Problem: BJ 1964번
# Date: 2022.02.11일.
# Time: 15분
# Level: Bronze III

def sum1(num):
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    return sum

level = int(input())
num = 5*sum1(level) - level*level +1
print(num % 45678)

# print(1000005 % 100)

# listN = [num in range(level)]
# print(sum(listN))










