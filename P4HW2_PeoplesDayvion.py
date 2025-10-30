#Dayvion Peoples

#10/30/25

#P4HW2

#program will calculate gross pay for multiple employees
numEmployees = 0
numGross_pay = 0
numReg_hours = 0
numOvertime = 0
name = input("Enter employees name or 'done' to terminate': ")
while name.lower() != 'done':
    numEmployees +=1
    hours = int(input(f"How many hours did {name} work?:  "))
    pay_rate = float(input(f"What is {name} pay rate?: "))
    if hours > 40:
        ot = hours - 40
        ot_pay_rate = pay_rate * 1.5
        ot_pay = ot * ot_pay_rate
        regular_pay = pay_rate * 40
        gross_pay = ot_pay + regular_pay
        
    else:
        ot = 0
        ot_pay = 0
        regular_pay = pay_rate * hours
        gross_pay = regular_pay
    numGross_pay += gross_pay
    numReg_hours += regular_pay
    numOvertime += ot_pay
    print()
    print(f"Employee name: {name}")
    print()
    print(f"{'Hours Worked':<20}{'Pay rate':<20}{'Overtime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("-" * 110)
    print(f"{hours:<20}${pay_rate:<20.2f}{ot:<20}${ot_pay:<20.2f}${regular_pay:<20.2f}${gross_pay:<20.2f}")

    name = input("Enter employees name or 'done' to terminate': ")
    print()
print(f"Total number of employees entered: {numEmployees}")
print(f"Total amount paid for overtime: ${numOvertime}")
print(f"Total amount paid for reguular hours: ${numReg_hours}")
print(f"Total amount paid in gross: ${numGross_pay}")