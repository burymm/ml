import sys
import re

pattern = r"\b[aA]+\b"
#There’ll be no more "Aaaaaaaaaaaaaaa"
#AaAaAaA AaAaAaA

for line in sys.stdin:
    line = line.rstrip()
    # print(re.search(pattern, line).group())
    # print(re.search(pattern, line))
    # print(re.match(pattern, line))
    if re.search(pattern, line).group():
        line = re.sub(pattern, 'argh', line, 1)
    print(line)
