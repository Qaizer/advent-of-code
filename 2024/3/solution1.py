import re

with open('input', 'r') as file:
    file_content = file.read()

pattern = r"mul\(\d{1,3}\,\d{1,3}\)"
matches = re.findall(pattern, file_content)
sum = 0
for match in matches:
    print(match)
    nums = re.findall(r"\d{1,3}", match)
    print(nums)
    sum += int(nums[0]) * int(nums[1])
print(sum)





