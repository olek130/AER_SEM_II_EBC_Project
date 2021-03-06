classdef MasterController < handle
    %MASTERCONTROLLER Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        mapGraph,
        agvList,
    end
    
    methods
        function obj = MasterController(agvRobotsList)
            %MASTERCONTROLLER Construct an instance of this class
            %   Detailed explanation's not written.
            obj.mapGraph = digraph();
            obj.agvList = agvRobotsList;
        end
        
        function loadMap(obj)
            graphData = readtable('./Tables/EdgesList.csv');
            nodeA = table2array(graphData(:,3));
            nodeB = table2array(graphData(:,4));
            weights = table2array(graphData(:,5));

            stateList = readtable('./Tables/StateList.csv');
            nodeNames = table2array(stateList(:,1));
            occupancyGrid = table2array(stateList(:,3));
            obj.mapGraph = digraph(nodeA, nodeB, weights, nodeNames);
            obj.mapGraph.Nodes.occupancyGrid = occupancyGrid;            
        end
        
        function out = addAgvRobot(obj,agvRobot)
            %ADDAGVROBOT Add a robot to list in the controller
            %   Function adds a robot on the list and returns the total
            %   number of robots on the list.
            obj.AgvList.(agvRobot.Id) = agvRobot;    
            obj.agvCount = length(obj.agvList);
            out = obj.agvCount;
        end
        
        function path = assignPath(obj, agvRobot, task)
            [path.nodes, path.length] = shortestpath(obj.mapGraph, task.startingNode, task.endingNode);
            path.nodesPairs = [path.nodes(1 : length(path.nodes)-1 )', path.nodes(2 : length(path.nodes) )'];
            path.edges = findedge(obj.mapGraph, path.nodesPairs(:,1), path.nodesPairs(:,2));
            
            % Modify path edges weight by +1
            obj.mapGraph.Edges.Weight(path.edges) = obj.mapGraph.Edges.Weight(path.edges) + 1;
            agvRobot.current_node = path.nodes(1);
            agvRobot.status = 'WAIT_FOR_PERMISSION_MOVE';
            agvRobot.path = path;
        end
        
        function [fig, plt] = plotGraph(obj, fig)
            clf(fig);
            LWidths = 5*obj.mapGraph.Edges.Weight / max(obj.mapGraph.Edges.Weight);
            plt = plot(obj.mapGraph,'EdgeLabel',obj.mapGraph.Edges.Weight,'LineWidth',LWidths); 
            hold on; grid minor;
        end
        
        function highlightPath(obj, plt, path, rgbColor)
            if nargin < 4 % default value
                rgbColor = [rand(), rand(), rand()];
            end
            highlight(plt, path.nodes, 'EdgeColor',rgbColor);
        end
        
        function action = getAction(obj,agvRobot)
            new_node_id = strcmp(obj.mapGraph.Nodes.Name, agvRobot.path.nodes(1));
            if obj.mapGraph.Nodes.occupancyGrid(new_node_id) == 1
                action = 'STOP';
            else
                action = 'MOVE';
            end
            if (any(strcmp({'SH1','SH2','SH3'},agvRobot.current_node)) && ~agvRobot.has_product)
                action = 'LOAD';
            elseif (any(strcmp({'ST1','ST2','ST3'},agvRobot.current_node)) && agvRobot.has_product)
                 action = 'UNLOAD';
            end
        end
           function updateOcuppancyGrid(obj,current_pose, last_pose)
               if not(strcmp(current_pose, last_pose)) 
                    current_node_id = strcmp(obj.mapGraph.Nodes.Name, current_pose);
                    last_node_id = strcmp(obj.mapGraph.Nodes.Name, last_pose);
                    if (~any(strcmp(current_node_id, {'SH1','SH2','SH3','B'})))
                        obj.mapGraph.Nodes.occupancyGrid(current_node_id) = 1;
                    end
                    obj.mapGraph.Nodes.occupancyGrid(last_node_id) = 0;
               end
           end         
    end
end

