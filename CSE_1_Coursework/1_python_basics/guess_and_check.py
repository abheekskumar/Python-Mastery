def cube_root():
    x = int(input("Enter an integer:"))
    ans = 0

    while ((ans**3) < abs(x)):
        ans +=1
    if ans**3 == abs(x):
        print(ans)
    else:
        print("Imperfect cube.")
        print(ans)
        
def cleaner_cube_root():
    x = int(input("Enter an integer:"))
    for i in range(abs(x)+1):
        if i**3 == abs(x):
            if x>=0:
                print(i)
            elif x<0:
                print(-i)
                




if __name__ == "__main__":
    pass
    #cube_root()
    cleaner_cube_root()