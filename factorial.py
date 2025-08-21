def factorial(n):
   
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


number = int(input("Enter a Number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
   
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}")
