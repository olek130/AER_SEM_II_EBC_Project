%%
close all;
clear all;
clc;
addpath('./Libs');

%% Program parameters
numberOfRobots = 2;
initialState = 1;
programSteps = 20;

%% AGV robots list construction
RobotFactory = AgvRobotFactory();
agvRobotsList = RobotFactory.makeAgvRobotsList(numberOfRobots, initialState);

%% Controller construction
controller = MasterController(agvRobotsList);
controller.loadMap();

%% Test task
task = struct();
task.name = 'getWood';
task.startingNode = 'ST3';
task.endingNode = 'SH1';

%% Task assignment test
%controller.assignPath(agvRobotsList.agvRobots.AGV_001, task);

%% %for iteration = 1 : 1 : programSteps
     for iter = 1:numberOfRobots
         agv_name = matlab.lang.makeValidName(strcat(num2str(iter,'AGV_%03.f')));
         %TODO put it to MasterController
        if strcmp(agvRobotsList.agvRobots.(agv_name).status,'WAIT_FOR_TASK')
            controller.assignPath(agvRobotsList.agvRobots.(agv_name), task);
        end
              
     end
     
    % robots asks for permissions or new path
%    % master controller evaluates requests
%    % robots make actions
% end
disp(agvRobotsList.agvRobots.AGV_002.path)
fig = figure();
[fig, plt] = controller.plotGraph(fig);
controller.highlightPath(plt,agvRobotsList.agvRobots.AGV_001.path);

% ship = struct();
% ship.cargo.types = ["coal","wood","potatoes"];
% ship.cargo.quantity = [10,10,10];
% storage = struct();
% storage.cargo.types = ["coal","wood","potatoes"];
% storage.cargo.quantity = [0,0,0];
