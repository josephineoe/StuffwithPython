#1

length = eval(input('Enter a length in cm:'))

if length < 0:
    print('This entry is invalid')
else:
    print('The length in inches is: ', (length/2.54))
