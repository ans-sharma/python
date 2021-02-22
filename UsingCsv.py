import csv

# myfile = open("/mnt/237beda3-9228-4a04-91c4-b6fd66ea6923/code playground/python/Test/a.csv", "w")
# # myfile = open('Test/t.csv','w')
# w = csv.writer(myfile)
# w.writerow(["Name","Place","Marks"])
# w.writerow(["Ans","KGP","90"])
# w.writerow(["XYZ","KOL","15"])
# w.writerow(["ABC","KOL","16"])
# myfile.close()
# myfile = open("/mnt/237beda3-9228-4a04-91c4-b6fd66ea6923/code playground/python/Test/a.csv", "r")
# # myfile = open("Test/t.csv","r")
# r = csv.reader(myfile)
# for a in r:
#     print(a)
# myfile.close()

myfile = open("/mnt/237beda3-9228-4a04-91c4-b6fd66ea6923/code playground/python/Test/a.csv", "w")
w = csv.writer(myfile)
[w.writerow([input()])for i in range(5)]