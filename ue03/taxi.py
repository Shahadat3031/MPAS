#!/usr/bin/env python3
import sys
import random
import bisect
from collections import Hashable
import numpy as np
import matplotlib.pyplot as plt

def weighted_choice(value_weight_list):
    total = 0
    cummulativ_weights = []
    for _, w in value_weight_list:
        total += w
        cummulativ_weights.append(total)
    x = random.uniform(0, total)
    i = bisect.bisect(cummulativ_weights, x)
    return value_weight_list[i][0]

class Time(object):
    def __init__(self, day, hour, minute):
        hour = int(hour) + int(minute) // 60
        
        self.minute = int(minute) % 60
        self.hour = hour % 24
        self.day = int(day) + hour // 24
    
    def __hash__(self):
        return self.day*1440 + self.hour*60 + self.minute

    def __add__(self, minutes):
        return Time(self.day, self.hour, self.minute+minutes)

    def __sub__(self, t):
        minutes = self.day*1440 - t.day*1440
        minutes += self.hour*60 - t.hour*60
        minutes += self.minute - t.minute
        return minutes

    def __eq__(self, t):
        return (self.day, self.hour, self.minute) == \
                (t.day, t.hour, t.minute)

    def __ne__(self, t):
        return not (self == t)

    def __gt__(self, t):
        return (self.day, self.hour, self.minute) > \
                (t.day, t.hour, t.minute)

    def __ge__(self, t):
        return not (self < t)

    def __lt__(self, t):
        return (self.day, self.hour, self.minute) < \
                (t.day, t.hour, t.minute)

    def __le__(self, t):
        return not (self > t)

    def __str__(self):
        return "Tag {:d} {:02d}:{:02d}".format(
                self.day, 
                self.hour, 
                self.minute
            )

    def __repr__(self):
        return "<"+str(self)+">"

TIMES_BETWEEN_CALLS = [(15,14),(20,22),(25,43),(30,17),(35,4)]
SERVICE_TIMES = [(5,12),(15,35),(25,43),(35,6),(45,4)]
START_TIME = Time(day=1, hour=9, minute=0)
END_TIME = Time(day=5, hour=17, minute=0)

def weighted_choice(value_weight_list):
    total = 0
    cummulativ_weights = []
    for _, w in value_weight_list:
        total += w
        cummulativ_weights.append(total)
    x = random.uniform(0, total)
    i = bisect.bisect(cummulativ_weights, x)
    return value_weight_list[i][0]
 
class Control(object):
    def __init__(self, event_queue):
        self.event_queue = event_queue
        self.dismissed_customers = 0
        self.waiting_times = []
        self.taxis = []

    def run(self):
        time = START_TIME
        while not self.event_queue.is_empty() and time < self.end_time:
            event = self.event_queue.get_next_event(time)
            while event != None:
                self.dispatch(event)
                event = self.event_queue.get_next_event(time)
            time += 1
    
    def add_taxis(self, taxis):
        self.taxis += taxis

    def dispatch(self, event):
        event.dst.handle_event(event)

    def set_run_time(self, run_time):
        self.end_time = run_time

    def schedule(self, event, delta=0):
        event.time += delta
        self.event_queue.schedule(event)

class Entity(object):
    def __init__(self, control, id):
        self.control = control
        self.id = id
    
    def __str__(self):
        return type(self).__name__+" "+str(self.id)
    
    def __repr__(self):
        return '<'+str(self)+'>'

    def handle_event(self, event):
        pass

