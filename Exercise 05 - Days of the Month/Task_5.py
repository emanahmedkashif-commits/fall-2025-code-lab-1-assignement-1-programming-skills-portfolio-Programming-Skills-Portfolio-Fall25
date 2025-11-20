months = {                                                           # Dictionary for the number of days in each month.
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}

month = int(input("Enter the month number from 1-12: "))             # Creates a variable to ask a question (numerical).

if 1<= month <=12:                                                   # Ensures the values entered are between 1 and 12.
    if month ==2:                                                    # Leap year condition.
        leap = (input("Is it a leap year? yes or no?")).strip().lower()
        if leap == "yes":
            print ("Number of days : 29.")
        else:
            print ("Number of days : 28.")                           # Displays a value for the first else statement.
    else:
        print (f"Number of days : {months[month]}")                  # Displays the value from the input from the question regardless of the condition.
else:
    print ("Invalid Number.")                                        # Displays the statement if not matched with the initial condition.
