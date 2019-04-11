"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# No setup
#repeat forever:
    #read input
    #tokenize input
    #if the first token is "q":
        #quit
   # else:
        #decide which math function to call based on first token



def evaluate_input():    
    while True:
        num_input = input("> ")
        token = num_input.split(" ")
        sign = token[0]
        if sign == 'q':
            break
        if len(token)<2:
            print("Invalid. Please try again.")
        elif len(token) == 3:
            if(sign == "+"):
                print(add(int(token[1]), int(token[2])))
            elif (sign == "-"):
                print(subtract(int(token[1]),int(token[2])))
            elif(sign == "*"):
                print(multiply(int(token[1]),int(token[2])))
            elif(sign == "/"):
                print(divide(int(token[1]),int(token[2])))
            elif (sign == 'power'):
                print(power(int(token [1]), int(token[2])))
            elif (sign == 'mod'):
                print(mod(int(token[1]), int(token[2])))
            else:
                print ("Invalid. Please try again.")
        elif len(token) == 2:
            if(sign == 'square'):
                print(square(int(token[1])))
            elif(sign == 'cube'):
                print(cube(int(token[1])))
            else:
                print("Invalid. Please try again.")



evaluate_input()



#do_setup()
#while exit_condition_not_reached:
    #input = consume_input()
    #output = evaluate_input(input)
    #print(output)