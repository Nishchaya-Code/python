try:
    num1,num2=eval(input("enter two numbers separated by the coma"))
    result=num1/num2
    print(result)

except ZeroDivisionError:
    print("you can't divide by zero!")

except SyntaxError:
    print("you don't listen to instructions")

except:
    print("You caused error to occur")

else:
    print('You made an error free code for once')

finally:
    print("no matter what this code will be running!")