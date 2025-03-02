weight=float(input('enter weight in kg'))
height=float(input('enter height in cm'))
BMI=weight/(height/100)**2
if BMI<=18.4:
    print('underweight')
elif BMI<=24.9:
    print('fit')
elif BMI<=29.9:
    print('overweight')
elif BMI<=34.9:
    print('severly overweight')
elif BMI<=39.9:
    print('obese')
else:
    print('severly obese')