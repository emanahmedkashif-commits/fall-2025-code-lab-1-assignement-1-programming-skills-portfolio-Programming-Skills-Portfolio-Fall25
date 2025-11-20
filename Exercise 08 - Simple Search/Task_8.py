names = ["Jake" , "Zac", "Ian", "Ron", "Sam", "Dave"]        # Creates a list containing the names.

question = input("Enter the name you are looking for: ")     # Creates a variable to ask the user of the name.

if question.lower() in (name.lower() for name in names) :    # Creates an if statement of whether the name is in the list.
    print (f"{question} is part of the list!")               # Displays the statement from the condition.
else:
    print (f"{question} is not part of the list!") 