import random
import string

digits=list(string.digits)
letters=list(string.ascii_letters)
symbols=['!','@','#','$','%','^','&','*','?']
ambiguous=['`','~','(',')','-','_','=','+','[',']','{','}',';',':','"',"'",',','<','.','>','/','?','\\','|']
similarity=['1','i','I','l','L','|','o','O','0','8']

def generatePassword():
    password=[]
    strength=int(input('Enter password strength(1:Infirm - 9:Extreme): '))
    if strength==1:
        random.shuffle(digits)
        for _ in range(4):
            password.append(random.choice(digits))
    elif strength==2:
        alphabets=list(string.ascii_lowercase)
        random.shuffle(alphabets)
        for _ in range(random.randint(5, 8)):
            password.append(random.choice(alphabets))
    elif strength==3:
        random.shuffle(letters)
        for _ in range(random.randint(6, 10)):
            password.append(random.choice(letters))
    elif strength==4:
        random.shuffle(digits)
        random.shuffle(letters)
        for _ in range(random.randint(10, 15)):
            t=random.choice([0,1])
            if t==0:
                password.append(random.choice(digits))
            else:
                password.append(random.choice(letters))
    elif strength==5:
        for _ in range(random.randint(12,16)):
            t=random.choice([0,1,2,3,4])
            if t==0 or t==1:
                random.shuffle(digits)
                password.append(random.choice(digits))
            elif t==3 or t==2:
                random.shuffle(letters)
                password.append(random.choice(letters))
            else:
                random.shuffle(symbols)
                password.append(random.choice(symbols))
    elif strength==6 or strength==7:
        l=0
        if strength==6:
            l=random.randint(18,25)
        else:
            l=random.randint(30,40)
        for _ in range(l):
            t=random.choice([0,1,2,3])
            if t==0:
                random.shuffle(digits)
                password.append(random.choice(digits))
            elif t==1:
                random.shuffle(letters)
                password.append(random.choice(letters))
            elif t==2:
                random.shuffle(symbols)
                password.append(random.choice(symbols))
            else:
                random.shuffle(ambiguous)
                password.append(random.choice(ambiguous))
    elif strength==8:
        for _ in range(random.randint(30,40)):
            t=random.choice([0,1,2,3,4])
            if t==0:
                random.shuffle(digits)
                password.append(random.choice(digits))
            elif t==1:
                random.shuffle(letters)
                password.append(random.choice(letters))
            elif t==2:
                random.shuffle(symbols)
                password.append(random.choice(symbols))
            elif t==3:
                random.shuffle(ambiguous)
                password.append(random.choice(ambiguous))
            else:
                for i in range(2):
                    random.shuffle(similarity)
                    password.append(random.choice(similarity))
    elif strength==9:
        for _ in range(random.randint(50,100)):
            t=random.choice([0,1,2,3,4])
            if t==0:
                random.shuffle(digits)
                password.append(random.choice(digits))
            elif t==1:
                random.shuffle(letters)
                password.append(random.choice(letters))
            elif t==2:
                random.shuffle(symbols)
                password.append(random.choice(symbols))
            elif t==3:
                random.shuffle(ambiguous)
                password.append(random.choice(ambiguous))
            else:
                for i in range(random.randint(4, 10)):
                    random.shuffle(similarity)
                    password.append(random.choice(similarity))
    else:
        raise ValueError('Invalid strength!')
    return password

t=int(input())
while t>0:
    password=generatePassword()
    for _ in password:
        print(_,end='')
    print('')
    t-=1