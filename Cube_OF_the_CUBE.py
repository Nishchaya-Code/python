def cube(n):
    if n%3==0:
        print('The cube of the number is',n*n*n)
    else:
        print('your number is not divisble by 3 so no cube')

n=int(input("enter any number"))
cube(n)