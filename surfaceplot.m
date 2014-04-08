%plots surface plot for desirability of printer locaiton on a campus
%additionally saves the optimum location as a variable optimum using
%multivariable polynomial regression with variable interaction

%read in data from file, file must only be random sampling for
% single printer
% columns of file must be in format where first column is total print
% distance, second column is printer x value, and third column printer
% y value
% change filename, and make sure file is in folder Matlab is using
num = csvread('data1.csv',1,0);

z = num(:,1);
x = num(:,2);
y = num(:,3);

%generate uniformly sampled data
xlin = linspace(min(x),max(x),length(x));
ylin = linspace(min(y),max(y),length(y));

%generate uniformly spaced grid to graph
[q,w] = meshgrid(xlin,ylin);

%interpolate the values of this function
%using linear interpolation to generate new
% z values
f = scatteredInterpolant(x,y,z);
e = f(q,w);

%plot the surface area, z values have been flipped so desirability is on
% z axis, meaning higher values are more optimal
figure
surf(q,w,-e,'FaceColor','interp',...
   'EdgeColor','none',...
   'FaceLighting','phong')
axis tight; hold on

%optional nonuniform data scatter plotting on top of surface plot
%to plot data, remove % in next line
%plot3(x,y,-z,'.','MarkerSize',15) 

%view can be changed to adjust for different campuses
view(-30,45)
camlight headlight


%will fit a multiple polynomial function to the values
% starting from the initial 0,0 point, it will find the function
% minimum value or where the most desirable location of a printer
% on the campus is and return it as optimum
polyregress1 = fit([x,y],z,'poly22');
initial = [0 0];
optimum = fminsearch(polyregress1,initial);
