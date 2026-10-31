
def fibo(num):
    # print("your numbers is :",num)
    a = 1
    b = 1
    for i in range (num):
        yield a 
        c = a + b
        a = b
        b = c

num = int(input("Enter number :"))
# print("Fibonacci Series ",fibo.num,end="  ")

print("The fibonacci series :")
for i in fibo(num):
    print(i)
