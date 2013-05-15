#!/usr/bin/env python2
import matplotlib
import math
import cmath
import random

def generate_point():
    phi = random.uniform(-math.pi, math.pi)
    return phi

def distance(p1, p2):
    d = abs(p1-p2)
    if d > math.pi:
        d = 2*math.pi-d
    return math.sqrt(d)

def simulate(point_num):
    points = [generate_point() for _ in range(point_num)]
    d = []
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                d.append(distance(p1, p2))
    return d
