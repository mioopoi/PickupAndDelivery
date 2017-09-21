

from dispatcher import ScheduleNode


# === Query status ===
WAITING = "waiting"       # the order is waiting for a courier to pickup
CANCELLED  = "cancelled"  # the order has been cancelled
SENDING = "sending"       # the order is under sending
DONE = "done"             # the order is finished


class Order:
    def __init__(self, identifier, birth_time, origin, destination):
        """Initialize an order.
        :param identifier: id of the order
        :param birth_time: timestamp that the order generate
        :param origin: location of the origin
        :param destination: location of the destination

        :type identifier: int
        :type birth_time: int
        :type origin: tuple[int, int]
        :type destination: tuple[int, int]
        """
        self.identifier = identifier
        self.birth_time = birth_time
        self.origin = origin
        self.destination = destination

        self.o_schedule_node = ScheduleNode(self.identifier, True)
        self.d_schedule_node = ScheduleNode(self.identifier, False)

        self.status = WAITING  # type: str
        self.waiting_time = 0  # type: int
        self.matched_courier = None  # type: int
        self.sending_time = 0  # type: int

    def update_status(self):
        if self.status == WAITING:
            self.waiting_time += 1
        elif self.status == SENDING:
            self.sending_time += 1
