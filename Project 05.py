start = int(input("Enter beginning of Range: "))
end = int (input("Enter End of range:  "))

for number in range(start,end+1):
    n = number
    length = 0
    while n > 0:
        n //= 10  # this is equivalent to n = n // 10
        length += 1

    total = 0
    n = number
    while n > 0:
        remainder = n % 10
        total = total + remainder ** length
        n //= 10
    
    if total == number:
        print(number)
