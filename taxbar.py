import os
import time
if os.path.exists(r'taxbar.txt'):
    os.remove(r'taxbar.txt')
time.sleep(2)
taxbar = open(r"taxbar.txt","a+") #Opening / creating (if it doesn't exist already) the .txt record file
print("Following are the tax-brackets applicable as per the GST ACT 2019:")
print("Select *1* for 8%")
print("Select *2* for 12%")
print("Select *3* for 15%")
print("Select *4* for 18%")
print("Select *5* for 22%")
taxfac = int(input("Enter tax bracket: "))
refdef = {1:"8", 2:"12", 3:"15", 4:"18", 5:"22"}
for taxfac in refdef:
    x = refdef[taxfac]
taxbar.write(x)
taxbar.close()
