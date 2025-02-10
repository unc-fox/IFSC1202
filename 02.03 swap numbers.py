number =int (input(" enter a number for swappy swappy: "))
right = number % 10
left = number // 10
reversed = (right * 10) + left
print (reversed)