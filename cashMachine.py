######################################################################
#                                                                    #
#                              Variables                             #
#                                                                    #
######################################################################
loop = bool (True)
balance = float(100)
######################################################################
#                                                                    #
#                        Functions/Loops                             #
#                                                                    #
######################################################################
#This function is just to make the program easier to rad as it looks
#nice and seperates each section.
def header():
    print("===========================================================")

#This function will display the current balance which will use the
#variable "balance" to display the correct numbers.
def view():
    header()
    print("Current balance: £",balance)

#This is a while loop inside of a function which means that if the "depInput"
#is greater than 300 it will do the actions (print) what are below 
#and if it is less than or equal to 300 then it will do the actions
#(calculations & print). At the start there is a global variable which
#gets the value from the value at the top and it allows it to be used within this function.
def deposit():
    global balance 
    header()
    print("All deposits must be under or equal to £300")
    print("How much do you want to deposit?")
    depInput = int(input())
    while depInput > 300: 
        print("You can only deposit £300 or less")
        print("Your current balance is", balance )
        print("How much do you want to deposit?")
        depInput = int(input())
    if depInput <= 300:
        balance = depInput + balance
        print("£",depInput, "has been added to your account")
        print("You balance is £",balance)

#This is a while loop inside of a function which means that if the "withInput"
#is greater than the balance (balance = float(100)) it will
#do the actions (print & ask for user input) what are below and if it is less
#than or equal to balance (balance = float(100))
#then it will do the actions (calculations & print).
def withdraw():
    global balance
    header()
    print("How much do you want to withdraw?")
    withInput = input()
    while withInput > balance:
        print("You can only withdraw your current balance or less")
        print("Your current balance is", balance )
        print("How much do you want to withdraw?")
        withInput = input()
    if withInput <= balance:
        balance = balance - withInput
        print("£",withInput, "has been withdrawn from your account")
        print("You balance is £",balance)

#This is another function which will print out the help messages.
def helpMenu():
    header()
    print("1 = View - This will allow you to see your current balance.")
    print("2 = Deposit - This will allow you to add money into your account.")
    print("3 = Withdraw - This will allow you to take money out of your account.")
    print("4 = Help Menu - This will show you this page.")
    print("5 = Exit - This will quit the program.")

#This function will print out the menu.
def menu():
    header()
    print("1 = View")
    print("2 = Deposit")
    print("3 = Withdraw")
    print("4 = Help Menu")
    print("5 = Exit")

######################################################################
#                                                                    #
#                              Main Loop                             #
#                                                                    #
######################################################################
#This is the main loop which will first welcome the user and if he wants 
#to continue it will carry through the loop else it will quit the program.
print("Welcome to the ATM, do you want to continue")

startInput = input()
while loop == True:
    if startInput.lower() == "yes":
        menu()
    else:
        quit()
    optionInt = input("Choose an option (1-5)")
    if optionInt == "1": 
        view()   
    elif optionInt == "2": 
        deposit()
    elif optionInt == "3": 
        withdraw()
    elif optionInt == "4": 
        helpMenu()
    elif optionInt == "5":
        print("Thank you for using the ATM!")
        quit()
    else:
        header()
        print("Invailid option")
