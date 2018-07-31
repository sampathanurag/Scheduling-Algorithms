#program to add a process by specifying the process ID and task time
#function to display the id and the time remaining can be called by display()

class Process():
    def __init__(self,Id, arrivalTime,taskTime,log = False):
        self.Id = Id
        self.taskTime = taskTime
        self.arrivalTime = arrivalTime
        self.log = log

    def display(self):
        print("Process ID:",self.Id,"| Arrival Time:",self.arrivalTime,"| Task Time Remaining:",self.taskTime,"| Log:",self.log)