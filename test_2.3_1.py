from itertools import takewhile

def primes(*args):
    a = 1
    primeArray = [1]
    while True:
        devCount = 0
        for i in range(len(primeArray)):
            if a != 1 and a % primeArray[i] == 0:
               devCount += 1
        if devCount == 1:
            primeArray.append(a)
            a += 1
            yield primeArray[-1]
        else:
            a += 1

# print(list(takewhile(lambda x : x <= 31, primes())))
yo = primes()
for i in range(15):
    print (next(yo))