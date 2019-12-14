from add_process import Process


# class Queue
# This class is utilized to create queues. These queues are used for the simulation of the processes
# in a computer OS


class Queue:
    # class used to create objects which have different attributes and features
    def __init__(self):
        """
        :param queue: List queue to simulate the data structure queue
        """
        self.queue = []

    def is_empty(self):
        """
        Function to check if queue is empty
        :return: Boolean
        """
        return self.queue == []

    def enqueue(self, item):
        """
        Adding a process object into a queue
        :param item: Process object
        :return: None
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Function to remove a completed or ejected process object from the queue
        :return: Process object
        """
        self.queue.pop(0)

    def size(self):
        """
        Function to find the number of processes currently existing in a queue
        :return: int
        """
        return len(self.queue)

    def display(self):
        """
        Function to neatly display the queue state at any point in time
        :return: None
        """
        print("Process Id:", end=" ")

        for i in range(self.size()):
            pr = self.queue[i]
            print(pr.Id, end=" ")

        if self.size == 0:
            print(" ", end="  ")
        print("  " * (10 - self.size()), "| Process Count:", self.size())

    def peek(self):
        """
        Function to find the process at the front of the queue
        :return: Process object
        """
        return self.queue[0]

    def find(self, process):
        """
        Function to find a particular process by process id
        :param process: Process Object
        :return: boolean
        """
        for i in range(len(self.queue)):
            pr = self.queue[i]
            if pr.Id == process.Id:
                return True
        return False
