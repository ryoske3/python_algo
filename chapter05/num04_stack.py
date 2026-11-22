n,q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

for _ in range(q):
    query = [int(x) for x in input().split()]

    cmd = query[0]
    if cmd == 0:
        #append
        a.append(query[1])
    elif cmd == 1:
        #pop
        a.pop()
    else:
        #print
        print(" ".join(map(str,a)))
