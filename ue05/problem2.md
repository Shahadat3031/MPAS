% MPAS - Exercise 5
% Problem 2
$$p(x) = \begin{cases}
    \frac{\alpha^x}{x!}e^{-\alpha}, & x = 0,1,\dots \\
    0,                              & \text{sonst}
\end{cases}$$

* 12 Autos/Stunde (Poisson-Verteilt mit $\alpha = 12$)
* Service-Time $\frac{1}{15}$ Stunden (normalverteilt mit $\mu = \frac{1}{15}, \sigma = \frac{1}{45}$)
* $E(xy) = E(x)E(y) = 12 \cdot \frac{1}{15} = \frac{4}{5}$

Stand irgendwie an der Tafel
$$L = p \frac{p^2 (1 + \sigma^2 \mu^2)}{2(1-p)} = 2.57$$

NG-Warteschleife ⇒ Normalverteilt
