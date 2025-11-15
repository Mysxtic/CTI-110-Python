#Dayvion Peoples
#11/15/25
#P5LAB
#This program will simulate a customer using a self-checkout machine

import random


def disperse_change(change):

    #Converting the value to an interger
    change = round(int(change * 100), 2)

    

    if change == 0:
        print("No Change Due")


    #Determine how many coins are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change // 1

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies >=0:
        if num_pennies == 1:
            print(f"{num_pennies} penny")
        else:
            print(f"{num_pennies} pennies")



def main ():
    print("Welcome to the self-checkout!")
    money_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${money_owed:.2f}")
    cashPaid = float(input("How much cash will you put in the self-checkout? "))
    change = cashPaid - money_owed
    print(f"Change is: ${change:.2f}")
    print(f"Change without formatting is: ${change}")
    change = round(change, 2)
    print(f"The change is ${change}")
    disperse_change(change)


if __name__ == "__main__":
    main()

    