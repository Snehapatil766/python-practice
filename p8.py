numbers = [11,22,41,5,62,43,5,83,22,53, 40,50,60,80,70]
even = 0
odd = 0

for num in numbers:
  if num % 2 == 0:
    even += 1
  else:
    odd += 1

print("Even numbers: ",even)
print("Odd numbers: " ,odd)