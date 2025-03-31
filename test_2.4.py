with open('input.txt') as f, open('output.txt', 'w') as w:
    file = []
    for line in f:
        file.append(line.rstrip())
    i = len(file) - 1
    while i >= 0:
        w.write(file[i] + '\n')
        i -= 1