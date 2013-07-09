% MPAS — Lernskript
% Martin Lenders

Einleitung
==========
Random Waypoint Model (RWM)
---------------------------
* assumption: Movement area = rectangle without obstacles
* node selects uniformly for every iteration a point $p = (x,y)$ in the area
* node selects uniformly for every iteration a velocity $v \in [v_{\min}, v_{\max}]$
* fixed pause time $t_{\mathrm{pause}}$
* algorithm for every node:
    * wait $t_{\mathrm{pause}}$
    * move to $p$ with velocity $v$
    * repeat

Systems
-------
* **Definition [*System*]:** group of objects joined in regular interaction 
    or interdependence towards accomplishment of some purpose
* **Definition [*System environment*]:** not in the specific system, 
    affecting the system
* boundaries depend on *purpose* of study but must be decided beforehand
* components:
    * **entity:** objects of interest in a system
    * **attribute:** property of an entity
    * **activity:** time period of specified length
    * **system state:** collection of variables necessary to describe 
        the system at any time
    * **event:** *instantaneous* occurence that might change the system
        state
    * **endogenous:** activities and events within system
    * **exogenous:** activities and events in system environment affecting
        the system
* **Definition[discrete system]:** state variables change at 
    discrete set of points in time
* **Definition[continuous system]:** system change continuously over
    time

Models
------
* **Definiton[*Models*]:** representation of system for purpose of
    system study
* types:
    * physical model
    * mathematical model
        - simulation model
            + **static:** system at particular point in type $\Leftrightarrow$ **dynamic:** representing system over time interval
            + **deterministic:** without random variables $\Leftrightarrow$ **stochastic:** with random variables
            + **discrete** $\Leftrightarrow$ **continuous**
* Monte-Carlo simulations: static, stochastic
* discrete-event simulations (focus of class): dynamic, stochastic, discrete

Performance Metrics
-------------------
* Request for service from system
    * done?
        * done correctly?
            * **time** (response time), **rate** (throughput), **resources** (utilization)
        * done incorrectly?
            * **propability** of error $j$
            * **time between occurences** of error $j$
    * cannot do?
        * **duration** of triggering event $k$
        * **time between occurences** of triggering event $k$ 
* what is best depends on metric:
    * low is better (e.g. letancy)
    * high is better (e.g. throughput)
    * nominal is better (e.g. rtt for specific protocols)

Steps of simulation study
-------------------------
* Phase 1: Discovery and orientation:
     1. **problem formulation**
     2. **settings of objective and overall plan**
* Phase 2: Model building and data collection:
     3. **model conceptualization** and **data collection**
     4. **model translation**
     5. **verification** (if not suitable: repeat at 4)
     6. **validation** (if results not realistic: repeat at 3)
* Phase 3: Model running
     7. **experimental design**
     8. **production runs and analysis**
     9. **decide if more runs necassary** (if yes: repeat at 7 or 8)
* Phase 4: Implementation
    10. **documentation and reporting**
    11. **impementation**

Validation is most crucial step!

Simulation methods
==================
Table method
------------
* Manually fill up table (or automate via spreadsheet)
* $x_{ij}$: Input, $y_i$: Result of repetition $i$
    1. determine characteristics of each input to simulation
    2. construct simulation table (see below)
    3. generate values for $x_{ij}$ for every $i$ and $j$ and calculate
        $y_i$

------------------------------------------------
$i$   $x_{i1}$ $x_{i2}$ $\dots$  $x_{ip}$ $y_i$
----- -------- -------- -------- -------- ------
$1$

$2$

$...$

$n$
------------------------------------------------

Queueing systems
----------------
* queueing system described by
    * calling population
    * arrival rate
    * service mechanism
    * system capacity
    * queuing discipline

General principles
==================
Concepts of discrete-event simulation
-------------------------------------
* **Definition[*Activity*]:**
    + unconditional wait
    + end of activity: primary event (placed in FEL)
