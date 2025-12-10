div3 = 'Fizz'
div5 = 'Buzz'
for i in range(1,101):
    if (i%3 == 0 and i%5 == 0):
        print('FizzBuzz')
    elif ( i%3 == 0):
        print (div3)
    elif (i%5 == 0):
        print (div5)
    else:
        print(i)
