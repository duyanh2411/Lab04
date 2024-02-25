text = "This is new content"
fp = open("duyanh.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()

fp = open("duyanh.txt", 'r')
print(fp.read())
fp.close()

file_path = r"D:\\thonny\duyanh.txt"
fp = open(file_path, 'r')
print(fp.read())
fp.close()

fp = open(file_path, 'w')
fp.write("This is overwritten content")
fp.close()

fp = open(file_path, 'r')
print("Opening file again..")
print(fp.read())
fp.close()

person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
fp = open("duyanh.txt", "w")
fp.writelines(person_data)
fp.close()

fp = open("duyanh.txt", "r")
print(fp.read())
fp.close()
