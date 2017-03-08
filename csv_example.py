import csv

with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print '__ '.join(row)

# with open('eggs.csv', 'a') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
# ......*
