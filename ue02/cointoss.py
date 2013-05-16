#!/usr/bin/env python3
import random, sys
import matplotlib.pyplot as plot, numpy

wins = []

def simulate_coin_tosses(n, k):
    for _ in range(k):
        wins_A = sum(random.choice([0,1]) for _ in range(n))
        wins_B = n-wins_A
        wins.append((wins_A, wins_B))
    return numpy.asarray(wins)
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('{:s} <n> [<k>]'.format(sys.argv[0]))
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 1 

    wins = simulate_coin_tosses(n, k)
    plot.boxplot(wins)
    plot.xticks([1,2], ['Wins A', 'Wins B'])
    plot.show()
