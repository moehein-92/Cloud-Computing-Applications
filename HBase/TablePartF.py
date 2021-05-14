import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
powers = connection.table('powers')

lst1 = []
lst2 = []

for k, v in powers.scan():
    row = powers.row(k)
    color = row['custom:color']
    name = row['professional:name']
    power = row['personal:power']
    lst1.append((color, name, power))
    lst2.append((color, name, power))

for i in lst1:
    color = i[0]
    name = i[1]
    power = i[2]
    for j in lst2:
        color1 = j[0]
        name1 = j[1]
        power1 = j[2]
        if (color == color1 and name != name1):
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
