#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import random
import math

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 48

def generateLine(spawnCoords):
    turnAngles = [0,45,90]


def generateMetro(dimensionsXYZ=[20,10,1], splitModel=0, metroLines=3):
    dimX, dimY, dimZ = dimensionsXYZ

    for line in range(metroLines):
        # Create metro line coordinate on pegboard
        metroSpawnCoordinates = [random.randrange(math.floor(coord/2*-1), math.floor(coord/2)) for coord in [dimX,dimY]]
        print(metroSpawnCoordinates)

generateMetro()

# if __name__ == '__main__':
#     a = generateMetro()
#     scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=True)
