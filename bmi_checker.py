height= float(input("Enter your Height in cm:"))
weight= float(input("Enter your weight in kgs:"))
BMI= weight / (height/100)**2
print("your BMI is, BMI")
if BMI <= 18.4:
 print("you are underweight")
elif BMI <= 24.9:
 print ("You are Healthy.")