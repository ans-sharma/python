'''Write a Tipper program where the user enters a restaurant bill total. The program should then
display two amounts: a 15% tip and a 20% tip.'''

bill = int(input("Enter the Total Bill:"))
print("15% tip:",int(bill * 0.15))  #Converting to int as fractional money cannot be paid
print("20% tip:", int(bill * 0.20))
