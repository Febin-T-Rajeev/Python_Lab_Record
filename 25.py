import csv
with open('abcd.txt', mode='w') as outf:
    fieldnames = ['Name', 'Department', 'Birthday Month']
    content = csv.DictWriter(outf, fieldnames=fieldnames)
    content.writeheader()
    content.writerow({'Name': 'John', 'Department': 'Accounting', 'Birthday Month': 'November'})
    content.writerow({'Name': 'Amy', 'Department': 'IT', 'Birthday Month': 'March'})
