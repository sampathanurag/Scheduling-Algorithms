"""
Shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process
with the smallest execution time to execute next. SJN is a non-preemptive algorithm.

Shortest Job first has the advantage of having a minimum average waiting time among all scheduling algorithms.
It is a Greedy Algorithm.
It may cause starvation if shorter processes keep coming. This problem can be solved using the concept of aging.
It is practically infeasible as Operating System may not know burst time and therefore may not sort them.
While it is not possible to predict execution time, several methods can be used to estimate the execution
time for a job, such as a weighted average of previous execution times. SJF can be used in specialized
environments where accurate estimates of running time are available.

Algorithm:
Sort all the process according to the arrival time.
Then select that process which has minimum arrival time and minimum Burst time.
After completion of process make a pool of process which after till the completion of previous process
and select that process among the pool which is having minimum Burst time.

"""

# Imports for the scheduling algorithm
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
    print("-" * 100)
    print('Current Statuses of Queue')
    print("Queue", end="\t")
    SJF.display()
    print("-" * 100)


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
    SJF scheduling algorithm
    :param p: Process List
    :return: None
    """
    global currentTime
    global processList
    global detailedsummary
    for a0 in sorted(p, key=lambda x: x.taskTime):
        if a0.arrivalTime <= currentTime and not a0.log:  # process arrival time is the current time
            SJF.enqueue(a0)
            a0.log = True
            break

    if not SJF.is_empty():
        disp(p)
        print("The queue is executed by the CPU")
        currentProcess = SJF.peek()
        print("Current Process being executed", "P:", end=" ")
        currentProcess.display()
        currentTime += currentProcess.taskTime
        currentProcess.taskTime = 0
        print("Process completed", "P:", currentProcess.Id)
        SJF.dequeue()
        t = [str(currentProcess.Id), str(currentTime), str(currentProcess.taskTime), "SJF"]
        processList.append(t)
        detailedsummary.append(t)

    elif SJF.is_empty():

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
                print("\t\t\t\t", end="")
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
            disp(p)
            currentTime += 1


SJF = Queue()
p = add()
currentTime = 0  # type: int
end_time = 1000
while end_time >= currentTime:
    Scheduling(p)
print(processList)
