"""
Author: Teresa Tang
tangsteresa@gmail.com or 5735298386
Last updated: 8/30/2019
Purpose: To generate and graph random curved paths through regression for the purpose of character movement control in games

Choose a type of equation to fit to your path points from the list below:
        0: sinusoidal,
        1: linear,
        2: quadratic,
        3: cubic,
        4: quartic,
        5: quintic,
        6: sixth,
        7: seventh,
        8: eighth,
        9: ninth

"""
import PathGen
import Grapher

"""Creates a path based on the given points"""
def generatePath(step, deviation, pathNum, has_start_end, only_start_end, desiredPathX, desiredPathY, equation, file_name):
    if(has_start_end):
        # assume first values in desiredPathX and desiredPath Y are start points while the last values in the same lists are end points
        path = PathGen.Path(desiredPathX, desiredPathY, equation, desiredPathY[0],
                            desiredPathY[len(desiredPathY) - 1], desiredPathX[0], desiredPathX[len(desiredPathY) - 1])
    elif(only_start_end):
        # points between the start and end point must be randomly generated
        path = PathGen.Path([], [], equation, desiredPathY[0],
                            desiredPathY[1], desiredPathX[0], desiredPathX[1])
    else:
        # assume default starting and ending point because none were given
        path = PathGen.Path(desiredPathX, desiredPathY, equation)

    # X and Y values for the generated path
    genPathY = []
    genPathX = []
    genPathY, genPathX = path.generatePath(step, deviation)

    # if there isn't an error in path generation, continue
    if(len(genPathY) != 0 and len(genPathX) != 0):
        print("Path generated")
        # get desired path X and Y values
        origPathY, origPathX = path.getOriginal()

        # create graphing object
        graph = Grapher.Grapher(genPathY, genPathX, pathNum)

        # graph generated path and desired path
        graph.graph(origPathY, origPathX, file_name)
        print("Done!")
    else:
        print("Path generation exited with code -1. Path could not be generated.")

def main():
    # user must set the following variables
    # as well as the desired path X and Y (with the first value being the start point and the last value being the end)

    # number of paths to generate
    num_paths = 3
    # see enumerated list at the top for equation types
    equation = 0
    # distance between the Y values that will be plotted onto the graph (the smaller the step, the smoother the path will appear)
    step = 0.1
    # the maximum amount you want your generated path's X values to differ from the X coordinate of the end point
    deviation = 10
    # the X coordinates of your desired path (remember: first value is start, last value is end)
    desiredPathX = [0, 20]
    # the Y coordinates of your desired path (remember: first value is start, last value is end)
    desiredPathY = [1, 37]
    # if the coordinates listed in the desiredPathX and desiredPathY are ONLY the start and end points, set true
    # otherwise, set false
    only_start_end = True
    # if the coordinates listed in desiredPathX and desiredPathY CONTAIN the start and end points but are not JUST the
    # start and end points, set true. Otherwise, set false
    has_start_end = False

    # If you want your path to be entirely randomly generated, desiredPathX and desiredPath Y will both be empty lists and
    # only_start_end and has_start_end will both be false

    # name of the file to save your path graphs as
    file_name = "TEST"

    for num in range(1, num_paths + 1):
        print("PATH GENERATION  " + str(num))
        generatePath(step, deviation, num, has_start_end, only_start_end, desiredPathX, desiredPathY, equation, file_name)


if __name__ == '__main__':
    main()