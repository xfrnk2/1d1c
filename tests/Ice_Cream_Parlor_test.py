import os
import sys

from src.hackerrank.Problem_Solving.Ice_Cream_Parlor import icecreamParlor


class TestClass(object):
    def test_func(self):
        assert icecreamParlor(200, [150, 24, 79, 50, 88, 345, 3]) == (1, 4), "연산을 잘 수행한다"
