from abc import ABC


class Storage(ABC):
    def add(self, key, value):
        pass

    def remove(self, key):
        pass

    def get(self, key):
        pass
