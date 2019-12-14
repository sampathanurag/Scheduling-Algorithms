# Script to add a process by specifying the process ID and task time
# The function to display the id and the time remaining can be accomplished by invoking the function display()


class Process:
    """"
    Class to create process objects with various attributes
    """
    def __init__(self, Id, arrivalTime, taskTime, log=False):
        """
        Initialization function
        :param Id: Process Id
        :param arrivalTime: Arrival time of the process into the system
        :param taskTime: The time taken for completion of the process
        :param log: Parameter set when the process is recognized and added to the process queue
        """
        self.Id = Id
        self.taskTime = taskTime
        self.arrivalTime = arrivalTime
        self.log = log

    def display(self):
        """
        Function to display the process in a neat understandable format
        :return: None
        """
        print("Process ID:", self.Id, "| Arrival Time:", self.arrivalTime, "| Task Time Remaining:",
              self.taskTime, "| Log:", self.log)
