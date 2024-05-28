# Assignment 1 - Fence Cost Calculator
# Author: Ethan du Toit
# Version: V3.1

print() 
# Greets the user
print("🎉 WELCOME TO THE FENCE COST CALCULATOR! 🎉\n")

print("Please enter your width, length & cost per metre values of your fence into the calculator: \n")

# Variable which will loop the program if the user requests to at the end
keep_going = ""
while keep_going == "":

    # Function which lets user input values and then checks that the number is more than zero.
    def error_checker(question):
        done = False
        error = "Please enter a valid number (must be an integer than zero)"
        while not done:
            print(question)
            try:
                num = float(input())
                if num > 0:
                    done = True
                else:
                    print(error)
            except ValueError:
                print(error)
        return(num)

    # Asks user to input width value
    width = error_checker("Step 1: Please enter your WIDTH value (in metres): ")
    print()
    print(f"⚪️ The width you entered is {width}m.\n")

    # Asks user to input length value
    length = error_checker("Step 2: Please enter your LENGTH value (in metres): ")
    print()
    print(f"⚪️ The length you entered is {length}m.\n")

    # Asks user to input cost per metre value
    costpm = error_checker("Step 3: Please enter your COST PER METRE value: ")
    print()
    print(f"⚪️ The cost per metre value you entered is ${costpm}.\n \n -------------- \n") #\n is for visual gaps

    # Calculates perimeter and overall cost (using perimeter and cost per metre values)
    perimeter = 2 * (width + length)
    fencecost = perimeter * costpm

    # Outputs the perimeter and overall cost to build the fence
    print(f"The perimeter of your fence is {perimeter}m. \n")
    print(f"The cost to build your fence will be ${fencecost}. \n")

    # Check whether user would like to complete another calculation or exit the program
    keep_going = input("Press enter to complete another calculation, or any other key to end the program. ") # Loops program if requested

# If user exits, thank them for using the program
print("\n \n \n🎉 THANK YOU FOR USING THE FENCE COST CALCULATOR! 🎉 ")


