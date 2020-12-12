from collections import namedtuple
import queue
import random
import argparse

Event = namedtuple('Event', 'time proc action')

SEARCH_DURATION = 5  # Max Default Search duration for passengers
TRIP_DURATION = 20  # Max Default Trip duration
DEFAULT_NUM_TAXIS = 3
DEPARTURE_INTERVAL = 5
DEFAULT_END_TIME = 90


def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change
    """
    time = yield Event(start_time, ident, 'leave garage')

    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')
    # end of taxi process


class Simulator:

    def __init__(self, proc_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(proc_map)

    def run(self, end_time):
        """main method to drive the simulation
        """
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        # main loop for driving the coroutines
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            curr_event = self.events.get()
            sim_time, proc, previous_action = curr_event
            print('taxi:', proc, proc * '  ', curr_event)
            activ_proc = self.procs[proc]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = activ_proc.send(next_time)
            except StopIteration:
                del self.procs[proc]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def compute_duration(previous_action):
    """Randomly compute the each taxi event time
    """
    if previous_action in ['leave garage', 'drop off passenger']:
        # taxi is in prowling state
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # trip duration
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        # time to go home
        interval = 1
    else:
        raise ValueError('Unknown previous action %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1


def main(num_taxis=DEFAULT_NUM_TAXIS, end_time=DEFAULT_END_TIME,
         seed=None):
    if seed is not None:
        random.seed(seed)  # get reproducable results
    taxis = {i: taxi_process(i, (i+1) * 2, i * DEPARTURE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                         default=DEFAULT_END_TIME, help='simulation end time; default = %s'
                         % DEFAULT_END_TIME)
    parser.add_argument('-t', '--num-taxis', type=int,
                         default=DEFAULT_NUM_TAXIS, help='num of taxis in sim; default = %s'
                         % DEFAULT_NUM_TAXIS)
    parser.add_argument('-s', '--seed', type=int,
                         default=None, help='random seed for sim')

    args = parser.parse_args()
    main(args.end_time, args.num_taxis, args.seed)

