__author__ = 'knedlus'


import os

# Calculator

# Functions ############################################################################

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y


# Input ############################################################################

def main():

    while True:
        try:
            user_input = int(raw_input("""Welcome to simple calculator, please choose your operation.\n
    1. Add two numbers
    2. Substract two numbers
    3. Divide two numbers
    4. Multiply two numbers\n
    Option: """))

        except ValueError:
            print "Please choose your operation by typing a number in front of the chose option!"
            continue

        if user_input < 1 or user_input > 4:
            print "Please choose your operation with one of the given numbers!"

        else:
            while True:
                try:
                    numberX = float(raw_input("\nPlease enter your first number: "))
                    numberY = float(raw_input("Please enter your second number: "))

                except ValueError:
                    print  "\nYou must enter integer or float number!"
                    continue

                if user_input == 1:
                    print """\nYou chose operation Add.
Number %.01f + Number %.01f = %.01f""" %(numberX, numberY, add(numberX,numberY))
                    break

                elif user_input == 2:
                    print """\nYou chose operation Substract.
Number %.01f - Number %.01f = %.01f""" %(numberX, numberY, substract(numberX,numberY))
                    break

                elif user_input == 3:
                    print """\nYou chose operation Divide.
Number %.01f / Number %.01f = %.01f""" %(numberX, numberY, divide(numberX,numberY))
                    break

                elif user_input == 4:
                    print """\nYou chose operation Multiply.
Number %.01f * Number %.01f = %.01f""" %(numberX, numberY, multiply(numberX,numberY))
                    break

            while True:
                proceed = raw_input("""Do you want to perfrom another operation?
                Type 'y' for yes or 'n' for no.""").upper()

                if proceed == "Y":
                    break

                elif proceed == "N":
                    print "Thank you for using our calculator!\nBye!"
                    return

                else:
                    print "You chose an invalid option!\nTry again!"
                    continue


if __name__ == "__main__":
    main()