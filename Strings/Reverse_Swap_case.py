import re


str="aWSEOME IS Coding"
print(''.join(re.split(r"(\s+)",str.swapcase())[-1::-1]))