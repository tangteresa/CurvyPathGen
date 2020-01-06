from scipy.optimize import curve_fit
import math
import random
import numpy as np

"""
Author: Teresa Tang
tangsteresa@gmail.com or 5735298386
Last updated: 8/30/2019

Generates a path that roughly follows or passes through the x and y coordinates given 
Parameters: 
xpoints: x coordinates of the points (includes start or end point)
    Precondition: Must have at least 2 x coordinates or input empty list
ypoints: y coordinates corresponding to the x coordinates (includes start or end point)
    Precondition: Must have at least 2 y coordinates or input empty list 
equation: type of regression equation
ystart: the y coordinate of the desired path's starting point 
yend: the y coordinate of the desired path's end point
xstart: the x coordinate of the desired path's starting point
xend: the x coordinate of the desired path's end point
"""
class Path:
    def __init__(self, xpoints, ypoints, equation, ystart=0, yend=10, xstart=10, xend=10):
        # default value for x and y coordinates of the desired path's start and end points are 0, 10, 10, and 10
        # in order from ystart to xend
        self.ystart = ystart
        self.yend = yend
        self.xstart = xstart
        self.xend = xend

        # input the x coordinates and y coordinates of the points that the path will roughly follow or pass through
        # data type is a list with comma delimited coordinates []
        # if coordinate lists are both empty then the path will be randomly generated
        self.xpoints = list.copy(xpoints)
        self.ypoints = list.copy(ypoints)

        # equation type, as listed in main
        self.equation = equation

        # minimum number of points required to define the equation of the type listed by the user
        self.minNumPoints = self.number_of_coefficients(self.equation)

    """Generate a path with random points or predefined points inputted by the user 
    Parameters: 
    step: the distance between each y value to be plotted on the graph 
    deviation: the maximum amount by which the randomly generated point's X values will differ from the end point's X value
    
    Return: 
    [], []: if there is an error 
    fitted_y: the y values of the regression equation
    fitted_x: the x values of the regression equation
    """
    def generatePath(self, step=0.1, deviation=5):
        # create random path points if no points are given
        if (len(self.xpoints) == 0 and len(self.ypoints) == 0):
            if (self.randPoints(deviation) != 0):
                return [], []
            # add default start/end points or the start/end points given by the user (if they only gave start/end points)
            self.ypoints.append(self.ystart)
            self.ypoints.append(self.yend)
            self.xpoints.append(self.xstart)
            self.xpoints.append(self.xend)

        # check if there are enough points to define the equation chosen by the user
        if (len(self.xpoints) < self.minNumPoints or len(self.ypoints) < self.minNumPoints):
            print("There are not enough points in the path. Must have " + str(self.minNumPoints) + ". Increase the"
                "distance between the start and end points, add more points, or lower the regression equation degree." )
            return [], []

        try:
            # perform regression on the points
            return self.regression(step)
        except RuntimeError:
            # a runtime error is most likely caused by the sinusoidal regression maxing out its iterations without
            # finding a suitable regression fit
            print("The sinusoidal function could not be fit to the path points.")
            return [], []

    """Returns the X and Y coordinates of the points in the original path, i.e. the path given by the user (aka desired path)"""
    def getOriginal(self):
        return self.ypoints, self.xpoints

    """Generates random x and y coordinates for the path to roughly follow
    Parameters: 
    deviation: the max amount by which randomly generated X coordinates will differ from the X coordinate of the end point
    
    Return: 
    -1: if the path is too short to have enough points to fit the regression equation to 
    0: if the correct amount of random points is successfully generated """
    def randPoints(self, deviation):
        try:
            # random.sample() returns a new list
            # the minimum number of points required to define a polynomial includes the start and end points
            # hence the minus 2 to find the number of points that still need to be generated
            self.ypoints = random.sample(range(self.ystart + 1, self.yend), self.minNumPoints - 2)
        except ValueError:
            print("The type of regression selected cannot be performed on the given path. Select a regression equation of"
                  " a lower degree or add more distance between the path's start and end points.")
            return -1

        # every Y coordinate will have a corresponding X coordinate
        for y in self.ypoints:
            # calculate minimum and maximum values that the X coordinates can be
            lowerbound = min(self.xend - deviation, self.xend + deviation)
            upperbound = max(self.xend - deviation, self.xend + deviation)
            self.xpoints.append(random.randint(lowerbound, upperbound))

        return 0

    def regression(self, step):
        # regression function
        solution, pcov = curve_fit(f=self.equations(self.equation), xdata=self.ypoints, ydata=self.xpoints,
                                   p0=[0.3, ] * self.number_of_coefficients(self.equation))

        print("Solution coefficients: " + str(solution))
        # turns solution into a list so that it can be graphed
        solution = solution.tolist()

        # calculates x values based on regression equation
        # saves x and y values into a list
        fitted_x = []
        fitted_y = []

        fitted_x.append(self.xstart)
        fitted_y.append(self.ystart)

        # plug Y values into the regression equation to get the corresponding X values
        for y in np.arange(self.ystart + step, self.yend - step, step):
            fitted_x.append(self.equations(self.equation)(y, *solution))
            fitted_y.append(y)

        fitted_x.append(self.xend)
        fitted_y.append(self.yend)

        return fitted_y, fitted_x

    def sinusoidal(self, y, a, b, c, d):
        return (a * np.sin(b * y + c)) + d

    def linear(self, y, a, b):
        return a * y + b

    def quadratic(self, y, a, b, c):
        return a * (y ** 2) + b * y + c

    def cubic(self, y, a, b, c, d):
        return a * (y ** 3) + b * (y ** 2) + c * y + d

    def quartic(self, y, a, b, c, d, e):
        return a * (y ** 4) + b * (y ** 3) + c * (y ** 2) + d * y + e

    def quintic(self, y, a, b, c, d, e, f):
        return a * (y ** 5) + b * (y ** 4) + c * (y ** 3) + d * (y ** 2) + e * y + f

    def sixth(self, y, a, b, c, d, e, f, g):
        return a * (y ** 6) + b * (y ** 5) + c * (y ** 4) + d * (y ** 3) + e * (y ** 2) + f * y + g

    def seventh(self, y, a, b, c, d, e, f, g, h):
        return a * (y ** 7) + b * (y ** 6) + c * (y ** 5) + d * (y ** 4) + e * (y ** 3) + f * (
                    y ** 2) + g * y + h

    def eighth(self, y, a, b, c, d, e, f, g, h, i):
        return a * (y ** 8) + b * (y ** 7) + c * (y ** 6) + d * (y ** 5) + e * (y ** 4) + f * (
                    y ** 3) + g * (y ** 2) + h * y + i

    def ninth(self, y, a, b, c, d, e, f, g, h, i, j):
        return a * (y ** 9) + b * (y ** 8) + c * (y ** 7) + d * (y ** 6) + e * (y ** 5) + f * (
                    y ** 4) + g * (y ** 3) + h * (y ** 2) + i * y + j

    def number_of_coefficients(self, equation):
        # selects number of coefficients based on the equation type
        number_of_coefficients = {
            0: 4,
            1: 2,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            6: 7,
            7: 8,
            8: 9,
            9: 10
        }

        return number_of_coefficients[equation]

    def equations(self, equation):
        # selects equation based on the input
        equations = {
            0: self.sinusoidal,
            1: self.linear,
            2: self.quadratic,
            3: self.cubic,
            4: self.quartic,
            5: self.quintic,
            6: self.sixth,
            7: self.seventh,
            8: self.eighth,
            9: self.ninth
        }

        return equations[equation]
