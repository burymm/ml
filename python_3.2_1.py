import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # print('human' in line)
    if 'human' in line:
        line = line.replace('human', 'computer')
    print(line)
