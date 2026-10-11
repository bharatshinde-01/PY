listt = [10 , 20 , 30 , 40 , 50 ]
n = int (input("Enter number to check :"))
for i in range (len(listt)):
    if listt[i] == n :
        print("Yes this is availabe in tupple :", listt[i])
        break
else :
    print("This numbers is not available in tupple :" , i )
