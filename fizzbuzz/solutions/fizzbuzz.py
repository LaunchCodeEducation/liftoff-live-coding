'''
given x print from 1 to x in fizzbuzz format

if x is evenly divisible by 3 print "fizz"
if x is evenly divisible by 5 print "buzz"
if x is evenly divisible by both 3 and 5 print "fizzbuzz"
else print the number
'''


def fizzbuzz(x):
    for i in range(1,(x+1)):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


fizzbuzz(16)