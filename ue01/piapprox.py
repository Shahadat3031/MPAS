#!/usr/bin/env python2
#-*- encoding: utf-8 -*-

import getopt
import math
import time
import sys
import re
import random
import matplotlib.pyplot as plt

shots = 0
hits = 0

def usage():
    print("{} [OPTIONS] <iterations_1> [<iterations_2>, ...]".format(sys.argv[0]))
    print("OPTIONS:")
    print("-c <file>, --csv=<file>: Output data as csv <file>")
    print("-r <n>, --repetitions=<n>: Repeat experiment <n> times")
    print("<iterations_n> must be a python-parseable term")

def shoot():
    global shots
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    shots += 1
    return x,y

def is_hit(x,y):
    return (x*x + y*y) <= 1

def approx_pi(iterations):
    global shots, hits
    shots, hits = 0.0, 0.0
    start = time.time()
    for i in range(iterations):
        x,y = shoot()
        if is_hit(x,y):
            hits += 1
    stop = time.time()
    return hits/shots*4, stop-start

def parse(input):
    if not re.match('[0-9*+/-<>]+', input):
        raise ValueError("Illegal symbols")
    return eval(input)

def main():
    options, iterations_array = getopt.gnu_getopt(sys.argv[1:],'c:r:', ['csv=','repetitions='])
    csv_diff = None
    csv_time = None
    for opt, arg in options:
        if opt in ('-c', '--csv'):
            csv_diff = open(arg+"_diff.csv", "w+")
            csv_time = open(arg+"_time.csv", "w+")
        if opt in ('-r', '--repetitions'):
            try:
                repetitions = int(arg)
            except ValueError:
                usage()
                sys.exit(1)
            if repetitions <= 0:
                usage()
                sys.exit(1)
    if len(iterations_array) < 1: 
        usage()
        sys.exit(1)
    
    if csv_diff and csv_time:
        diff_str = ""
        time_str = ""
        for iterations in iterations_array:
            diff_str += "{};".format(iterations)
            time_str += "{};".format(iterations)
        csv_diff.write(diff_str[:-1]+"\n")
        csv_time.write(time_str[:-1]+"\n")

    for r in range(repetitions):
        results = []
        for i,iterations in enumerate(iterations_array):
            try:
                iterations = parse(iterations)
            except ValueError:
                usage()
                sys.exit(1)
            pi, exec_time = approx_pi(iterations)
            results.append((pi, exec_time))
            print("{}: n = {}; Pi: {}; Difference: {}; Execution Time: {}".format(r+1,iterations, pi, math.pi-pi, exec_time))
        if csv_time and csv_diff:
            diff_str = ""
            time_str = ""
            for result in results:
                diff_str += "{};".format(math.pi-result[0])
                time_str += "{};".format(result[1])
            csv_diff.write(diff_str[:-1]+"\n")
            csv_time.write(time_str[:-1]+"\n")

if __name__ == "__main__":
    main()
