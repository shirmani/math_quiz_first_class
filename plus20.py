#plus & minose 0-20
import random

true = 0

while true < 7 :
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    e1 = a+b
    e2 = a-b
    z = '{}'+'{}'+'{}'

    f = random.randint(1,2)
    if f == 1:
        e = e1
        z = z.format(a,'+', b)
    else:
        e= e2
        z = z.format(a, '-', b)


    if e > 0 and e < 20:
        print (z)
        c = int(input ('='))

        if c == e:
            print ('very good you succses :)')
            true = true+1

        else:
            print ('try again :(')
        # hint print  # i can add a pohto if i end 3 shecode

            h = int( input('if you want a hint press on 6:'))
            if h == 6:
                g = [a, b]
                for i in g:
                    print('\n' + str(i))
                    for a in range(1, i + 1):
                        print('*', end=' ')

            ans = int(input ('\n do you know what is the right answer? \n write it here: '))
            if ans == e:
                 print('very good you succses :)')
                 true = true + 0.5

            else:
                while e != ans:
                    ans = int (input ('try again :'))
                    if ans == e :
                        print ('very good you succses :)')

print ('you did this \n you control in numbers!!!')


    

