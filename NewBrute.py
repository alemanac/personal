char = 'abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ1234567890@#$&!-_'

class creation:
    def make_my_own():
        return input('password here: ')
    def random_password():
        try: 
            length = int(input('lengh of randomly generated password: '))
        except:
            length = 4
            print("You didn't put a number. Pretty uncool you know, so it'll automatically be 4")
        y = ''
        import random
        for x in range(length):
            y += random.choice(char)
        return y
        
def choice():
    passwordchoice = input('random or your own [random]/[own]: ')
    if passwordchoice == 'random':
        return creation.random_password()
    elif passwordchoice == 'own':
        return creation.make_my_own()
    else:
        print('invalid choice')

password = choice()

def brute():
    guesspass = ' '
    listgp = list(guesspass)
    position = 0
    charamount = 
    print(listgp)
    while guesspass != password:
        for x in range(len(char)):
            listgp[positionamount] = char[position]
            print('test',listgp)
            position += 1
        
            

