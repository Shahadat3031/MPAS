#!/usr/bin/env python3
import math
import random
import matplotlib.pyplot as plot


def generate_point(r):
    phi = random.uniform(-math.pi, math.pi)
    x = math.cos(phi) * r
    y = math.sin(phi) * r
    return (x, y)


def distance(p1, p2):
    x = abs(p1[0]-p1[1])
    y = abs(p2[0]-p2[1])
    return math.sqrt(x**2 + y**2)


def simulate(point_num, r, plotit=False):
    points = [generate_point(r) for _ in range(point_num)]

    if plotit:
        xs = []
        ys = []
        for p in points:
            xs.append(p[0])
            ys.append(p[1])
            plot.plot(xs, ys, 'r+')
            plot.show()

    point = generate_point(r)
    d = []
    for p in points:
            d.append(distance(p, point))
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
    plot.hist(d,100)
    plot.show()
    num *= 10
