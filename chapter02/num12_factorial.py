n = int(input())
number_of_permutation = 1

for i in range(1, n + 1):
    number_of_permutation *= i

print(number_of_permutation)
