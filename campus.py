import csv
import random 
import math

# A printer object represents a single printer
class Printer:
    def __init__(self, x, y):
        self.xCoordinate = float(x); # x
        self.yCoordinate = float(y); # y
        self.printDist = 0;  # assigned print distance
        self.distToOrigin = self.distTo(0, 0);

    # distance to (x,y)
    def distTo(self, x, y):  
        return math.sqrt((x - self.xCoordinate)**2 + (y - self.yCoordinate)**2);

# encapsulates a random list of printers, sorted by 
# distance to origin
class Printers:
    def __init__(self, size, xMax, yMax):
        self.printers = [];
        for i in range(size):
            self.printers.append(Printer(random.uniform(0, xMax), random.uniform(0, yMax)));
        self.size = size;
        self.sortByDistToOrigin();

    def sortByDistToOrigin(self):
        self.printers.sort(key=lambda printer: printer.distToOrigin);

# A buildings object encampsulates data relevent to a college campus,
# including the location of its buildings and printers.
class Buildings:
    # buildingNames is a list of strings
    buildingNames = [];
    # xCoordinates is a list of x coordinates of buildings
    xCoordinates = [];
    # yCoordinates is a list of y coordinates of buildings
    yCoordinates = [];
    # buildingWeights is a list of doubles
    buildingWeights = [];


    # The constructor takes a .csv filename, and populates the appropriate 
    # tables
    def __init__(self, fileName):
        csvFile = open(fileName, 'rU');
        csvReader = csv.reader(csvFile);
        for line in csvReader:
            if len(line) != 4:
                print 'Each line must have four elements: name, x coordinate, y coordinate, and weight';
                exit();
            self.buildingNames.append(line[0]);
            self.xCoordinates.append(float(line[1]));
            self.yCoordinates.append(float(line[2]));
            self.buildingWeights.append(int(line[3]));
        self.xMax = max(self.xCoordinates);
        self.yMax = max(self.yCoordinates);


    # testing method for printing state
    def printState(self):
        print('Building Names:');
        for name in self.buildingNames:
            print(name);
        print('Coordinates:');
        for i in range(len(self.xCoordinates)):
            print (str(self.xCoordinates[i]) + " " + str(self.yCoordinates[i]));
        print('Building Weight:');
        for weight in self.buildingWeights:
            print(weight);

# A random distribution of printers, with methods to compute 
# undesirablity
class Distribution:    
    def __init__(self, buildings, size):
        self.buildings = buildings;  # buildings object
        self.printers = Printers(size, self.buildings.xMax, self.buildings.yMax);
        self.allocateBuildingsToPrinters();
    def allocateBuildingsToPrinters(self):
        for buildingNumber in range(len(self.buildings.buildingNames)):
            distances = [];
            for printer in self.printers.printers:
                distances.append(printer.distTo(self.buildings.xCoordinates[buildingNumber], self.buildings.yCoordinates[buildingNumber]));
            closestPrinter = min(xrange(len(distances)),key=distances.__getitem__)
            self.printers.printers[closestPrinter].printDist += self.buildings.buildingWeights[buildingNumber] * min(distances);
            
    def totalPrintDist(self):
        out = 0;
        for printer in self.printers.printers:
            out += printer.printDist;
        return out;

# A dataGenerator object is initalized with a set of buildings, a number 
# of printers, and a requested number of data points.  Contains
# a table relating total print distance to printer coordinates
class dataGenerator:
    def __init__(self, buildingFile, printNum, dataNum):
        self.buildings = Buildings(buildingFile);
        self.printNum = printNum;
        self.data = [];
        for i in range(dataNum):
            self.generateDataPoint();

    def generateDataPoint(self):
        dist = Distribution(self.buildings, self.printNum);
        dataPoint = [];
        dataPoint.append(dist.totalPrintDist());
        for i in range(self.printNum):
            dataPoint.append(dist.printers.printers[i].xCoordinate);
            dataPoint.append(dist.printers.printers[i].yCoordinate);
        self.data.append(dataPoint);

    def getData(self):
        return self.data;



