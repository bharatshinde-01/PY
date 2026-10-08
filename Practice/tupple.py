A = [ 1 , 2, 3, 4,5, 6]
n = int(input("Enter number to check :"))
for i in range(len(A)):
    if A[i] == n:
        print("This numbers is available :", A[i])
        break
else:
    print("This numbers is not availabel :",n)