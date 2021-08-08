a = input('Enter which operator you want to use ')
b = int(input('Enter first number '))
c = int(input('Enter Second number '))

if a == '+':
    if (b==56 and c==9) or (b==9 and c==56):
        print('{} {} {} = 77'.format(b,a,c))
    else:
        print('{} {} {} = {}' .format(b,a,c,(b+c) ))
elif a == '*':
        if(b==45 and c == 3) or (b == 3 and c== 45):
            print('{} {} {} = 555'.format(b,a,c))
        else:
            print('{} {} {} = {}' .format(b,a,c,(b*c) ))
elif a == '/':
    if(b == 56 and c == 6):
        print('{} {} {} = 4'.format(b,a,c))
    else:
        print('{} {} {} = {}' .format(b,a,c,(b/c) ))







