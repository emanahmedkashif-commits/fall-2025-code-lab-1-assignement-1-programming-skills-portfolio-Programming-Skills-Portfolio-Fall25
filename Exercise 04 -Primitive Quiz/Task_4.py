capitals = {                                                # Created a dictionary to store information.
    "France" : "Paris",
    "Netherlands" : "Amsterdam",
    "Greece" : "Athens",
    "Ireland" : "Dublin",
    "Italy" : "Rome",
    "Ukraine" : "Kyiv",
    "Denmark" : "Copenhagen",
    "Germany" : "Berlin",
    "Azerbaijan" : "Baku",
    "Switzerland" : "Bern"
}

for country, capital in capitals.items():                     # Creates a for loop.
    answer = input(f"What is the capital of {country}? \n")   # Creates a variable to ask a question.
    if answer.lower() == capital.lower():                     # Ignores capitalization, therefore any version of "paris" is accepted.
        print ("Your answer is correct!")                     # Displays the conditions.
    else:
        print ("Wrong answer!")                               # Displays the final else conditon.

