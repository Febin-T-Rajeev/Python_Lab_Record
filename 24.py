import csv
with open('Book1.csv','r')as csvfile:
    data=csv.reader(csvfile)
    for line in data:
        print(line[1])
