def fibonacci():
    n = int(input("How many Fibonacci numbers? "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print(f"First {n} Fibonacci numbers: {sequence}")
