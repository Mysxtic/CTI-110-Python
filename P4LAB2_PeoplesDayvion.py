#Dayvion Peoples
#P4LAB2
#10/30/25
#Use while loops and for loops together

'''
Get integer from user
Determine of integer is postive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again
If yes, run program
if no, end program
'''
run_again = "yes"

while run_again != "no":


    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for  item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run this progam again: ")

#Loop has broken, user entered 'no'
print("Program is ending...")
    