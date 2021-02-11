import re
txt = "(+91)9999999998"
# x = re.search("^\d\d\d\d\d\d\d\d\d\d$", txt)
x = re.search("^\(\+\d\d\)\d\d\d\d\d\d\d\d\d\d$", txt)
if x:
  print("Its a valid no")
else:
  print("Not a valid no")
