temperatures = [30, 32, 29, 35, 31, 28, 34, 33, 36, 30,
                27, 31, 32, 37, 29, 34, 35, 28, 33, 31,
                30, 36, 32, 29, 38, 34, 31, 27, 35, 33]

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)temperatures = [30, 32, 29, 35, 31, 28, 34, 33, 36, 30,
                27, 31, 32, 37, 29, 34, 35, 28, 33, 31,
                30, 36, 32, 29, 38, 34, 31, 27, 35, 33]

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)