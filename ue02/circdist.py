#!/usr/bin/env python3
import math
import random
import matplotlib.pyplot as plot


def generate_point(r_max):
    phi = random.uniform(-math.pi, math.pi)
    u = random.random()+random.random()
    r_unit = 2-u if u > 1 else u
    r = r_unit * r_max
    x = math.cos(phi) * r
    y = math.sin(phi) * r
    return (x, y)


def distance(p1, p2):
    x = abs(p1[0]-p1[1])
    y = abs(p2[0]-p2[1])
    return math.sqrt(x**2 + y**2)


def simulate(point_num, r):
    d = []
    for _ in range(point_num):
        point1 = generate_point(r)
        point2 = generate_point(r)
        d.append(distance(point1, point2))
    return d


def avg(a):
    return float(sum(a)) / len(a)


r = 10
num = 100
while num <= 100000:
    print('-'*40)
    print('Simulating with %d points at r=%d' % (num, r))
    d = simulate(num, r)
    print('Result:    %f' % avg(d))
    print('Should be: %f' % ((128/(45*math.pi))*r))
    plot.hist(d,10)
    plot.show()
    num *= 10
