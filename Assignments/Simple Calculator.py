''' Name - Kelly Kasina Reg No - SCT 211-0038/2022 '''

#Get the users name
name = input("Enter your name: ")

#Welcome the user and give them the choices
print("Welcome " + name )
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Close")

choice = input("Enter choice(1/2/3): ")

#Code for sum
if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            print(num1, "+", num2, "=", num1 + num2)

#Code for subtraction
elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", num1 - num2)

#Code for closing 
elif choice == '3' :
        print("Terminating program")            

else :
        print("Invalid input")
