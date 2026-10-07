s = int (input("Enter starting point :"))
e = int (input ("Enter ending point :"))

for n in range ( s , e + 1):
    if n > 1:
        for i in range ( 2 , n ):
            if n % 2 == 0:
                break
        else :
            print ( n , end= " ")
            
