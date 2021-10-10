from algorithms import DoublyLinkedList
from algorithms import DoublyLinkedListNode
import EvictionPolicy


class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.__dll = DoublyLinkedList()
        self.__mapper = {}

    def keyAccessed(self, key):
        if key in self.__mapper:
            self.__dll.detachNode(self.__mapper[key])
            self.__dll.addNodeAtLast(self.__mapper[key])
        else:
            newNode = self.__dll.addElementAtLast(key)
            self.__mapper[key] = newNode

    def evictKey(self):
        first = self.__dll.getFirstNode()
        if first == None:
            return None
        self.__dll.detachNode(first)
        return first.getElement()
