a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

print("1.Addition")
print("2.Subtration")
print("3.Multiplation")
print("4.Division")
print("5.Modules")

c = int(input("Choose operation :"))

match (c):
    case 1: 
        print("Sum of two numbers is :",a + b)
    case 2:
        print("Subtration of two number is :", a - b)
    case 3:
        print("Multiplation of two numbers is :",a * b)
    case 4 :
         if a == 0 or b == 0:
             print("Not Divisibal by Zero !  ")
         else :
             print("Division of two numbers is :",a / b)
    case 5: 
        print("Modulus of numbers is :", a % b )
    case default :
        print("Invalid operation !")

