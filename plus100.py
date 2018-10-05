#plus & minose 0-100
import random

# definition func
def hint(x):
    for a in range(1, x[0] + 1):
        p = '*' * 10
        print(p)
    for b in range(1, x[1] + 1):
        print('*', end=' ')

#start
true = 0

while true < 7 :
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    e1 = a+b
    e2 = a-b

    z = '{}'+'\n'+'{}'+'\n'+'{}'

    f = random.randint(1,2)

    if f == 1:
        e = e1
        z = z.format(a,'+', b)
    else:
        e= e2
        z = z.format(a, '-', b)


    if e > 0 :
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
                a1 = []
                b1 = []
                for q in g:
                    o1 = q / 10
                    o2 = q % 10
                    if a == q:
                        a1.append(int(o1))
                        a1.append(o2)
                        w = a1
                    else:
                        b1.append(int(o1))
                        b1.append(o2)
                        o = b1
                for i in g:
                    print('\n' + str(i))
                    if i == a:
                        hint(a1)
                    else:
                        hint(b1)

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

