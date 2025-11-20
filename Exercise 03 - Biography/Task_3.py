name = input("Enter your full name: ")           # Created a variable "name".
hometown = input("Enter your hometown: ")        # Created a variable "hometown".

while True:                                      # Continue the statement if true.
        age_ask = input("Enter your age: ")      # Created a variable "age".

        if age_ask.isdigit():                    # Continue if the age is a digit.
         age = int(age_ask)
         break
        else:
          print ("Please type a numerical.")     # Display if a sring has been typed.
        age = None

information = {                                  # Created a dictionary to store this information.
    "name" : name,
    "hometown" : hometown,
    "age" : age
}

if age is not None:
    print (f"{information["name"]}\n{information["hometown"]}\n{information["age"]}")   # Displays this information.
