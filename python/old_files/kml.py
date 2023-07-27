#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""KML sample"""


import simplekml
from polycircles import polycircles
import subprocess
import pandas as pd


def main():
    "Plotting Points using simplekml library"

    point_kml = simplekml.Kml()
    point_kml.newpoint(name='Sample point', coords=[(-116.9957, 33.097)])
    point_kml_path = '/Users/kareblora/Desktop/point_kml.kml'
    point_kml.save(point_kml_path)

    "Opening file using subprocess"

    subprocess.call(['open', point_kml_path])

    "Plotting Lines"
    
    lines_kml = simplekml.Kml()
    lines = lines_kml.newlinestring(name='Path', description='Sample line',
                                    coords=[(-87.66, 41.87), (-87.19, 39.77), (-83.04, 39.95)])
    
    lines.style.linestyle.width = 5
    lines.style.linestyle.color = simplekml.Color.aqua
    
    lines_kml_path = '/Users/kareblora/Desktop/lines_kml.kml'
    lines_kml.save(lines_kml_path)

    "Opening file using subprocess"

    subprocess.call(['open', lines_kml_path])



if __name__ == '__main__':
    main()
