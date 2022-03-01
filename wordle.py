def doubles(str):
    for i in range(0, len(str)):
        c = 0
        c = str.count(str[i])
        if (c > 1):
            return 0
        if (str[i].isalpha() == 0):
            return 0 
    return 1

def checker(a,b):
    l = []
    for i in range(len(a)):
        if(a[i] == b[i]):
            l.append(2)
        elif(a[i] in b):
            l.append(1)
        else: 
            l.append(0)
    return l

from english_words import english_words_set
import random

print()
print()
print()
l = list(english_words_set)
l2 = []
for i in l:
    if((len(i) == 6 or len(i) == 5) and i[0].islower() and doubles(i)== 1):
            l2.append(i)
l2.sort()
c = random.choice(l2)
lenc = len(c)
print("The word is ",lenc," letters long")

i = 1
while(i <= 6):
    print()
    print()
    print()
    gu = []
    str = input("Enter the guess: ")
    if(str == '0'):
        print(c)
        break

    if(str == c):
        print("WELL DONE CORRECT GUESS")
        break

    if(len(str) != lenc or l2.count(str) == 0):
        print("Guess correctly")

    else:
        i = i + 1
        gu = checker(str,c)
        for j in range(len(gu)):
            if (gu[j] == 2):
                print(c[j].upper(),end = " ")
            if(gu[j] == 0):
                print("_",end = " ")
            if(gu[j] == 1):
                print(str[j].lower(), end = " ")
    print()
else:
    print()
    print()
    print()
    print("The correct guess was",c)
print()
print()
print()