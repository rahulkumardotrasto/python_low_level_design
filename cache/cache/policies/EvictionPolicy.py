from abc import ABC


class LRUEvictionPolicy(ABC):
    def keyAccessed(self, key):
        pass

    def keyAccessed(self):
        pass
