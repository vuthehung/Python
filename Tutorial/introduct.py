CURRENT_YEAR = 2022

print("First name: ")
first_name = input()
print("Last name: ")
last_name = input()

print("When you were born?")
year_born = int(input())

age = CURRENT_YEAR - year_born

height = float(input())
name = first_name + " " + last_name
print("Your name is " + name)
print("Your height: " + str(height))
print("Your age: " + str(age))