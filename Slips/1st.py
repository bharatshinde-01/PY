# Write a Python program to accept n numbers in list and remove duplicates
# from a list.

n = int (input("Enter how many numbers :"))
List = [] 
print("Enter your numbers :",end= " ")
for i in range (n):
    num = int(input())
    List.append(num)
print("Your elements :",end=" ")
for i in range (n):
    print(List[i],end= " ")

b = []
for num in List:
    if num not in b:
        b.append(num)

print("")
print("List After removing Duplicates :",b)