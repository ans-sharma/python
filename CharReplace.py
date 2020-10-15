sText = input("Enter the String: ")
sPattern = input("Pattern to find: ")
sReplace = input("Pattern to replace: ")
sFinal = ""
i = 0
while i < len(sText):
    if sText[i] == sPattern[0]:
        if sText[i:i+len(sPattern)] == sPattern:
            sFinal += sReplace
            i += len(sReplace)
        else:
            sFinal += sText[i]
            i += 1
    else:
        sFinal += sText[i]
        i += 1
print("Modefied String: "+sFinal)
