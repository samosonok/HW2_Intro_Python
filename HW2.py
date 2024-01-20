# assign a variable with user input
user_input = input("Please enter 4-digit number: ")

# convert user input first to float and then to int value
int_number = int(float(user_input))

# assign each variable with calculated value using floor division and modulo operator
first_number = int_number // 1000
second_number = (int_number % 1000) // 100
third_number = (int_number % 100) // 10
forth_number = int_number % 10

# print each number
print(first_number)
print(second_number)
print(third_number)
print(forth_number)

# My first attempt
# first_number = int_number // 1000
# second_number = (int_number - (first_number * 1000)) // 100
# third_number = (int_number - (first_number * 1000) - (second_number * 100)) // 10
# forth_number = int_number - (first_number * 1000) - (second_number * 100) - (third_number * 10)
