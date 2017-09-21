

class ScheduleNode:
    def __init__(self, order_id, is_origin):
        """Initialize a schedule node (for inserting into the schedule of a courier).
        :param order_id: id of corresponding order of the schedule node
        :param is_origin: bool param indicates that if the schedule node is an origin of an order or not

        :type order_id: int
        :type is_origin: bool
        """
        self.order_id = order_id
        self.is_origin = is_origin


class Dispatcher:
    def __init__(self):
        pass