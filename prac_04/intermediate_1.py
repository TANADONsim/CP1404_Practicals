numbers = []
for number in range(5):
    number = int(input("Enter number:"))
    numbers.append(number)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The biggest number is", max(numbers))
print("The average number is", sum(numbers)/len(numbers))
