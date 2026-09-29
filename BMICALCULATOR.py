name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
bmi = (weight * 703) / (height * height)
print(bmi)

if bmi > 0:
    if(bmi < 18):
        print( name + ",you are underweight")
    elif(bmi < 24):
        print(name +",you are overweight")
    elif(bmi < 34):
        print(name +",you are obese")
    elif (bmi < 39 ):
        print(name +",you are moderately obese")
    else:
        print(name +",you are extremely obese")
else:
    print("Enter valid inputs")