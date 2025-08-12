def greatest_3(a,b,c):
    biggest = a
    if b > a:
        biggest = b
        if c > b:
            biggest = c
    elif c > a:
        biggest = c
    return biggest

#print(greatest_3(float(input("Enter a number:")),float(input("Enter a number:")),float(input("Enter a number:"))))

def sum2(a,b,c):
    suma = a+b+c

    if a != b:
        if b != c:
            sumb = suma
        else:
            sumb = a+b
    else:
        if a != c:
            sumb = a + c
        else:
            sumb = 0 
    return suma,sumb

#print(sum2(float(input("Enter a number:")),float(input("Enter a number:")),float(input("Enter a number:"))))


def multiples():
    print("Enter 5 numbers below:")
    a,b,c,d,e = float(input("First number:")),float(input("Second number:")),float(input("Third number:")),float(input("Fourth number:")),float(input("Fifth number:"))
    div = float(input("Enter a divisor:")) # divisor
    l_multiples = []
    count = 0
    if a%div == 0:
        count += 1
        l_multiples.append(a)
    if b%div == 0:
        count += 1
        l_multiples.append(b)
    if c%div == 0:
        count += 1
        l_multiples.append(c)
    if d%div == 0:
        count += 1
        l_multiples.append(d)
    if e%div == 0:
        count += 1
        l_multiples.append(e)
    print(count,l_multiples)

#multiples()

def ascending():
    a,b,c = float(input("First number:")),float(input("Second number:")),float(input("Third number:"))
    min = mid = max = None
    if a<b:
        if b > c:
            b = max
            if a > c:
                a = mid
                c  = min
        else:
            c = max
            b = mid
            a = min
    elif a>c:
        a = max
        if b > c:
            b = mid
            c = min
        else:
            b = min
            c = mid


def guess_num():
    import random as rd
    n1 = 1
    n2 = 6
    chosenNum = rd.randint(n1,n2)
    chances = 5
    won = False
    while chances >1:
        chances-=1
        userNum = int(input(f"Enter a number between {n1} and {n2}:"))
        assert userNum in range(1,7), "Invalid Input!"
        if userNum == chosenNum:
            print("You win")
            won = True
            break
        else:
            print("Wrong number")
    else:
        print(f"You ran out of guesses. The number was {chosenNum}")
    if won:
        print(f"You won with {chances} chances left.")

guess_num()