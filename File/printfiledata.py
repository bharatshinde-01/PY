try:
    f = open("File/test.txt","r")
    data = f.read();
    print("File text :")
    print(data)
    f.close()
except FileNotFoundError:
    print("File not found !")