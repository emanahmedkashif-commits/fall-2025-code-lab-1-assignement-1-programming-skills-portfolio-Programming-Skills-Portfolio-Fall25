def even_or_odd(value):                              # Defines the even/odd function. 
    if value % 2 ==0 :                               # Creates an if-statement for determining an even value.
        return (f"The value {value} is even.")       # Condition to return the function.
    else:
        return (f"The value {value} is odd.")        # Else condition to return the function.

def ask():                                           # Defines the question function.
    question = (int(input("Enter a digit: ")))       # Asks a question.

    answer = even_or_odd(question)                   # Calls the even/odd function. 

    print (answer)                                   # Displays the answer to the question.

ask()                                                # Calls the function to ask the question.
    
