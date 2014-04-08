%Description:
%This script will take in the data of the buildings and the printer loads
%and will put them into separate vectors to be used later.

%from small scale testing, I have determined that an organized CSV is the
%way to go, as it is extremely fast compared to importing .xlsx

filename = 'Pton Bldg Data.csv';
M = importdata(filename);
xlocation = M.data(:,1);
ylocation = M.data(:,2);
printerload = M.data(:,3);

buildinglist = char(M.textdata(:,1));
buildinglist = buildinglist(2:end,:);

clear M;
