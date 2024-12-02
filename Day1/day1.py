"""
For example:

3   4
4   3
2   5
1   3
3   9
3   3

In the example list above, the pairs and distances would be as follows:
The smallest number in the left list is 1, and the smallest number in the right list is 3. 
The distance between them is 2.
To find the total distance between the left list and the right list, add up the distances between 
all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!
"""

# ********** #

col1, col2 = [], []

with open("input.txt") as file:
    for line in file:
        col1.append(int(line.split("   ")[0]))
        col2.append(int(line.split("   ")[1].replace("\n", "")))

col1.sort()
col2.sort()

dist = []
for i in range(len(col1)):
    if col1[i] > col2[i]:
        dist.append(col1[i] - col2[i])
    else:
        dist.append((col1[i] - col2[i]) * -1)

print(sum(dist))

sim = []
for n in col1:
    sim.append(n * col2.count(n))

print(sum(sim))