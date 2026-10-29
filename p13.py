numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Ascending order:", numbers)

numbers.sort(reverse=True)

print("Descending order:", numbers)