* **Definition[*Delay*]:**
    + conditional wait
    + completion of delay: secondary event (placed elsewhere [e.g. secondary queues])
* **Definition[*System snapshot*]**: include
    + system state
    + status of all entities
    + status of all sets of entities
    + FEL
    + statistics

World views
-----------
* Event scheduling:
    + events are executed
    + variable time advance between events
* Process-interaction:
    + processes = lifetimes of entities are executed
    + processes interact 
    + process = time-sequenced list of events, activities and delays + demand for resources
    + variable time advance during processes
* activity scanning:
    + checking for conditions of activities at each clock cycle
    + fixed time advance
    + disadvantage: slow runtime
* three-phase approach (hybrid of activity scanning / event scheduling):
    + events = activities of duration 0
    + two types of activities:
        * **B activities:** activities bound to occur (primary events
          and unconditianal activities)
        * **C activities:** activities bound to certain conditions
          (secondary events, conditional activities)
      $\Rightarrow$ B-type in FEL, activity scanning for C-type

Object-oriented simulation framework
------------------------------------
* module {rng}
    - **RNG**
        + getNext()
    - **Exponential** extends **RNG**
        + lambda : **double**
        + uniform : **random**
        + Constructor()
        + getNext()
    - **Uniform** extends **RNG**
        + max : **double**
        + min : **double**
        + uniform : **random**
        + Constructor()
        + getNext()
* module {core}
    - **Control**
        + queue : **Queue**
        + system_time : **double**
        + Constructor(**Queue**)
        + run()
        + setRunTime(**double**)
    - **Queue**
        + schedule(**Event**)
        + getNextEvent()
        + dump()
    - **Event**
        + arrival_time : **double**
        + type : **int**
        + src : **Entity**
        + dst : **Entity**
        + Constructor(**double**, **Entity**)
        + Constructor(**double**, **Entity**, **Entity**)
    - **Entity**
        + Constructor(**Control**)
        + handleEvent(**Event**)

Simulation graphs
-----------------
* Nodes: Event or state transition
    * state variables and changes annotated in $\{\}$ as node label
* Edges: Scheduling of events by
    * boolean conditions $(i)$
    * time delay $t$
    * parameters for node instance (box on edge)
    * pointed edges to show cancelation of events

Network simulators
==================
Tools
-----
* ns-2
* OMNeT++
* SSFNet (standard, not implementation)
* Parsec (simulation language)
* OPNET
* JiST/SWANS
* BRITE
* Akaroa


Statistical models in simulation
================================
Basic Propability Theory Concepts
---------------------------------
* discrete random variables distributed by **probability mass function (PMF)** $p(x_i)$
* continuous random variables distributed by **probability density function (PDF)** $f(x)$
* **cumulative distribution function (CDF)** $F(x) = \mathbf{Pr}(X \leq x)$
    + $X$ is discrete: 
        $$F(x) = \sum\limits_{x_i \leq x} p(x_i)$$
    + $X$ is continuous:
        $$F(x) = \int\limits^x_{-\infty} f(t)\ dt$$
    + $\forall a \leq b: \mathbf{Pr}(a \leq X \leq b) = F(b) - F(a)$
* **Expacted value** $E(X) = \mu = m = $ mean = 1st moment of $X$ 
    + $X$ is discrete:
        $$E(X) = \sum\limits_{i \in \{0,1,\dots\}} x_i p(x_i)$$
    + $X$ is continuous:
        $$E(X) = \int\limits_{-\infty}^{\infty} x f(x)\ dx$$ 
* **Variance** $V(X) = \mathit{Var}(X) = \sigma^2$
    + measurment of spread or variation of $X$
    $$V(X) = E((X - E[X])^2) = E(X^2) - (E[X])^2$$
* **Standard deviation (SD)** $\sigma$
    $$\sigma = \sqrt{V(x)}$$
