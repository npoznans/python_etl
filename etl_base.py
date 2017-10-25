#!/usr/bin/env python
import csv
import psycopg2

triggers = []

try:
    conn = psycopg2.connect("dbname='well_info_development' host='localhost' user='postgres' password='postgres'")
except:
    print "I am unable to connect to the database."

if 'test_recommendations.csv' is '':
    print "\n\n\tYou need to pull down the recommendation CSV from google drive"

cur = conn.cursor()
sql = "SELECT id FROM employers"
cur.execute(sql)
rows = cur.fetchall()
employers = []
for row in rows:
    employers.append(row[0])


with open('test_recommendations.csv' , 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    header_names = reader.fieldnames
    for row in reader:
        triggers.append(row['Row Titles'])

final_object = []
fieldnames = ['Recommendation', 'Source', 'Category','Score']
final_object.append(fieldnames)
with open('test_recommendations.csv' , 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for header in header_names[1:]:
        val = 0
        for row in reader:
            if row[str(header)] == 'X':
                final_object.append([str(header), 'Verve', triggers[val-1],  0])
            val += 1
        csvfile.seek(0)

with open('recommendation_import.csv', 'wb') as writefile:
    output = csv.writer(writefile, delimiter=',')
    for row in final_object:
        output.writerow(row)

print "\n\n\tYou have successfully created the custom recommendations."
print "\n\n\tcopy and paste this in your terminal -> python import_recommendations.py\n\n"
