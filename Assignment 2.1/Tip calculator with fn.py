'''  Name - Kelly Kasina Reg no - SCT211-0038/2022 '''

#Function for calculating the total bill each should pay
def total_by_each(bill,tipPercentage):
    tipAmount = float((bill*(tipPercentage/100)))
    tipByEach = float(tipAmount/peopleNumber)
    billByEach = float(bill/peopleNumber)
    totalByEach = float(round(tipByEach + billByEach , 2))
    return totalByEach

#Getting user input
bill = float(input("Enter the total bill amount: "))
peopleNumber = float(input("Enter number of people splitting the bill: "))
print("Choose a tip percentage: \n 1: 10% tip \n 2: 12% tip \n 3: 15% tip")
tipChoice= input("Enter the choice number(1/2/3): ")

#Printing bill for each for 10% tip percentage
if tipChoice == '1' :
    tipPercentage = 10
    print("The total amount payable by each person is: " , total_by_each(bill,tipPercentage))

#Printing bill for each for 12% tip percentage
elif tipChoice == '2':
    tipPercentage = 12
    print("The total amount payable by each person is: " , total_by_each(bill,tipPercentage))

#Printing bill for each for 15% tip percentage
elif tipChoice == '3' :
    tipPercentage = 15
    print("The total amount payable by each person is: " ,  total_by_each(bill,tipPercentage))

#Invalid tip choice
else :
    print("Invalid Input")
