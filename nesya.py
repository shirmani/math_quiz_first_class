def endsmallq(x):
    print ('if you want to go forawd please press on 2')
    a = input (':')
    return a

def ifgo():
    if endsmallq == 2:
        print ('let stalt')
    else:
        while endsmallq() == 2:
            print('if you want to go forawd please press on 2')

ifgo()
import bollian