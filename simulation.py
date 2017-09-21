

from zone import Zone, Merchant

import random


class Simulation:
    def __init__(self):
        self.zone = Zone(100, 100)

        self.merchants = {}
        self.init_merchants(20)

        self.order = {}


    def init_merchants(self, num):
        """Initialize the merchants. Merchants will not change its location at any time.
        :param num: number of merchants
        :return: None
        :type num: int
        """
        length = self.zone.length
        width = self.zone.width
        assert num > 0, "number of merchants must be greater than 0"
        assert num <= length * width, "number of merchants exceeds the capacity of the zone"

        occupied_locations = set()
        for i in range(num):
            x = random.randint(0, width - 1)
            y = random.randint(0, length - 1)
            location = (x, y)
            while location in occupied_locations:
                x = random.randint(0, width - 1)
                y = random.randint(0, length - 1)
                location = (x, y)
            self.merchants[i] = Merchant(i, location)
            occupied_locations.add(location)