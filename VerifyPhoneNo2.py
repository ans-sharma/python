import re
txt = "(+1)9999999998"
# x = re.search("^\d\d\d\d\d\d\d\d\d\d$", txt)
x = re.search("^\(\+\d{1,3}\)\d{10}$", txt)
if x:
    print("Its a valid no")
else:
    print("Not a valid no")
