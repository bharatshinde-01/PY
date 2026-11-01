try :
    f = open("test.txt","r")
    data = f.read()
    print("File contanin :")
    print(data)
    f.close()

except FileNotFoundError :
    print("File not found !")
    