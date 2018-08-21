num1 = int(input(" "))
v=num1
sum = 0
if num1 <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num1 > 0:
        sum = sum + num1
        num1 = num1 - 1
print("Sum of first", v, "natural numbers is: ", sum)        
