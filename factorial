def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n - 1)
 
def factorial():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {n} (loop)      = {factorial_loop(n)}")
        print(f"Factorial of {n} (recursion) = {factorial_recursion(n)}")
