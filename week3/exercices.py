# Creation Date : 2023-02-25
# Created by : Antoine LeBel

# Multiplication
first_number = input("First number: ")
second_number = input("Second number: ")

result = int(first_number) * int(second_number)
print(result)

# Concatenation
first_name = input("First name: ")
second_name = input("Last name: ")

full_name = first_name + " " + second_name
print(full_name)

# Next letter
# Transform into a number
letter = input("Letter: ")
letter_to_int = ord(letter)

# Add one
new_letter_to_int = letter_to_int + 1
new_letter = chr(new_letter_to_int)
print(new_letter)

# Priority
number = input("Number: ")
result = (int(number) * 3 / 2) + 10
print(int(result))

# Like letters
number = input("Number: ")
print(number + "-" + number) # no need to convert, but needed int(number) * -1 would work

# Hour to seconds
hours = input("Hours: ")
print(int(hours) * 60 * 60)
