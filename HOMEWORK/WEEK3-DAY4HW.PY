import re

with open('regex_test.txt') as f:
    names_data = f.readlines()

pattern = re.compile(r'^([A-Z][a-z]+)\s+([A-Z][a-z]+),\s+(\d+),\s+(.*)$')

for line in names_data:
    match = pattern.match(line.strip())
    if match:
        last_name = match.group(2)
        age = match.group(3)
        country = match.group(4)
        print(f"{last_name}, {age}, {country}")
        print(f"Age: {age}, Country: {country}")
    else:
        print("invalid")
