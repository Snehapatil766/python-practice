marks = [75, 80, 65, 90, 55, 88, 72, 60, 95, 45,
         78, 82, 69, 91, 50, 85, 74, 67, 93, 58]

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

average = sum(marks) / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Above average:", above)
print("Below average:", below)