import csv

with open ('Book1.csv',newline='')as csvfile:
    data=csv.reader(csvfile,delimiter=' ',quotechar='|')
    for row in data:
        print(','.join(row))
