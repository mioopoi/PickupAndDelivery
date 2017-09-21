
from global_parameters import *

class Courier:
    def __init__(self, identifier, location, capacity=CAPACITY, load=0):
        """Initialize a courier/delivery man.
        :param identifier: id of the courier
        :param location: current location of the courier
        :param capacity: the capacity of the courier (largest number of parcels the courier can carry simultaneously)
        :param load: current number of parcels carried by the courier

        :type identifier: int
        :type capacity: int
        :type load: int
        """
        self.identifier = identifier
        self.location = location
        self.capacity = capacity
        self.load = load

        # the schedule of the courier (a sequence of queries that the courier should process one by one)
        self.schedule = None
        """:type : list[ScheduleNode]"""

        # the route of the courier to go to the first node in his schedule
        self.route = None
