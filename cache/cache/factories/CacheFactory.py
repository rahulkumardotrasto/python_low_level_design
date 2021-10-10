from cache import Cache
from policies import LRUEvictionPolicy
from storage import HashMapBasedStorage


class CacheFactory:
    def defaultCache(self, capacity: int):
        return Cache(LRUEvictionPolicy(), HashMapBasedStorage(capacity))
