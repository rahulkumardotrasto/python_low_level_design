import DoubleLinkedListNode
from exceptions import InvalidElementException


class DoubleLinkedList():

    def __init__(self):
        self.__dummyHead = DoubleLinkedListNode(None,  None)
        self.__dummyTail = DoubleLinkedListNode(None,  None)

        self.__dummyHead.next = self.__dummyTail
        self.__dummyTail.prev = self.__dummyHead

    def detachNode(self, node: DoubleLinkedListNode):
        if node != None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def addNodeAtLast(self, node: DoubleLinkedListNode):
        tailPrev = self.__dummyTail.prev
        tailPrev.next = node
        node.next = self.__dummyTail
        self.__dummyTail.prev = node
        node.prev = tailPrev

    def addElementAtLast(self, key, value):
        if key == None or value == None:
            raise InvalidElementException('Invalid element')
        newNode = DoubleLinkedListNode(key, value)
        self.addNodeAtLast(newNode)
        return newNode

    def isItemPresent():
        return self.__dummyHead.next != self.__dummyTail

    def getFirstNode():
        if not self.isItemPresent():
            return None
        return self.__dummyHead.next

    def getLastNode():
        if not self.isItemPresent():
            return None
        return self.__dummyTail.prev
