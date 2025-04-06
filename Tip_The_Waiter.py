def tip_waiter(total,tip):
    amt_paid=total+tip
    print('you have to pay',amt_paid)
    
total=int(input('Enter the total amount'))
tip=int(input('Enter the tip'))

tip_waiter(total,tip)