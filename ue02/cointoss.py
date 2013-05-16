#!/usr/bin/env python3
import random, sys
import matplotlib.pyplot as plot, numpy

wins = []
HEADS = 0
TAILS = 1

def simulate_coin_tosses(n, k):
    A_ahead, B_ahead, wins_A, wins_B = 0, 0, 0, 0
    for _ in range(k):
        for _ in range(n):
            throw = random.choice([HEADS,TAILS])
            if throw == HEADS:
                wins_A += 1
                wins_B -= 1
            else:
                wins_A -= 1
                wins_B += 1
        wins.append((wins_A, wins_B))
        A_ahead += 1 if wins_A > wins_B else 0
        B_ahead += 1 if wins_B > wins_A else 0
    return numpy.asarray(wins), A_ahead, B_ahead
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('{:s} <n> [<k>]'.format(sys.argv[0]))
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 1 

    wins, A_ahead, B_ahead = simulate_coin_tosses(n, k)
    print("A was ahead {} times".format(A_ahead))
    print("B was ahead {} times".format(B_ahead))
    print("Remise {} times".format(n-A_ahead-B_ahead))
    plot.boxplot(wins)
    plot.xticks([1,2], ['Wins A', 'Wins B'])
    plot.show()
