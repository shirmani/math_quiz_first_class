#div 0-10
import random

true = 0

while true < 7:
    a = random.randint(1, 20)
    b = random.randint(2, 20)
    e = a / b
    e1 = a%b


    z = '{}' + ':'+ '{}'


    z = z.format(a, b)


    if e1==0 and 1 < e < 20:
        print(z)
        c = int(input('='))

        if c == e:
            print('very good you succses :)')
            true = true + 1

        else:
            print('try again :(')
            # hint print  # i can add a pohto if i end 3 shecode

            h = int(input('if you want a hint press on 6:'))
            if h == 6:
                print ( str(a) + '='+'_    '+ str(b) + '='+ '|')
                f = a*'*'
                for g in range (1,b+1):
                    print (f)

            ans = int(input('\n do you know what is the right answer? \n write it here: '))
            if ans == e:
                print('very good you succses :)')
                true = true + 0.5

            else:
                while e != ans:
                    ans = int(input('try again :'))
                    if ans == e:
                        print('very good you succses :)')

print('you did this \n you control in numbers!!!')


