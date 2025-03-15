medical=input('do you have medical issues (yes or no)')
if medical=='yes':
    print('allowed')
else:
    attendance=int(input('enter your attendance'))
    if attendance>=75:
        print('allowed')
    else:
        print('not allowed')
