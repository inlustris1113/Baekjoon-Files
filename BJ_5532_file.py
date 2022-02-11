import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input()) # 좀더 간결하게 바꾸기.

# print(int(math.ceil(8.0)))
# print(int(math.ceil(8.1)))


# print("A/C 값: ", A/C, type(A/C))
# print("B/D 값: ", B/D, type(B/D))

# A/C 값:  4.166666666666667 <class 'float'>
# B/D 값:  3.75 <class 'float'>

print(L - max(math.ceil(A/C),math.ceil(B/D)))
# else:
#    print(L - max(int(A / C), int(B / D)))

