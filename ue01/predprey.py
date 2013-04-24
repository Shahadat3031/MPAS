#!/usr/bin/env python2
import matplotlib.pyplot as plot
import scipy
from scipy.integrate import odeint

def predpray(a, b, r, s, x_0, y_0, t_start, t_stop, t_samplerate):
    def derivative((x_t, y_t), t):
        dx = r * x_t - a * x_t * y_t
        dy = -s * y_t + b * x_t * y_t
        return (dx, dy)

    t = scipy.arange(t_start, t_stop, t_samplerate)
    species = scipy.array((x_0,y_0))

    return odeint(derivative, species, t)

def usage(argv):
    print "Usage %s <a> <b> <r> <s> <x_0> <y_0> <t_start> <t_stop> <t_samplerate>" % argv[0]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 10:
        usage(sys.argv)
        sys.exit(1)
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        r = float(sys.argv[3])
        s = float(sys.argv[4])
        x_0 = float(sys.argv[5])
        y_0 = float(sys.argv[6])
        t_start = float(sys.argv[7])
        t_stop = float(sys.argv[8])
        t_samplerate = float(sys.argv[9])
    except ValueError, e:
        print e
        usage(sys.argv)
        sys.exit(1)
    populations = predpray(a, b, r, s, x_0, y_0, t_start, t_stop, t_samplerate)

    fig = plot.figure()
    ax = fig.add_subplot(111)
    ax.plot(populations, xdata=scipy.arange(t_start, t_stop, t_samplerate))
    ax.legend(('x(t)', 'y(t)'), 'upper center')
    ax.set_xlabel("Time")
    ax.set_ylabel("Population")
    plot.show()
