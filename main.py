a = input()
b = int(a.split()[0])
c = int(a.split()[1])

bn = True
result = b // 2


if b % 2 == 0:
    if c % 2 == 0:
        v = c // 2
    else:
        v = c // 2 + 1
    result = result*v
else:
    result += 1
    if c % 2 == 0:
        v = c//2
    else:
        v = c//2+1
    result = result*v
if bn:
    print(result)
