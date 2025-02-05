#Ask the user to provide his wieght.
weight= float(input("Please enter weight in kg:   "))

#Ask the user to provide hi height.
height= float(input("Please enter height in metres:   "))

#calculating the BMI
bmi=weight/(height**2)

print ("Your BMI is :", round(bmi,2))
# check if the BMI is bigger or equal to 25
if bmi >= 25.0 :
    print ("You are overwieght you need to work out more and watch your diet.")
# check if the BMI is bigger 18.5 or less than or equal 18.5
elif bmi<25.0 and bmi >=18.5:
    print ("You are fit & healthy.")
# check if the BMI is less than 18.5
else:
    print ("You are underweight. Watch your health.")




'''
this is the LAB_CONDITIONALS Bonus 
Feb5, 2025
By Mohammed Albushaier
'''
