first = float (input("Input First Number: "))
operator = input ("Input Operator: ")
second = float (input("Input Second Number: "))
if operator == "+":
    answer = first + second
elif operator == "-":
    answer = first - second
elif operator == "*":
    answer = first * second 
elif operator == "/":
    answer = first / second
else:
    answer = ("Invalid Operator")
print (first, operator, second, "=", answer) 
