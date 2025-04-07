#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

with open('numbers.txt', 'r') as file:
    # Read all lines in the file
    numbers = file.readlines()

numbers = [int(num.strip()) for num in numbers]

count = len(numbers)
total = sum(numbers)
average = total / count if count > 0 else 0
highest = max(numbers)
lowest = min(numbers)

print(f"How many numbers: {count}")
print(f"Total of all the numbers: {total}")
print(f"Average: {average:.2f}")
print(f"Highest number: {highest}")
print(f"Lowest number: {lowest}")
