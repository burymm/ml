import sys
import re

pattern = r"(.*)\b(^[A-Za-z0-9]+)\2\b\1"
# pattern = r".*\\.*"
# pattern = r"(.)*(z)(.{3})\2\1*"
# pattern = r"([\w \.\"\?\!])*\bcat\b\1*"
# pattern = r"(cat)([\w \.])*\1"

for line in sys.stdin:
    line = line.rstrip()
    # print(re.search(pattern, line).group())
    if re.match(pattern, line) is not None:
        print(line)
    # process line