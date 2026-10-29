salaries = [25000, 35000, 60000, 75000, 28000, 45000, 90000, 20000]

print("Highest salary:", max(salaries))
print("Lowest salary:", min(salaries))
print("Average salary:", sum(salaries) / len(salaries))

above = 0
below = 0

for salary in salaries:
    if salary > 50000:
        above += 1
    if salary < 30000:
        below += 1

print("Employees earning above 50000:", above)
print("Employees earning below 30000:", below)