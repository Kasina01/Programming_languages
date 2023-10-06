'''  Name - Kelly Kasina Reg no - SCT211-0038/2022 '''

#Get the users name
name = input("Enter your name: ")

#Welcome the user and ask for their height and weight
print("Welcome " + name )
height = float (input("Enter your height in metres: "))
weight =float( input("Enter your weight in kilograms: "))

#Code for calculating BMI

bmi = (weight/(height**2))
print("Your BMI is" , bmi)

if bmi < 18.5 :  
    print(name + " you are underweight")

elif bmi>18.5 and bmi<24.5 :
    print(name + " you are normalweight")

else :
    print(name + " you are overweight")