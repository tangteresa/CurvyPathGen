import matplotlib.pyplot as plt

"""
Author: Teresa Tang
tangsteresa@gmail.com or 5735298386
Last updated: 8/30/2019

Graphs the regression equation (the generated path) and the original points of the desired path for comparison
 Parameters: 
 ycoord: the Y coordinates of the generated path 
 xcoord: the X coordinates of the generated path 
 pathNum: the path number 
 
"""
class Grapher:
    def __init__(self, ycoord, xcoord, pathNum):
        self.xcoord = xcoord
        print("Graphing")
        self.ycoord = ycoord
        self.pathNum = pathNum

    """Graphs the generated path (smooth path) and the original path (scatter)
    Parameters: 
    originalY: the Y coordinates of the original or desired path
    originalX: the X coordinates of the original or desired path 
    file_name: the name that the graph will be saved as 
    """
    def graph(self, originalY, originalX, file_name):
        plt.figure(1)

        # plot data
        plt.ylabel('X')
        plt.xlabel('Y')
        plt.suptitle('Path Generation via Regression')
        # currently, the graph will autoscale the axes
        # uncomment the following two lines to choose a scale

        # plt.gca().set_ylim(ymin=-30)
        # plt.gca().set_ylim(ymax=30)

        plt.plot(self.ycoord, self.xcoord)
        plt.scatter(originalY, originalX)

        # save graph
        plt.savefig(str(file_name) + str(self.pathNum))