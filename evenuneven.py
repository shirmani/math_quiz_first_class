import random
import math

 # definition func

def hint(a):
    d = int(a / 2)
    for i in range(1, d + 1):
        print('* *')


def fixworng(e,x):
    while e != x:
        e = int(input('please put the right answer:'))

# start

print ('the computer give you a number \n '
       'if the number even click on 2 \n'
       ' if the number uneven press 1')

true = 0

while true < 7 :
    a = random.randint(0, 100)

    print (a)
    if a%2 == 0:
        b = int(input('='))
        if b ==2:
            print ('you right :)')
            true += 1
        else:
            print ('try again :(')
            c = int(input('if you want hint press on 6 :'))

            if c == 6:
                hint(a)
            e = input ('if you know the answer now write here :')
            if e == 2:
                print('good ,you right :)')
                true += 0.5
            else:
                fixworng(e,2)


    else:
        b = int(input('='))
        if b == 1:
            print('you right :)')
            true +=1
        else:
            print('try again :(')
            c = int(input('if you want hint press on 6 :'))
            if c == 6:
                hint(a)
                print('*')

                e = int (input('if you know the answer now write here :'))
                if e == 1:
                    print('good ,you right :)')
                    true +=0.5
                else:
                    fixworng(e, 1)

