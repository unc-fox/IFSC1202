start = int(input("Enter beginning of Range: "))
end = int (input("Enter End of range:  "))

while start <= end:
    print(start +1)
    start += 1



n = int(input("Enter a Number:"))
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)