units=int(input('enter the amount of units conssumed'))
if units<50:
    print('the total bill is',units*2.6)
elif units>50 and units<100:
    print('the total bill is',units*3.5)
else:
    print('the total bill is',units*5.26)
