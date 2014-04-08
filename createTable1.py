# Script creates data, exports to csv
from campus import *
import csv

targetFile = open('data1.csv', 'wb');  # where we're going to write to
csvWriter = csv.writer(targetFile);

# Gonna generate some data now.  Using 5 printers and 100 points.
# You can change those values as you like
d = dataGenerator('pton.csv', 1, 100);

# Gonna write in a header for the csv file.  You can delete
# this part if you want
header = [];
header.append('Total Print Distance');
for i in range(d.printNum):
    header.append('X-Printer ' + str(i+1));
    header.append('Y-Printer ' + str(i+1));
csvWriter.writerow(header);

# Gonna write that data to the csv file now.
for row in d.getData():
    csvWriter.writerow(row);




