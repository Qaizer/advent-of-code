import re

with open('input', 'r') as file:
    lines = file.readlines()
    
transposed = [list(row) for row in zip(*map(lambda line: re.split(r"\s{1,}", line), lines))]
result = sum(int(item) * transposed[1].count(item) for item in transposed[0])
    
print(result)







