#Exercise
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#1) If the number is a multiple of 4, print out a different message.
#2)Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#Even or Odd
number = int(input("Enter number for knowing if its even or odd?:"))
if number%4 == 0:
    print('Number {} is multiple of 4'.format(number))
elif number%2 == 0:
    print('Number {} is even'.format(number))
else:
    print('Number {} is odd'.format(number))

#Extras
num = int(input('Enter number to check: '))
check = int(input('Enter number to be divided by: '))

if check != 0:
    if num%check == 0:
        print('Number {} divides evenly into {}'.format(num,check))
    else:
        print('Number {} doesn\'t divide evenly into {}'.format(num,check))
else:
    print('Number to be divided by can\'t be 0')
