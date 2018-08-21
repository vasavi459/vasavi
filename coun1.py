Number = int(input(" "))
q = 0
while(Number > 0):
    Number = Number // 10
    q = q + 1
print("\n Number of Digits in a Given Number = %d" %q)    
