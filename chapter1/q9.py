#9
price = eval(input('Input price of meal:'))
tip = eval(input('Input tip percentage desired:'))

perctip = price*(tip/100)

total = price + perctip

print('The total price of the meal with tip incl is:', total)