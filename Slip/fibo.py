n = int (input("Enter the term of series :"))
a = 1
b = 1
for i in range(n):
 print(a,end=" ")
 c = a + b ; a = b ; b = c;