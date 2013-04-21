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
Die Ergebnisse von 1000 Durchläufen von Simulationen mit den geforderten Werten
lassen wir uns in zwei CSV-Dateien ausgeben. Eine für die Ausführungszeiten
und eine für die Differenzen zu Pi.
Diese lesen wir dann mit R ein
```{r}
<<read-ue01-3-data>>
```
und lassen uns Box-and-Whisker-Plots für die Ausführungszeit
```{r plot-time, result="asis", fig.cap="Ausführungszeit der Monte-Carlo-Simulation"}
<<plot-ue01-3-data-time>>
```
und für die Differenz zu $\pi$ ausgeben.
```{r plot-diff, result="asis", fig.cap="Differenz zu Pi des Ergebnisses der Monte-Carlo-Simulation"}
<<plot-ue01-3-data-diff>>
```

Problem 4: Dynamische kontinuierliche Simulation
------------------------------------------------
~~~python
~~~
