def armstrong_number():
    num = int(input("Enter a number: "))
    order = len(str(num))
    sum_val = sum(int(digit) ** order for digit in str(num))
    if num == sum_val:
        print(f"{num} is an Armstrong Number ✅")
    else:
        print(f"{num} is NOT an Armstrong Number ❌")
