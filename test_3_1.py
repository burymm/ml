s = input()
a = input()
b = input()

count = 0
for i in range(1000):
    if a in s:
        count += 1
        s = s.replace(a, b)
    else:
        break

if a in s:
    print("Impossible")
else:
    print(count)