name = input("Enter your full name: ")   # Created a variable "name".
hometown = input("Enter your hometown: ")   # Created a variable "hometown".
age = int(input("Enter your age: "))   # Created a variable "age".

information = {   # Created a dictionary to store this information.
    "name" : name,
    "hometown" : hometown,
    "age" : age
}


print (f"{information["name"]}\n{information["hometown"]}\n{information["age"]}")   # Displays this information.






