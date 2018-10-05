import random

# func
def hint(x):
    for a in range(1, x[0] + 1):
        p = '*' * 10
        print(p)
    for b in range(1, x[1] + 1):
        print('*', end=' ')

#start
true = 0

while true <7:

    b = random.randint(1,50)

    b1 = int(b/10)
    b2 = b%10

    c = [b1,b2]

    hint(c)

    a = int(input('='))

    if b == a:
        print('very good you succses :)')
        true +=1
    else:
        ans = int(input('\n do you know what is the right answer? \n write it here: '))
        if ans == b:
            print('very good you succses :)')
            true += 0.5

        else:
            while b != ans:
                ans = int(input('try again :'))
                if ans == b:
                    print('very good you succses :)')