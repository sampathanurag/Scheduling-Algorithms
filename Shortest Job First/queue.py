from add_process import Process


# class Queue
# This class is utilized to create queues. In an Operating system, multiple queues may be used


class Queue:
    # class used to create objects which have different attributes and features
    def __init__(self):
        self.queue = []

    def is_empty(self):
        # function to check if a queue is empty
        # return true if empty, false if it contains certain processes
        return self.queue == []

    def enqueue(self, item):
        # function used to add processes to the end of a queue
        self.queue.append(item)

    def dequeue(self):
        # function used to remove processes from the front of a queue, if empty, returns an error
        self.queue.pop(0)

    def size(self):
        # function used to find the number of processes currently existing in the queue
        return len(self.queue)

    def display(self):
        # function used to display the status of the queue, various process it contains, and number of processes
        print("Process Id:", end=" ")

        for i in range(self.size()):
            pr = self.queue[i]
            print(pr.Id, end=" ")

        if self.size == 0:
            print(" ", end="  ")
        print("  " * (10 - self.size()), "| Process Count:", self.size())

    def peek(self):
        return self.queue[0]

    def find(self, process):
        for i in range(len(self.queue)):
            pr = self.queue[i]
            if pr.Id == process.Id:
                return True
        return False
