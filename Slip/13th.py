try:
    n = int(input("Enter number :"))
    if n > 0 :
        print("Positive number ")
    else :
        print("Negative number ")
except ValueError :
    print("invalid number ")