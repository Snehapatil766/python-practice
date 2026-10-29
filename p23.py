numbers = [10, 20, 10, 30, 20, 10, 40]

for num in numbers:
    if numbers.index(num) == numbers.index(num):
        if num not in numbers[:numbers.index(num)]:
            print(num, ":", numbers.count(num))