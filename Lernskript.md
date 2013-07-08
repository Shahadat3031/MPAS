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

