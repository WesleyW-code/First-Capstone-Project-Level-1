# Capstone project

# Importing math module:

import math

# Allowing user to chose between investment or bond:
# Printing the choices for the user and giving description of each choice:

choice = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n \ninvestment - to calculate the amount of interest you'll earn on interest\nbond - to calculate the amount you'll have to pay on a home loan\n\nPlease enter your finance option now: ")

# Displaying error message if the user does not enter the selection correctly:

if choice != "investment" and choice != "Investment" and choice != "INVESTMENT" and choice != "Bond" and choice != "bond" and choice != "BOND":
    print("Invalid entry - Please make sure you have spelled your option correctly, only use capitals at the begining or throughout your inputed option.")
    
# If user selects the investment option this formula will run:

elif choice == "investment" or choice == "Investment" or choice == "INVESTMENT":
    money = float(input("\nEnter the amount of money you want to deposit: ")) # Ask the user the amount of money that they are depositing.
    rate = float(input("Enter the percentage interest rate you will be receiving (only the number not the percentage symbol): ")) # Ask the user to enter the interest rate (just the number).
    years = float(input("Enter the number of years you plan to invest for: ")) # Ask the user the number of years they plan to invest.
    interest = input("Do you want 'simple' or 'compound' interest: (Enter simple or compound) ") # Ask user wether they want simple or compound interest.
    conv_rte = rate / 100
    if interest == "simple":
        answer = money*(1 + conv_rte * years) # Formulate the answer.
        print("\nThe amount you will receive after",years,"years, with a simple interest rate of",rate,"percent is: R",round(answer,2)) # Print out the answer.
    elif interest == "compound":
        answer = money * math.pow((1 + conv_rte),years) # Formulate the answer.
        print("\nThe amount you will receive after",years,"years, with a compound interest rate of",rate,"percent is: R",round(answer,2)) # Print out the answer.
    else:
        print("The type of interest has not been selected or typed in correctly!") # Print out error message if 'simple' or 'compound' has not been entered correctly.

# If user selects the bond option this formula will run:

else:
    choice == "Bond" or choice == "bond" or choice == "BOND"
    value = float(input("\nPlease enter the present value of the house: ")) # Ask the user the present value of the house.
    int_rte = float(input("Please enter the interest rate (only the number not the percentage symbol): ")) # Ask the user to enter the interest rate (just the number).
    num_mnths = float(input("Please enter the number of months you plan to take to repay the bond: ")) # Ask the user over how many months they want to repay the bond.
    conv_rte = (int_rte / 100)/12 # Converting the interest rate to monthly by dividing the annual interest rate by 12.
    answer = (conv_rte * value)/(1 - (1 + conv_rte)**(- num_mnths)) # Calculates how much money the user will have to repay each month. 
    print("\nYou will have to pay R",round(answer,2),"every month for the next",num_mnths,"months to pay off your bond.") # Outputs the answer.




    
