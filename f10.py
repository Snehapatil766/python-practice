def largest(numbers):
    result = numbers[0]
    for n in numbers:
        if n > result:
            result = n
    return result

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))