import happybase as hb
import csv

connection = hb.Connection()
powers = connection.table('powers')

with open('input.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        k = row[0]
        hero = row[1]
        power = row[2]
        name = row[3]
        xp = row[4]
        color = row[5]
        powers.put(k, {'personal:hero':hero,
                       'personal:power':power,
                       'professional:name':name,
                       'professional:xp':xp,
                       'custom:color':color})