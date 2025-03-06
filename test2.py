objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
# objects = [1, 2, 3, 1, 2]

ans = 0
immutable = []
for obj in objects: # доступная переменная objects
    if not (obj in immutable):
    	ans += 1
    	immutable.append(obj)

print(ans)