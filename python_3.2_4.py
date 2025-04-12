import sys
import re

pattern = r"(\w)\1{1,}"

# attraction
# buzzzz
# mewmewNnyaaa

for line in sys.stdin:
    line = line.rstrip()
    # print(re.search(pattern, line).group())
    # print(re.search(pattern, line))
    # print(re.match(pattern, line))
    # print(re.findall(pattern, line))
    # print(re.sub(pattern, r'\2\1\3', line))
    line = re.sub(pattern, r'\1', line)
    print(line)
