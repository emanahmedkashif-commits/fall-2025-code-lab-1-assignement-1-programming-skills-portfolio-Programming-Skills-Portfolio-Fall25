password = "12345"                                               # Creates a variable to store the correct password.
attempts = 5                                                     # Creates the attempt limit.

while attempts > 0:                                              # Creates a while loop prior to any attempt.
    answer = input("Enter your password: ")                      # Variable to ask the user to enter their password.
    if answer == password:                                       # Creates an if-statement for the correct or wrong password.
        print ("Access granted!")
        break
    else:
        attempts -=1                                             # Condition in case of wrong password entered.
        if attempts > 0:
            print (f"Incorrect password. Please try again. You have {attempts} attempts remaining.")
        else:
            print ("Device disabled!")                           # Final decision for the wrong password.