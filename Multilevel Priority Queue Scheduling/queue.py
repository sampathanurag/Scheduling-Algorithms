from add_process import Process

"""
class Queue
This class is utilized to create queues. In an Operating system, multiple queues may be used
 with different priorities. For the sole purpose of simplicity we have taken 3 queues
 Queue 1, Quantum 5, Priority High
 Queue 2, Quantum 7, Priority Moderate
 FCFS   , Quantum -, Priority Low
"""


class Queue:
    """
    class used to create objects which have different attributes and features
    """

    def __init__(self, quantum=None):
        """
        Function to inialize the Queue Object
        :param quantum: Quantum to choose the priority of the queue
        """
        self.quantum = quantum
        self.items = []

    def is_empty(self):
        """
        function to check if a queue is empty
        :return: true if empty, false if it contains certain processes
        """
        return self.items == []

    def enqueue(self, item):
        """
        function used to add processes to the end of a queue
        :param item: Process object to be added to the queue
        :return: None
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Function to remove process object from the queue
        :return: None
        """
        self.items = self.items[:-1]

    def size(self):
        """
        function used to find the number of processes currently existing in the queue
        :return: int
        """
        return len(self.items)

    def display(self):
        """
        function used to display the status of the queue, various process it contains, and number of processes
        :return: None
        """
        print("Process Id:", end=" ")

        for i in range(len(self.items)):
            pr = self.items[i]
            print(pr.Id, end=" ")
        if self.size == 0:
            print(" ", end="  ")
        print("  " * (10 - self.size()), "| Process Count:", self.size())

    def peek(self):
        """
        Returns the process object at the front of the queue
        :return: Process Object
        """
        return self.items[-1]

    def find(self, process):
        """
        Function to find the process with a particular id
        :param process: Process object
        :return: Boolean
        """
        for i in range(len(self.items)):
            pr = self.items[i]
            if pr.Id == process.Id:
                return True
        return False
