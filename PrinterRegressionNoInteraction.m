%read in data from file, file must only be random sampling for
% columns of file must be in format where first column is total print
% distance, second column is printer x value, and third column printer
% y value, and so on for additional printers
% change filename, and make sure file is in folder Matlab is using
data = csvread('data.csv',1,0);

[i size] = size(data);
printernum = (size - 1)/2;

%dependent values of data
desirability = data(:,1);

%independent first degree values of data
data1 = data(:,2:size);
%independent second degree values of data
data2 = data1.^2;
%values of 1 to return a b0 coefficient
data0 = ones(i,1);

%concatenate data for b0 coeff, first degree, and second degree
data12 = horzcat(data0,data1,data2);

%run multivariable regression on dataset to return the coefficients
coeffs = mvregress(data12,desirability);

%regression function to optimize
regression = @(initx) sum(bsxfun(@times,vertcat(1,initx',initx'.^2),coeffs));

%initial guessing point, this can be modified for different starting point
initialx = ones(1,size-1);

%find optimal locations
%format of printer locations is [x1,y1,x2,y2,...xn,yn]
printerlocations = fmincon(regression, initialx,[],[],[],[],...
    zeros(1,length(initialx)),max(data1));
