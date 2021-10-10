from cache.storage import Storage
from cache.policies import EvictionPolicy
from cache.exceptions import StorageFullException
from cache.exceptions import NotFoundException


class Cache:
    def __init__(self, evictionPolicy: EvictionPolicy, storage: Storage):
        self.__evictionPolicy = evictionPolicy
        self.__storage = storage

    def put(self, key, value):
        try:
            self.__storage.add(key, value)
            self.__evictionPolicy.keyAccessed(key)
        except StorageFullException:
            print('Got storage full. Will try to evict.')
            keyToRemove = self.__evictionPolicy.evictKey()
            if keyToRemove == None:
                raise RuntimeError(
                    'Unexpected State. Storage full and no key to evict.')
            self.__storage.remove(keyToRemove)
            print('Creating space by evicting item...' + keyToRemove)
            self.put(key, value)

    def get(self, key):
        try:
            value = self.__storage.get(key)
            self.__evictionPolicy.keyAccessed(key)
            return value
        except NotFoundException:
            print('Tried to access non-existing key.')
            return None
