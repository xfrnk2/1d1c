# coding=utf-8

from uuid import uuid4

from game_object import GameObject
from event import Event
from renderer import Renderer
from timer import Timer
from field import LogicField


class PuYo(GameObject):
    def __init__(self, container: LogicField):
        self.__id = uuid4()
        self.__container = container

        self.__x = 6
        self.__y = 20
        self.__data = '⦿'

        self.__speed = 1
        self.__valid = True
        self.__visible = True

    def update(self, event: Event):
        if self.__valid:
            y = self.__y
            y -= self.__speed * Timer.get_elapsed()
            y = max(y, 0)

            position = (self.x, int(y))
            if self.__container.already_exist(position, self):
                self.valid = False
                return

            self.__y = y
            if int(self.__y) == 0:
                self.valid = False

    def render(self):
        if self.__visible:
            Renderer.render(self.__data, self.position)

    @property
    def valid(self) -> bool:
        return self.__valid

    @valid.setter
    def valid(self, valid):
        self.__valid = valid

    @property
    def id(self) -> str:
        return self.__id

    @property
    def position(self) -> tuple:
        return int(self.__x), int(self.__y)

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]
