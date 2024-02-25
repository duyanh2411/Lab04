with open(r'D:\thonny\duyanh.txt', "w+") as fp:
    fp.write('My First Line\n')
    fp.write('My Second Line')
    fp.seek(0)
    print(fp.read())

with open(r'D:\thonny\duyanh.txt', "r+") as fp:
    fp.seek(0, 2)

    fp.write("\nThis content is added to the end of the file")

    fp.seek(0)
    print(fp.read())
with open(r'D:\thonny\duyanh.txt', "rb") as fp:
    fp.seek(3)
    print(fp.read(5).decode("utf-8"))

    fp.seek(10, 1)
    print(fp.read(6).decode("utf-8"))

with open(r'D:\thonny\duyanh.txt', "rb") as fp:
    
    print(fp.read(8).decode('utf-8'))

    fp.seek(-5, 1)
    print(fp.read(10).decode("utf-8"))

with open(r'D:\thonny\duyanh.txt', "r+") as fp:
    fp.seek(0, 2)

    print('file handle at:', fp.tell())

    fp.write("\nDemonstrating tell")

    print('file handle at:', fp.tell())

    fp.seek(0)
    print('file handle at:', fp.tell())

    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')
    print('file handle at:', fp.tell())
