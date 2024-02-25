import os

old_name = r"D:\thonny\duyanh.txt"
new_name = r"D:\thonny\duyanh1.txt"
os.rename(old_name, new_name)

import os

folder = r'D:\thonny\lab4a.q4a\\'
count = 1
for file_name in os.listdir(folder):
    source = folder + file_name

    destination = folder + "sales_" + str(count) + ".txt"

    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
res = os.listdir(folder)
print(res)

import os

files_to_rename = ['sales_1.txt', 'sales_4.txt']
folder = r"D:\thonny\lab4a.q4a\\"

for file in os.listdir(folder):
    if file in files_to_rename:
    
        old_name = os.path.join(folder, file)
        
        only_name = os.path.splitext(file)[0]

        new_base = only_name + '_new' + '.txt'

        new_name = os.path.join(folder, new_base)

        os.rename(old_name, new_name)

res = os.listdir(folder)
print(res)

import os
from datetime import datetime

current_timestamp = datetime.today().strftime('%d-%b-%Y')
old_name = r"D:\thonny\lab4a.q4a"
new_name = r"D:\thonny\lab4a.q4a" + current_timestamp + ".txt"
os.rename(old_name, new_name)

import os

folder = r"D:\thonny\lab4a.q4b\\"
print('Before rename')
files = os.listdir(folder)
print(files)

for file_name in files:

    old_name = os.path.join(folder, file_name)

    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)

print('After rename')
print(os.listdir(folder))
