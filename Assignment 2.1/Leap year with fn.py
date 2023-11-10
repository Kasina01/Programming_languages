'''  Name - Kelly Kasina Reg no - SCT211-0038/2022 '''
#Function for checking modulus of year and 4
def yearTest(x):
    test = x%4
    return test


year = int(input ("Enter a year: "))

if yearTest(year) == 0:
    print("Leap year")
else :
    print("Non leap year")
