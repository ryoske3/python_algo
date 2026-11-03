s = input()

li = []
for ele in s:
    if ele not in li:
        li.append(ele)
        print(ele,end="")

