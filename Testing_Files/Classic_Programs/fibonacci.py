def fibonacci(num1):
    # base case: num1 == 1 or 0; return 1
    if num1 == 1 or num1 == 0:
        return 1
    return fibonacci(num1-1) + fibonacci(num1-2)

if __name__ == "__main__":
    print(fibonacci(int(input("Enter a number for the fibonacci:"))))