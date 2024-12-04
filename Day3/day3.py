"""
Day 3: Mull It Over
---FIRST PART ---
For example, consider the following section of corrupted memory:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up 
the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
"""
import re

data = open("input.txt").read().strip()
muls = re.findall(r"mul\(\d+,\d+\)", data)
add = 0

for mul in muls:
    nums = list(map(int, mul.replace("mul(", "").replace(")","").split(",")))
    add += (nums[0] * nums[1])
print(add) # 166630675


""" SECOND PART 
There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
data = open("input.txt").read().strip()
muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
add = 0

able = True
for mul in muls:
    if mul == "do()":
        able = True
    elif mul == "don't()":
        able = False
    else:
        if able:
            nums = list(map(int, mul.replace("mul(", "").replace(")","").split(",")))
            add += nums[0] * nums[1]

print(add)

