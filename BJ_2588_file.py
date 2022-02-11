i = "472\n385"
print(i.split("\n"))

# . splitlines()

num1 = input()
num2 = input()

numList = [num1, num2]

num1 = int(numList[0])
num2 = numList[1]

num3 = num1 * int(num2[len(num2)-1])
num4 = num1 * int(num2[len(num2)-2]) * 10
num5 = num1 * int(num2[len(num2)-3]) * 100

num6 = num3 + num4 + num5
# print(num1, num2, num3)
print(num3)
print(int(num4/10))
print(int(num5/100))
print(num6)