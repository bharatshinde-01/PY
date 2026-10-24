n  = int (input("Enter how many numbers :"))
a = [] 
for i in range (n):
    num = int(input("Enter num :"))
    a.append(num)
b = []
for c in a:
    if c not in  b:
        b.append(c)
print(b)