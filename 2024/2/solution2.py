import re

with open('2024/2/input', 'r') as file:
    lines = file.readlines()

    safe_count = 0
    for line in lines:
        report = list(map(int, line.split()))
        differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
        if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
            safe_count += 1

print(safe_count)