class Customer(Entity):
    last_id = 0
    
    def __init__(self, control):
        Customer.last_id += 1
        super(Customer, self).__init__(control, Customer.last_id)
        self.service_time = weighted_choice(SERVICE_TIMES)

    def handle_event(self, event):
        if isinstance(event, Call):
            self.calling_time = event.time
            dispatched_taxi = min(
                    self.control.taxis, 
                    key=lambda taxi: taxi.next_free_time
                )
            
            taxi_avail_time = max(
                    dispatched_taxi.next_free_time,
                    self.calling_time
                )
            
            if taxi_avail_time.day != event.time.day:
                self.control.dismissed_customers += 1
            else:
                drive = Drive(
                        dst=dispatched_taxi, 
                        src=self, 
                        time=taxi_avail_time
                    )
                self.control.schedule(drive)

                dispatched_taxi.next_free_time = taxi_avail_time + self.service_time
                if dispatched_taxi.next_free_time > Time(event.time.day, 17, 00):
                    next_free_time = START_TIME + 1440
                    dispatched_taxi.next_free_time = next_free_time
                    
            new_customer = Customer(self.control)
            next_call = Call(new_customer, event.time)
            self.control.schedule(next_call)
        else:
            raise ValueError("Customers can not handle {} events".\
                    format(type(event).__name__)
                )

class Taxi(Entity):
    last_id = 0
    def __init__(self, control):
        Taxi.last_id += 1
        super(Taxi, self).__init__(control, Taxi.last_id)
        self.next_free_time = START_TIME

    def handle_event(self, event):
        if isinstance(event, Drive):
            calling_time = event.src.calling_time
            event.src.waiting_time = event.time - calling_time
            self.control.waiting_times.append(event.src.waiting_time)
        else:
            raise ValueError("Taxis can not handle {} events".\
                    format(type(event).__name__)
                )

class Event(object):
    def __init__(self, dst, src=None, time=0):
        self.dst = dst
        self.src = src
        self.time = time

    def __str__(self):
        return type(self).__name__+"("+str(self.dst)+","+str(self.src)+","+str(self.time)+")"

    def __repr__(self):
        return "<"+str(self)+">"

class Call(Event):
    def __init__(self, customer, last_call_time=START_TIME):
        self.dst = customer
        self.src = None
        self.time = last_call_time + weighted_choice(TIMES_BETWEEN_CALLS)
        if self.time > Time(day=self.time.day, hour=17, minute=0):
            self.time += 16*60

class Drive(Event):
    pass

class Queue(object):
    def __init__(self):
        self.queue = {}

    def schedule(self, event):
        if event.time not in self.queue:
            self.queue[event.time] = []
        self.queue[event.time].append(event)

    def get_next_event(self, time):
        if time not in self.queue:
            return None

        next_event_queue = self.queue[time]
        if len(next_event_queue) == 1:
            del self.queue[time]
            return next_event_queue[0] 
        else:
            next_event = next_event_queue[0]
            del next_event_queue[0]
            return next_event

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return '\n'.join(','.join(
                [str(q) for q in self.queue[i]]) for i in sorted(self.queue)
            )

def run_simulation(num_taxis):
    queue = Queue()
    control = Control(queue)
    taxis = [Taxi(control) for _ in range(num_taxis)]
    control.add_taxis(taxis)

    first_customer = Customer(control)
    first_call = Call(first_customer)
    control.schedule(first_call)

    control.set_run_time(END_TIME)
    control.run()

    return control.dismissed_customers, control.waiting_times

def plot_avg_waiting_times(figure, avg_waiting_times):
    ax = fig.add_subplot(121,title="Avg. waiting time ({} rep.)".format(len(avg_waiting_times[1])))
    ax.boxplot([
            np.asarray(avg_waiting_times[1]),
            np.asarray(avg_waiting_times[2])
        ])

def plot_dismissed_customers(figure, dismissed_customers):
    ax = fig.add_subplot(122,title="Dismissed cust. ({} rep.)".format(len(dismissed_customers[1])))
    ax.boxplot([
            np.asarray(dismissed_customers[1]),
            np.asarray(dismissed_customers[2])
        ])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <repetions>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    dismissed_customers = {1: [], 2: []}
    avg_waiting_times = {1: [], 2: []}

    for i in range(int(sys.argv[1])):
        print("Iteration {}".format(i+1))
        for num_taxis in 1,2:
            d, w = run_simulation(num_taxis)
            dismissed_customers[num_taxis].append(d)
            avg_waiting_times[num_taxis].append(sum(w)/len(w))
    
    fig = plt.figure()
    
    plot_avg_waiting_times(fig, avg_waiting_times)
    plot_dismissed_customers(fig, dismissed_customers)

    plt.show()
