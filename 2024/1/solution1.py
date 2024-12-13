import re

with open('2024/1/input', 'r') as file:
    lines = file.readlines()

transposed = [list(row) for row in zip(*map(lambda line: re.split(r"\s{1,}", line), lines))]
transposed[0].sort()
transposed[1].sort()
result = sum(abs(int(transposed[0][i]) - int(transposed[1][i])) for i in range(len(transposed[0])))
    
print(result)