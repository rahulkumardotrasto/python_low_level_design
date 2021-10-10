from abc import ABC, abstractmethod


class Parent(ABC):
    def common(self):
        print("In common method  of Parent")

    @abstractmethod
    def vary(self):
        pass


class Child1(Parent):
    def vary(self):
        print("In vary method of Child1")


class Child2(Parent):
    def vary(self):
        print("In vary method of Child2")
