# CST 173 Logical Operators Practice

#################################################
# Validate that variable 'choice' is 4-7 or 9

choice = int(input("Enter input: "))

# Validate that input is 4-7 or 9
if (choice >= 4 and choice <= 7) or choice == 9:
    print("OK")
else:
    print("Not OK")
    
print()

#################################################
# Determine if a given power tool is subject to a
# product recall.  Tools impacted:
#   - Serial number 123400 through 123900
#   - Manufactured from Nov 2021 through Jul 2022
#   - Assembed in factories 21, 23, or 27

serialNumber = 123456
month = 5
year = 2022
factory = 23

recalled = False

# Determine if the tool is part of recall
if serialNumber >= 123400 and serialNumber <= 123900  and  \
    (factory == 21 or factory == 23 or factory == 27) and \
    ((year == 2021 and month >= 11) and (year == 2022  and month <= 7)):
    recalled = True
else:
    recalled = False

print(recalled)


#################################################
