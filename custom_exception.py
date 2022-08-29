# How to throw our own exception:

#create a class whatever exception you want.
#Here we are creating to fill a form by age limit concept 

class Dob(Exception):
    pass

bday=int(input("Enter your Birth year:"))
age=2022-bday

try:
    if age<=30 and age>=18:
        print("Fill up you form.")
    else:
        raise Dob
except Dob:
    print("You are not eligible for exam.")