* **Coefficient of variation** ($C.O.V.$)
    $$C.O.V. = \frac{\sigma}{\mu}, \mu > 0$$
* **Covariance** ($\mathrm{Cov}(X,Y)$), 0 if $X$ and $Y$ independent
    $$\mathrm{Cov}(X,Y) = E(XY) - E(X) E(Y)$$ 
* **Correlation** ($\mathrm{Corr}(X,Y)$) normalized (between -1 and 1) value of covariance
    $$\mathrm{Corr}(X,Y) = \rho_{XY} = \frac{\sigma_{XY}^2}{\sigma_x \sigma_y}$$
* $x$ value at which CDF takes value $\alpha$: **$\alpha$-quantile** or **$(100 \cdot \alpha)$-percentile**
* **Median** = 0.5-quantile
* **Mode:** most likely value
* Selecting central tendancy:
    * data categorical? $\Rightarrow$ **mode**
    * total of interest? $\Rightarrow$ **mean**
    * distribution skewed? $\Rightarrow$ **median**
    * else: **mean**

Discrete distributions
----------------------
* Bernoulli distribution
* Binomial distribution
* Geometric distribution
* Negative Binomial distribution
* Poisson distribution

Continuous distributions
------------------------
* Uniform distribution
* Exponential distribution
* Weibull distribution
* Normal distribution
* Lognormal distribution

Random number generators
========================
Pseudo-random numbers
---------------------
* produce sequence of numbers in $[0,1]$, simulating or imitating ideal
  properties of random numbers
   + Uniformaty
   + Independence

Generating random numbers
-------------------------
### Midsquare method
* von Neumann, Metropolis in 1940s
* start with four digit positive integer $Z_0$
* compute $Z_0^1 = Z_0 \times Z_0$ $\Rightarrow$ eight digit integer
* Take middle four digits for next four-digit number
$$U_i = \frac{Z_i}{1000}$$
* Problem: tends to 0

### Linear congruential method
* Assumption $m > 0$ und $a < m, c < m, X_0 < m$:
    $$X_{i+1} = (aX_i + c) \mod m, \qquad i = 0,1,2,...$$
* $X_i \in [0, m-1]$\
  $\Rightarrow R_i = \frac{X_i}{m}, i = 1,2,...$
* Hull and Dobell, 1962: LGC has full period if and only if
    1. greatest common divisor of $m$ and $c$ is 1
    2. if $q$ is a prime number that divides $m$, then $q$ divides $a$
    3. if 4 divides $m$, then 4 divides $a-1$

### General congruential generators
$$X_{i+1} = g(X_i, X_{i-1}, ...) \mod m$$

* $g()$ depends on generator
    - quadratic congruential generator $g(X_i, X_{i-1}) = aX_i^2 + bX_{i-1} + c$
    - multiple recursive generators $g(X_i, X_{i-1}, ..., X_{i-k}) = a_1 X_i + a_2 X_{i-1} + ... + a_k X_{i-k}$
    - fibonacci generator $g(X_i, X_{i-1}) = X_i + X_{i-1}$

### Combined linear congruential method
* Longer period generators needed\
    $\Rightarrow$ Combine two or more multiplicative congruential generators
  $$X_{i+1,j} = (a_jX_i+c_j) \mod m_j$$
* suggested, that
  $$X_i = \left(\sum_{j=1}^k (-1)^{j-1} X_{i,j}\right) \mod m_1 - 1$$
  and
  $$R_i = \begin{cases}
    \frac{X_i}{m_1},    & X_i > 0 \\
    \frac{m_1-1}{m_1},  & X_i = 0
  \end{cases}$$

Tests for random numbers
------------------------
* Test for uniformaty
    + compare uniform distribution with empirical distribution of 
      generated numbers
    + Kolmogorov-Sminrnov Test (cdf)
    + Chi-square Test (expected value)
