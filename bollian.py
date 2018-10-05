import random

point = 0
while point < 7:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    e = str(a) +'__' + str(b)
    z = '>'
    y = '<'
    w = '='

    print (e)
    c = input('fill in the blanks:')
    if a > b:
       if c == z:
           print('you right !!')
           point += 1
       else:
          print ('try again :)')
          h = int(input('if you want a hint press on 6:'))
          if h == 6:
              g = [a, b]
              for i in g:
                  print('\n' + str(i))
                  for a in range(1, i + 1):
                      print('*', end=' ')
          ans = input('\n do you know what is the right answer? \n write it here: ')
          if ans == z:
              print('very good you succses :)')
              point += 0.5
          else:
              while z != ans:
                  ans =input('try again :')
                  if ans == z:
                      print('very good you succses :)')
    elif a < b:
        if c == y:
            print('you right !!')
            point += 1

        print('try again :)')
        h = int(input('if you want a hint press on 6:'))
        if h == 6:
            g = [a, b]
            for i in g:
                print('\n' + str(i))
                for a in range(1, i + 1):
                    print('*', end=' ')
        ans = input('\n do you know what is the right answer? \n write it here: ')
        if ans == y:
            print('very good you succses :)')
            point += 0.5
        else:
            while y != ans:
                ans = input('try again :')
                if ans == y:
                    print('very good you succses :)')

    else:
        if c == w:
            print('you right !!')
            point += 1

        print('try again :)')
        h = int(input('if you want a hint press on 6:'))
        if h == 6:
            g = [a, b]
            for i in g:
                print('\n' + str(i))
                for a in range(1, i + 1):
                    print('*', end=' ')
        ans = input('\n do you know what is the right answer? \n write it here: ')
        if ans == w:
            print('very good you succses :)')
            point += 0.5
        else:
            while w != ans:
                ans = input('try again :')
                if ans == w:
                    print('very good you succses :)')