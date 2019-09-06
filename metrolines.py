#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import random
import math

import numpy as np
import matplotlib.pyplot as plt
plt.subplots(1,figsize=(5,5))
plt.grid(b=True, which="major", color='#666666')

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 48

def generateLines(startPoints, endPoints):
    trainStops = [startPoints]
    while trainStops[-1] != endPoints:
        currPoint = trainStops[-1]

        turnAngles = []
        if currPoint[0] - endPoints[0] != 0:
            turnAngles.append([1,0])        # Can turn/move straight horizontally
        if currPoint[1] - endPoints[1] != 0:
            turnAngles.append([0,1])        # Can turn/move stright vertrically

        LengthA = currPoint[0] + currPoint[1]
        LengthB = endPoints[0] + endPoints[1]

        # if math.sqrt(LengthA**2 + LengthB**2) < math.sqrt((dimX**2 + dimY**2))*0.8:
        #     if (currPoint[0] - endPoints[0] != 0) and (startPoints[1] - endPoints[1] != 0):
        #         turnAngles.append([1,1])        # Can move diagonally

        if currPoint[0] - endPoints[0] > 0:
            for i in range(len(turnAngles)):
                turnAngles[i][0] = turnAngles[i][0] * -1

        if currPoint[1] - endPoints[1] > 0:
            for i in range(len(turnAngles)):
                turnAngles[i][1] = turnAngles[i][1] * -1

        trackLength = 1

        trackDirection = random.sample(turnAngles, 1)

        currPoint = [(currPoint[axis] + math.ceil(trackDirection[0][axis] / trackLength)) for axis in range(len(currPoint))]

        trainStops.append(currPoint)
    return trainStops

# Matplotlib colors
colors = ['b','g','r','c','m','y','k']

def generateMetro(maxDimensionsXYZ=[25,25,1], splitModel=0, metroLines=7):
    global dimX, dimY, dimZ
    dimX, dimY, dimZ = maxDimensionsXYZ

    axes = plt.gca()
    axes.set_xlim([dimX/2*-1,dimX/2])
    axes.set_ylim([dimY/2*-1,dimY/2])

    # 4 Quadrants on a graph ++, -+, --, +-
    quadrants = [[1,1],[-1,1],[-1,-1], [1,-1]]



    for line in range(metroLines):
        # Create metro line coordinate on pegboard

        startAndEndQuadrants = random.sample(quadrants, 2)

        # Ensure that the length of each metro line is long enough using a^2 + b^2 = c^2
        metroLineLength = 0
        while sqrt(metroLineLength) < math.sqrt((dimX**2 + dimY**2))*0.5:
            # Start divide both points by 2 as they will be multiplied by 2 when they're put into their quadrants
            metroStartPoints = [random.randrange(0, math.ceil(coord/2)) for coord in [dimX,dimY]]
            metroEndPoints = [random.randrange(0, math.ceil(coord/(dimX/dimY)/2)) for coord in [dimX,dimY]]
            # MetroEndPoints is divided by (dimX/dimY) so that it never reaches out past the given Y coordinate. If we didnt do this, then the metro map would be a dimX by dimX chart instead of dimX by dimY

            LengthA = metroStartPoints[0] + metroStartPoints[1]
            LengthB = metroEndPoints[0] + metroEndPoints[1]

            # a^2 + b^2 = c^2
            metroLineLength = LengthA**2 + LengthB**2

        print(math.sqrt(metroLineLength))
        #Multiply coordinates with the quadrant it belongs in (randomly generated in startAndEndQuadrants)
        metroStartPoints = [metroStartPoints[axis] * startAndEndQuadrants[0][axis] for axis in range(len(metroStartPoints))]
        metroEndPoints = [metroEndPoints[axis] * startAndEndQuadrants[1][axis] for axis in range(len(metroEndPoints))]

        #Assign quadrant to the coordinates

        points = generateLines(metroStartPoints, metroEndPoints)

        print("Metro Start and End:",metroStartPoints, metroEndPoints)
        #plt.plot([metroStartPoints[0], metroEndPoints[0]], [metroStartPoints[1], metroEndPoints[1]], '-', linewidth=7)
        print("points",points)

        plotLineColor = colors[line]


        for i in range(len(points)-1):
            plt.plot([points[i][0],points[i+1][0]], [points[i][1], points[i+1][1]], '-', linewidth=4, color = plotLineColor)

    plt.show()

generateMetro()

# if __name__ == '__main__':
#     a = generateMetro()
#     scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=True)
