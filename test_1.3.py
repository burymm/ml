def closest_mod_5(x):
    for y in range(x, x + 5):
        if y % 5 == 0:
            return y
    return "I don't know :("


print ('input x')
# x = int(input())
print(closest_mod_5(int(input())))    
