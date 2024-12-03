"""
This example data contains six reports each containing five levels.
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

--- PART TWO ---
Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
More of the above example's reports are now safe:
7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!
"""

file = open("input.txt").read().strip()
lines = file.split("\n")

pt1, pt2 = 0, 0

def isSafe(r):
    incr = True if int(r[1]) > int(r[0]) else False
    diffs = [1,2,3] if incr else (-1,-2,-3)

    for i in range(1, len(r)):
        if int(r[i]) - int(r[i-1]) not in diffs:
            return False
    return True

for line in lines:
    report = line.strip().split()
    
    if isSafe(report):
        pt1 += 1
    else:
        for i in range(len(report)):
            new_report = report.copy()
            del(new_report[i])
            if isSafe(new_report):
                pt2 += 1
                break

print("Answer pt1: ",pt1 , " - Answer pt2: ",pt1+pt2)
