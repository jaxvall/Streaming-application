class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def __str__(self):
        end_of_row = ""
        while not self.isEmpty():
            char = self.dequeue()
            end_of_row += char
        return end_of_row

    def enqueue(self, x):
        """
        Adds a value to queue.
        """
        new = Node(x)
        if self.isEmpty():
            self.__first = new
        else:
            self.__last.next = new
        self.__last = new

    def dequeue(self):
        """
        Removes a value from the queue
        :return: The removed value
        """
        if not self.isEmpty():
            x = self.__first.value
            self.__first = self.__first.next
            return x

    def isEmpty(self):
        """
        Checks if the queue is isEmpt
        :return: Boolean variable. True if the queue is empty. False if not.
        """
        return self.__first == None

    def peek(self):
        x = None
        if self.__first != None:
            x = self.__first.value
        return x
