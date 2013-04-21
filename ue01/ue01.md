% Modeling and Performance Analysis with Simulation
% Martin Lenders (4206090)

Übung 1
=======

Problem 1: Komponenten eines Systems
------------------------------------

Problem 2: Prozess einer Simulatiosstudie
-----------------------------------------

Problem 3: Monte Carlo Simulation
---------------------------------
~~~python
import random

shots = 0
hits = 0

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
    for i in range(iterations):
        x,y = shoot()
        if is_hit(x,y):
            hits += 1
    return hits/shots*4
~~~

Problem 4: Dynamische kontinuierliche Simulation
------------------------------------------------
~~~python
~~~
