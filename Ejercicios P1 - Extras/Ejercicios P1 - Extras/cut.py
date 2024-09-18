import csv
with open('listado-codigos-postales.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        print('$ '.join(row))

