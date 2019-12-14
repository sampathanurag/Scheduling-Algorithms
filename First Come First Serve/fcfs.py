# First Come First Serve Scheduling for tasks
"""
Given In processes with their burst times, the task is to find average waiting time and average turn
around time using FCFS scheduling algorithm.
First in, first out (FIFO), also known as first come, first served (FCFS), is the simplest scheduling algorithm.
FIFO simply queues processes in the order that they arrive in the ready queue.
In this, the process that comes first will be executed first and next process starts only after the previous gets
fully executed.
"""

#imports
import sys
from queue import Queue
from add_process import Process

global currentTime
global processList
processList = []
global detailedsummary
detailedsummary = []


def unique(p, pId):
    """
    Function to check for the uniqueness of the process id
    :param p: Queue of processes
    :param pId: Specific process id
    :return: boolean
    """
    for i in range(len(p)):
        if p[i].Id == pId:
            return False
    return True


def countProcess(p):
    """
    Function to count the number of processes
    :param p: Process queue
    :return: int
    """
    count = 0
    for i in range(len(p)):
        if p[i].log == False:
            count += 1
    return count


def disp(p):
    """
    Function to display the current state of the scheduler
    :param p: process list
    :return: None
    """
    global currentTime
    print("-" * 100)
    print("Current Time:", currentTime)
    print("Processes:")
    for a0 in range(len(p)):
        p[a0].display()
    print("")
    print('Current Statuses of Queue')
    print("Queue", end="\t")
    FCFS.display()
    print("-" * 100)


# function to add processes
def add():
    """
    Function to add the processes specifying the various attributes
    :return: Process List
    """
    p = []  # list of processes
    print("Enter the number of processes")
    ans = int(input().strip())
    for i in range(ans):
        print("Enter process ID, arrival Time, Task Time")
        inp = [int(inp_temp) for inp_temp in input().strip().split(' ')]
        pId = inp[0]
        aT = inp[1]
        tT = inp[2]
        if unique(p, pId):
            process = Process(pId, aT, tT)
        p.append(process)

    print("-" * 100)
    print("Processes added:")
    for a0 in range(len(p)):
        p[a0].display()
    print("-" * 100)
    return p


def Scheduling(p):
    """
    FCFS scheduling algorithm
    :param p: Process List
    :return: None
    """
    global currentTime
    global processList
    global detailedsummary
    for a0 in sorted(p, key=lambda x: x.arrivalTime):
        # print(a0.Id,a0.arrivalTime)
        if a0.arrivalTime <= currentTime and not a0.log:  # process arrival time is the current time
            FCFS.enqueue(a0)
            a0.log = True
    disp(p)

    # if Queue1 and Queue2 are both empty, then the CPU moves to lower priority queues
    # the last / lowest priority queue is the FCFS
    if not FCFS.is_empty():
        print("The queue is executed by the CPU")
        currentProcess = FCFS.peek()
        print("Current Process being executed", "P:", end=" ")
        currentProcess.display()
        for a0 in sorted(p, key=lambda x: x.arrivalTime):
            # print(a0.Id,a0.arrivalTime)
            if a0.arrivalTime >= currentTime and a0.arrivalTime <= currentTime + currentProcess.taskTime and not a0.log:  # process arrival time is the current time
                FCFS.enqueue(a0)
                a0.log = True
                currentProcess.taskTime -= (a0.arrivalTime - currentTime)
                currentTime = a0.arrivalTime  # type: object
                t = [str(currentProcess.Id), str(currentTime), str(currentProcess.taskTime), "Queue2"]
                #processList.append(t)
                detailedsummary.append(t)
                return
        currentTime += currentProcess.taskTime
        currentProcess.taskTime = 0
        print("Process completed", "P:", currentProcess.Id)
        FCFS.dequeue()
        t = [str(currentProcess.Id), str(currentTime), str(currentProcess.taskTime), "FCFS"]
        processList.append(t)
        detailedsummary.append(t)
    for a0 in sorted(p, key=lambda x: x.arrivalTime):
        # print(a0.Id,a0.arrivalTime)
        if a0.arrivalTime <= currentTime and not a0.log:  # process arrival time is the current time
            FCFS.enqueue(a0)
            a0.log = True
    if FCFS.is_empty():
        if countProcess(p) == 0:
            print("-" * 100)
            disp(p)
            print("All Processes completed successfully")
            print("Total time taken for all processes: ", currentTime)
            print("-" * 100)
            for i in range(len(processList) - 1):
                try:
                    if processList[i] == processList[i + 1]:
                        processList.remove(processList[i])
                except:
                    pass
            print("\t\t\t\t----------------------Execution Summary--------------------------")
            print("\t\t\t\tProcess ID \t\t\t Current Time   \t\t  Task Time Remaining ")
            for row in processList:
                print("{: >20} {: >20} {: >20}\n".format(*row))
                print("\t\t\t\t",end = "")
                print("-"*65)
            print("\n")
            print("\t\t\t\t                        END")
            print("-" * 100)
            key = input("Enter any alphanumeric key for a detailed summary")
            if key:
                print("-" * 100)
                disp(p)
                print("All Processes completed successfully")
                print("Total time taken for all processes: ", currentTime)
                print("-" * 100)
                for i in range(len(detailedsummary) - 1):
                    try:
                        if detailedsummary[i] == detailedsummary[i + 1]:
                            detailedsummary.remove(detailedsummary[i])
                    except:
                        pass
                print("\t\t\t\t----------------------Execution Summary--------------------------")
                print("\t\t\t\tProcess ID \t\t\t Current Time   \t\t  Task Time Remaining ")
                for row in detailedsummary:
                    print("{: >20} {: >20} {: >20}\n".format(*row))
                    print("\t\t\t\t", end="")
                    print("-" * 65)
                print("\n")
                print("\t\t\t\t                        END")
                print("-" * 100)
            sys.exit(0)
        else:
            currentTime += 1


FCFS = Queue()
p = add()
currentTime = 0  # type: int
end_time = 1000
while end_time >= currentTime:
    Scheduling(p)
print(processList)