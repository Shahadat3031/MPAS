#!/usr/bin/env python3
import random
import sys
from queue import PriorityQueue
import numpy as np
import matplotlib.pyplot as plt

MECHANIC_ARRIVAL = 0
MECHANIC_SERVICE = 1
ARRIVAL_MEAN = 4
SERVICE_MEAN = 3

class Control(object):
    def __init__(self, queue):
        self.time = 0
        self.attendants = set()
        self.queue = queue
        self.total_mechanics_payments = 0
        self.runtime = None

    def dispatch(self,event):
        event.dst.handle_event(event)

    def run(self):
        while not self.queue.empty():
            event = self.queue.next_event()
            time = event.time
            if self.runtime == None or time <= self.runtime:
                self.dispatch(event)
            else:
                break
    
    def get_total_payments(self):
        return self.time / 5.0 * len(self.attendants) + ( # 1/5 EUR/min = 12 EUR/h
                self.total_mechanics_payments
            )

    def set_run_time(self, runtime):
        self.runtime = runtime

    def schedule(self, event, delta = 0):
        event.time += delta
        self.queue.schedule(event)

class Queue(object):
    class QueueIterator:
        def __init__(self, queue):
            self.queue = queue
            self.idx = -1

        def __iter__(self):
            return self

        def __next__(self):
            if self.idx+1 < len(self.queue):
                self.idx += 1
                return self.queue[self.idx]
            else:
                raise StopIteration

    def __init__(self):
        self.queue = PriorityQueue()

    def schedule(self, event):
        self.queue.put(event)

    def next_event(self):
        return self.queue.get()

    def empty(self):
        return self.queue.empty()

    def __str__(self):
        return str(self.queue.queue)

    def __len__(self):
        return len(self.queue.queue)

    def __getitem__(self, key):
        return self.queue.queue[key]

    def __iter__(self):
        return Queue.QueueIterator(self)

class Event(object):
    def __init__(self, type, dst, time = 0, src = None):
        self.time = time
        self.type = type
        self.src = src
        self.dst = dst

    def __lt__(self, other):
        return self.time < other.time

class MechanicArrival(Event):
    def __init__(self, dst, time = 0, src = None):
        super(MechanicArrival,self).__init__(MECHANIC_ARRIVAL, dst, time, src)

class MechanicService(Event):
    def __init__(self, dst, time = 0, src = None):
        super(MechanicService,self).__init__(MECHANIC_SERVICE, dst, time, src)

class Entity(object):
    def __init__(self, control):
        self.control = control
        self.payment = 0
    
    def handle_event(self, event):
        pass

class ToolCripAttendant(Entity):
    def __init__(self, control):
        super(ToolCripAttendant,self).__init__(control)
        self.control.attendants |= {self}
        self.next_free_time = 0

    def __lt__(self, other):
        return self.next_free_time < other.next_free_time

    def handle_event(self, event):
        if event.type == MECHANIC_SERVICE:
            self.control.total_mechanics_payments += event.src.payment
        else:
            raise ValueError()

class Mechanic(Entity):
    def schedule_service_event(self, arrival_event):
        next_free_attendant = min(self.control.attendants)
        service_start = max(arrival_event.time, next_free_attendant.next_free_time)
        service_end = service_start + random.expovariate(1/SERVICE_MEAN)
        next_free_attendant.next_free_time = service_end
        self.control.schedule(MechanicService(src=self, dst=next_free_attendant, time=service_start))
        self.payment += (service_end - arrival_event.time)/6.0  # 1/6 EUR/min = 10 EUR/h

    def handle_event(self, event):
        if event.type == MECHANIC_ARRIVAL:
            next_arrival = event.time + random.expovariate(1/ARRIVAL_MEAN)
            self.control.schedule(MechanicArrival(dst=Mechanic(self.control), time=next_arrival))
            self.schedule_service_event(event)
        else:
            raise ValueError()

def run_simulation(number_attendants):
    queue = Queue()
    control = Control(queue)
    control.set_run_time(runtime)
    for _ in range(number_attendants):
        ToolCripAttendant(control)
    queue.schedule(MechanicArrival(dst=Mechanic(control), time=0))
    control.run()
    return control.get_total_payments()

def plot(payments, runtime):
    data = [np.asarray(p) for p in payments]
    xlabels = ["{} Attendant(s)".format(i+1) for i,_ in enumerate(payments)]
    plt.xticks([i+1 for i, _ in enumerate(payments)], xlabels)
    plt.title("Payments ({} min., {} rep.)".format(runtime, len(payments[0])))
    plt.boxplot(data,0,'')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: {} <repetitions> <runtime in minutes> [<max_number_attendants>]'.format(sys.argv[0]),file=sys.stderr)
        sys.exit(1)
        
    repetitions = int(sys.argv[1])
    runtime = int(sys.argv[2])
    max_number_attendants = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    
    results = [] 

    for number_attendants in range(1, max_number_attendants+1):
        results.append([])
        for i in range(repetitions):
            total_payments = run_simulation(number_attendants)
            results[number_attendants-1].append(total_payments)
            if (i*number_attendants) % 1000 == 0:
                print("Number of attendants = {}, Repetition = {}".format(number_attendants,i+1))
    plot(results,runtime)
