n = int (input("Enter how many numbers :"))
a = []
for num in range (n):
    num = int(input("Enter numbers :"))
    a.append(num)
print("Your numbers :",a)

b = []
for num in a:
    if num not in b:
        b.append(num)
print("Length of new list :",len(b))
print("List after removing Duplicates :", b)