* Test for autocorrelation
    + autocorrelation $\rho_{i,m}$ between $R_i, R_{i+m}, R_{i+2m}, ...,
      R_{i+(M+1)m}$
        - $m$ = lag
        - $M$: largest integer such that $i+(M+1)m \leq N$

Random-variate generation
=========================
Inverse-tranform technique
--------------------------
* compute CDF $F(X)$ of desired random variable $X$
* set $F(X) = R$ on the range of $X$
* solve equation $F(X) = R$ for $X$ in terms of $R$
* generate uniform random numbers $R_1, R_2, R_3, ...$ 
  and compute desired random variate by $X_i = F^{-1}(R_i)$
 
Acceptance-rejection technique
------------------------------
* generate $R$ and accept/decline according to rule

Queueing Models
===============
Characteristics of queueing models
----------------------------------
* **customers:** served entities
* **servers:** serving entities
* **calling population:** population of potential customers
    + *finite* or *infinite*
* **system capacity:** slots in queque
    + *limited* or *unlimited*
* **pending:** customer is outside the queueing system
* **runtime of a customer:** time from departure to reentry into 
  queueing system 
* Queue behavior:
    + Balk: leave when line too long
    + Renege: leave when line moves too slowly
    + Jockey: move from one line to shorter line
* Queue discipline:
    + FIFO, LIFO, SIRO (service in random order), SPN, PR (according to
      priority)

Queueing notation — Kendall notation
------------------------------------
* notation for parallel server queues: $A/B/c/N/K$
    + $A$ interarrival-time distribution
    + $B$ service-time distribution
    + $c$ number of parallel servers
    + $N$ system capacity
    + $K$ size of calling population
    + $N,K$ dropped if infinite
    + may be extended by queuing discipline
* Symbols for $A$ and $B$
    + $M$ Markov, exponential distribution
    + $D$ Constant, deterministic
    + $E_k$ Erlang distribution of order $k$
    + $H$ Hyperexponential distribution
    + $G$ General, arbitrary

Long run measures of performance of queueing systems
----------------------------------------------------
* general performance measures of queueing system
    + $P_n$ steady-state propability of having $n$ customers in system
    + $P_n(t)$ propability of $n$ customers in system at time $t$
    + $\lambda$ arrival rate
    + $\lambda_e$ effective arrival rate
    + $\mu$ service arrival rate
    + $\rho$ server utilisation
    + $A_n$ interarrival time between customers $n-1$ and $n$
    + $S_n$ service time of the $n$-th arriving customer
    + $W_n$ total time spent in system by the $n$-th customer
    + $W_n^Q$ total time spent in waiting line by customer $n$
    + $L(t)$ the number of customers in system at time $t$
    + $L_Q(t)$ the number of customers in queue at time $t$
    + $L$ long-run time-average number of customers in system
    + $L_Q$ long-run time-average number of customers in queue
    + $W$ long-run average time spent in system per customer
    + $w_Q$ long-run average time spent in queue per customer 
* primary long-run measures:
    + $L, L_Q, W, w_Q, \rho$

The Conservation Equation: Little's Law
---------------------------------------
$$\hat L = \hat \lambda \hat w$$

* $\hat L$ Average number of customers in system
* $\hat \lambda$ Arrival rate
* $\hat w$ Average system time
* $L = \lambda w$ as $T \to \infty$ and $N \to \infty$

Input modeling
==============
Data collection
---------------

Identifying the distribution with data
--------------------------------------

Parameter estimation
--------------------

Goodness-of-fit tests
---------------------

Fitting a non-stationary poisson process
----------------------------------------

Selecting input models without data
-----------------------------------

Multivariate and time-series input data
---------------------------------------

Output analysis for a single model
==================================
Types of simulation
-------------------

Stochastic nature of output data
--------------------------------

Measures of performance
-----------------------

Output analysis for terminating simulations
-------------------------------------------

Output analysis for steady-state simulations
--------------------------------------------
