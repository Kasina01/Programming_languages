''' Name - Kelly Kasina Reg No - SCT 211-0038/2022 '''
import datetime
#Class for Arithmetic calculator
class Calculator:
        #Function for addition
        def addition ( x, y):
                return x + y

        #Function for subtraction
        def subtraction ( x, y):
                #Exception to prevent negative subtraction
                if x < y:
                        raise ValueError("x Should be larger than y")
                else :
                        return x-y

#Class for Age calculator
class AgeCalculator:
        #Function for calculating age
        def user_age ():   
                today = datetime.date.today()
                currentyear = today.year
                currentmonth = today.month
                currentday = today.day
                currentdiff = int(((currentyear*364)+(currentmonth*30)+currentday))
                birthdiff = int(((birthyear*364)+(birthmonth*30)+birthday))
                daysdiff = int((currentdiff-birthdiff))
                ageyears = int(daysdiff/365)
                agemonths = int(((daysdiff%365)/30))
                agedays = int(((daysdiff%365)%30))
                ageText = "You are {} years, {} months and {} days old"
                print(ageText.format(ageyears,agemonths,agedays))   

#Get the users name
name = input("Enter your name: ")

#Welcome the user and give them the choices
while True:
        print("Welcome " + name )
        print("Select operation.")
        print("1.Arithmetic calculator")
        print("2.Age calculator")
        print("3.Close")

        choice1 = input("Enter choice(1/2/3): ")
               
        #Code for Arithmetic calculator
        if choice1 == '1':
                print("Select operation.")
                print("1.Addition")
                print("2.Subtraction")

                choice2 = input("Enter choice(1/2): ")
 
                 #Code for printing sum
                if choice2 == '1':
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))

                        print(num1, "+", num2, "=", Calculator.addition(num1,num2))

                #Code for printing subtraction
                elif choice2 == '2':
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        print(num1, "-", num2, "=", Calculator.subtraction(num1,num2))

                #Exception for an invalid choice input
                elif choice2 != '1' or choice2 != '2' :
                        raise ValueError("The choice is between 1 and 2")

        #Code for age calculator
        elif choice1 == '2':
                print("Enter your birthday: ")
                birthyear = int( input("Birth year: "))
                birthmonth = int (input("Birth month: "))
                birthday = int(input("Birth day: "))
                AgeCalculator.user_age()
                
        #Code for closing 
        elif choice1 == '3' :
                print("Terminating program")  
                break

        #Exception for an invalid choice input
        elif choice1 != '1' or choice1 != '2' or choice1 != '3':
             raise ValueError("The choice is between 1,2 and 3")