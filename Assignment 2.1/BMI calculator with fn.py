'''  Name - Kelly Kasina Reg no - SCT211-0038/2022 '''

#Function for calculating BMI
def bmiCalculator(x,y):
    unroundedbmi= (x/(y**2))
    bmi = round(unroundedbmi,2)
    return bmi

#Get the users name
name = input("Enter your name: ")

#Welcome the user and ask for their height and weight
print("Welcome " + name )
height = float (input("Enter your height in metres: "))
weight =float( input("Enter your weight in kilograms: "))

#Code for printing BMI
print("Your BMI is" , bmiCalculator(weight,height))

if  bmiCalculator(weight,height) < 18.5 :  
    print(name + " you are underweight")

elif bmiCalculator(weight,height) > 18.5 and bmiCalculator(weight,height) < 24.5 :
    print(name + " you are normalweight")

else :
    print(name + " you are overweight")