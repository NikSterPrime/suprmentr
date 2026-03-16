name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")
category = ""
if age<=12:
    category = "a Child"
elif age<=19:
    category = "a Teenager"
if age<=59:
    category = "an Adult"
else:
    category = "a Senior Citizen"

print(f"Hello, {name}. You are {category} who is {age} years old, and loves to {hobby}.")
