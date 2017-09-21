"""
Author: Huafan Li <huafan@seu.edu.cn>
Date of creation: 2017/9/21

"""


class Merchant:
    def __init__(self, identifier, location):
        """Initialize a merchant.
        :param identifier: identifier of a merchant
        :param location: location

        :type identifier: int
        :type location: tuple[int, int]
        """
        self.identifier = identifier
        self.location = location


class Zone:
    def __init__(self, length, width):
        """Initialize the city.
        :param length: the length of the zone
        :param width: the width of the zone
        :type length: int
        :type width: int
        """
        assert length > 0 and width > 0, "length and width of zone must be greater than 0"

        self.length = length
        self.width = width
        self.matrix = [[0 for col in range(length)] for row in range(width) ]
        self.anchor = ((width-1)/2, (length-1)/2)  # centre of the zone, assume the home of the couriers locates here


class Path:
    def __init__(self):
        pass