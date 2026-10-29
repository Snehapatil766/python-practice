scores = [45, 110, 75, 20, 95, 55, 120, 30, 80, 100]

print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Total runs:", sum(scores))
print("Average runs:", sum(scores) / len(scores))

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif 50 <= score <= 99:
        half_centuries += 1

print("Centuries:", centuries)
print("Half-centuries:", half_centuries)