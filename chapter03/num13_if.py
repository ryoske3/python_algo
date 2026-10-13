n = int(input())
a = [int(input()) for x in range(n)]

'''
if 0 in a:
    print("NO")
else:
    print("YES")
'''

x = 1
for ele in a:
    x *= ele

if x == 0:
    print("NO")
else:
    print("YES")
