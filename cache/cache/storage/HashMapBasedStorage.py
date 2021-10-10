from cache.exceptions import NotFoundException
from cache.exceptions import StorageFullException
import Storage


class HashMapBasedStorage(Storage):
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__storage = {}

    def add(self, key, value):
        if self.isStorageFull():
            raise StorageFullException('Capacity Full.....')
        self.__storage[key] = value

    def remove(self, key):
        if key not in self.__storage:
            raise NotFoundException(key + 'doesnt exist in cache.')
        del self.__storage[key]

    def get(self, key):
        if key not in self.__storage:
            raise NotFoundException(key + 'doesnt exist in cache.')
        return self.__storage[key]

    def isStorageFull(self):
        return len(self.__storage) == self.__capacity
