
n = int(input("Enter how many numbers :"))
a = [] 
print("Enter numbers :")
for i in range (n):
    num = int(input())
    a.append(num)
print("Your numbers :",a)

b = []
for i in a:
    if i not in b:
        b.append(i)
print("Afeter remove Duplcates :")
print(b)