#10
#a)
pwr = eval(input('Enter a power: '))
eqn = 2**pwr
digt = eqn%10

print('last digit of 2 raised to that power is: ', digt)

#10
#b
pwr = eval(input('Enter a power: '))
eqn = 2**pwr
digt = eqn%100

print('last two digits of 2 raised to that power is: ', digt)

#10
#c hmm not done
pwr = eval(input('Enter a power: '))
digt = eval(input('How many digits do you want?: '))
eqn = 2**pwr
last = eqn%digt


print('last digit of 2 raised to that power is: ', last)