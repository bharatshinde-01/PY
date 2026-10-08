n = int (input("Enter digits :"))
sum = 0
for i in range(n):
 dig = n % 10
 sum = sum + dig
 n = n // 10

print ( " sum of digits is this :" , sum ) 