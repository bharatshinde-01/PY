num = int(input("Enter number :"))
print("Prime numbers up to ",num,end=" :")
for i in range(num):
    if i %2 != 0:
        print(i,end="  ")
    