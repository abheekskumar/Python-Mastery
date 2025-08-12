# Program to print the largest of 3 numbers
def main1():
    num1, num2, num3 = eval(input("Enter the first number:")), eval(input("Enter the second number:")), eval(input("Enter the third number:"))
    maxnum = num1
    if num2 > maxnum:
        maxnum = num2
    if num3 > maxnum:
        maxnum = num3
    print("The largest number is:",maxnum)
    
#program to determine if a given number is even or odd
def main2():
    if eval(input("Enter a number to check if it's even or odd:"))%2==0:
        print("Even")
    else:
        print("Odd")

# lambda function implementation
def main3():
    add = lambda x, y : x+y
    print(add(1,2))
    print((lambda x,y:x*y)(3,3))

# Python Basics

# escape sequences




# Anomalous behavior in Python

print((0.1+0.2)==0.3)
print(len(str(0.1+0.2)))

if __name__ == '__main__':
    main3()

    