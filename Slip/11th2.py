t =(10,20,30,40,20,10,50)

print("Repeted items in tuple :")
for i in t:
    if t.count(i)> 1:
        print(i)
b = int(input("Enter number to check :"))
if b in t:
    print("Yes this numbers is avaible :",b)
else :
    print("This is not avible in tuple ;")
