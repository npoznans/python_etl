#!/usr/bin/env python
import csv
import psycopg2

triggers = []

try:
    conn = psycopg2.connect("dbname='local_dev' host='localhost' user='postgres' password='postgres'")
except:
    print "I am unable to connect to the database."

if 'loading.csv' is '':
    print "\n\n\tYou need to have a csv file named 'loading.csv' in this directory"

cur = conn.cursor()
sql = "SELECT id FROM loading_table"
cur.execute(sql)
rows = cur.fetchall()
employers = []
for row in rows:
    employers.append(row[0])


with open('loading.csv' , 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    header_names = reader.fieldnames
    for row in reader:
        triggers.append(row['Row Titles'])

final_object = []
fieldnames = ['column1', 'column2', 'column3', 'column4']
final_object.append(fieldnames)
with open('loading.csv' , 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for header in header_names[1:]:
        val = 0
        for row in reader:
            if row[str(header)] == 'X':
                final_object.append([str(header), 'Verve', triggers[val-1],  0])
            val += 1
        csvfile.seek(0)

with open('loading.csv', 'wb') as writefile:
    output = csv.writer(writefile, delimiter=',')
    for row in final_object:
        output.writerow(row)

print "\n\n\tYou have successfully loaded the files."
print "\n\n\tcopy and paste this in your terminal -> python import_loading.py\n\n"
