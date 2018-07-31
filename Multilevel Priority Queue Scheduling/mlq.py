# Multi-level Priority Queue Scheduling for tasks
import sys
from queue import Queue
from add_process import Process
global currentTime
global processList
processList = []

def unique(p,pId):
	for i in range(len(p)):
		if p[i].Id == pId:
			return False
	return True

def countProcess(p):
	count = 0
	for i in range(len(p)):
		if p[i].log == False:
			count += 1
	return count

def disp(p):
	global currentTime
	print("-"*100)
	print("Current Time:",currentTime)
	print("Processes:")
	for a0 in range(len(p)):
		p[a0].display()
	print("")
	print("Current Statuses of Queues")
	print("Queue1",end = "\t")
	Queue1.display()
	#print("Number of elements:",Queue1.size())
	print("Queue2",end = "\t")
	Queue2.display()
	#print("Number of elements:",Queue1.size())
	print("FCFS",end = "\t")
	FCFS.display()
	#print("Number of elements:",Queue1.size())
	print("-"*100)


#function to add processes
def add():
	p = []		#list of processes
	print("Enter the number of processes")
	ans = int(input().strip())
	for i in range(ans):
		print("Enter process ID, arrival Time, Task Time, Queue Number 1/2/3(Optional)")
		inp  = [int(inp_temp) for inp_temp in input().strip().split(' ')]
		pId = inp[0]
		aT = inp[1]
		tT = inp[2]
		try:
			qnum = inp[3]
		except:
			qnum = 1
		if int(qnum) >=1 and int(qnum) <= 3:
				qno = int(qnum)
		else:
			qno = 1
		if unique(p,pId):
			process = Process(pId,aT,tT,qno)
		p.append(process)

	print("-"*100)
	print("Processes added:")
	for a0 in range(len(p)):
		p[a0].display()
	print("-"*100)
	return p



def Scheduling(p):
	global currentTime
	global processList
	for a0 in sorted(p,key=lambda x: x.arrivalTime):
		#print(a0.Id,a0.arrivalTime)
		if a0.arrivalTime <= currentTime:	#process arrival time is the current time
			if not a0.log:
				#print(a0.Id)
				if a0.qno == 1:
					Queue1.enqueue(a0)
				elif a0.qno == 2:
					Queue2.enqueue(a0)
				else:
					FCFS.enqueue(a0)

				a0.log = True
	disp(p)

	
	if not Queue1.isEmpty():
		print("Queue1 is executed by the CPU")
		print("Time quantum of Queue1:",Queue1.quantum)
		currentProcess = Queue1.peek()
		print("Current Process being executed","P:",end = " ")
		currentProcess.display()
		if currentProcess.taskTime > Queue1.quantum:
			currentProcess.taskTime -= Queue1.quantum
			Queue1.dequeue() #premempt
			Queue2.enqueue(currentProcess)
			currentTime += Queue1.quantum
			t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"Queue1"]
			processList.append(t)


		else:
			currentProcess = Queue1.peek()
			currentTime += currentProcess.taskTime
			currentProcess.taskTime = 0
			print("Process completed","P:",currentProcess.Id)
			Queue1.dequeue()
			t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"Queue1"]
			processList.append(t)

	#if Queue1 is empty, the CPU prcesses Queue2 which has a lower priority than Queue1

	elif not Queue2.isEmpty():
		print("Queue2 is executed by the CPU")
		print("Time quantum of Queue2:",Queue2.quantum)
		currentProcess = Queue2.peek()
		print("Current Process being executed","P:",end = " ")
		currentProcess.display()

		time1 = currentProcess.taskTime
		time2 = Queue2.quantum
		min_time = min(time1,time2)
		for a0 in sorted(p,key=lambda x: x.arrivalTime):
		#print(a0.Id,a0.arrivalTime)
			if a0.arrivalTime >= currentTime and a0.arrivalTime <= currentTime+min_time:	#process arrival time is the current time
				if not a0.log:
					if a0.qno == 1:
						Queue1.enqueue(a0)
					elif a0.qno == 2:
						Queue2.enqueue(a0)
					else:
						FCFS.enqueue(a0)
				a0.log = True

				currentProcess.taskTime -= (a0.arrivalTime - currentTime)
				currentTime = a0.arrivalTime
				t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"Queue2"]
				processList.append(t)
				return



		if currentProcess.taskTime > Queue2.quantum:
			currentProcess.taskTime -= Queue2.quantum
			Queue2.dequeue()
			FCFS.enqueue(currentProcess)
			currentTime += Queue2.quantum
			currentProcess.display()
			disp(p)
			t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"Queue2"]
			processList.append(t)
		else:
			currentProcess = Queue2.peek()
			currentTime += currentProcess.taskTime
			currentProcess.taskTime = 0
			print("Process completed","P:",currentProcess.Id)
			Queue2.dequeue()
			t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"Queue2"]
			processList.append(t)
		#disp(p)


	#if Queue1 and Queue2 are both empty, then the CPU moves to lower priority queues
	#the last / lowest priority queue is the FCFS

	elif not FCFS.isEmpty():
		print("FCFS queue is executed by the CPU")
		print("Time quantum of FCFS Queue:",FCFS.quantum)
		currentProcess = FCFS.peek()
		print("Current Process being executed","P:",end = " ")
		currentProcess.display()

		for a0 in sorted(p,key=lambda x: x.arrivalTime):
		#print(a0.Id,a0.arrivalTime)
			if a0.arrivalTime >= currentTime and a0.arrivalTime <= currentTime+currentProcess.taskTime:	#process arrival time is the current time
				if not a0.log:
					if a0.qno == 1:
						Queue1.enqueue(a0)
					elif a0.qno == 2:
						Queue2.enqueue(a0)
					else:
						FCFS.enqueue(a0)
				a0.log = True

				currentProcess.taskTime -= (a0.arrivalTime - currentTime)
				currentTime = a0.arrivalTime
				t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"Queue2"]
				processList.append(t)
				return

		currentTime += currentProcess.taskTime
		currentProcess.taskTime = 0
		print("Process completed","P:",currentProcess.Id)
		FCFS.dequeue()
		t = [str(currentProcess.Id),str(currentTime),str(currentProcess.taskTime),"FCFS"]
		processList.append(t)

	#disp(p)

	for a0 in sorted(p,key=lambda x: x.arrivalTime):
		#print(a0.Id,a0.arrivalTime)
		if a0.arrivalTime <= currentTime:	#process arrival time is the current time
			if not a0.log:
				#print(a0.Id)
				if a0.qno == 1:
					Queue1.enqueue(a0)
				elif a0.qno == 2:
					Queue2.enqueue(a0)
				else:
					FCFS.enqueue(a0)

				a0.log = True
	

	if Queue1.isEmpty() and Queue2.isEmpty() and FCFS.isEmpty():
		if countProcess(p) == 0:
			print("-"*100)
			disp(p)
			print("All Processes completed successfully")	
			print("Total time taken for all processes: ",currentTime)
			print("-"*100)
			for i in range(len(processList)-1):
				try:
					if processList[i] == processList[i+1]:
						processList.remove(processList[i])
				except:
					pass
			print("\t\t\t----------------------Execution Summary--------------------------")
			print("\t\t\tProcess ID \t\t Current Time   \t\t  Task Time Remaining \t\t   Queue ")
			for row in processList:
				print("{: >30} {: >30} {: >30} {: >30}".format(*row))
				print("\t\t\t\t\t|")
				print("\t\t\t\t\tV\n")
			print("\t\t\t\t\tEND")
			print("-"*100)
			sys.exit(0)
		else:
			currentTime += 1
	




#Define 3 queues
# q1 has the highest priority and a time quantum 5
# q2 has the next priority and a time quantum 7
# q3 is a fcfs first come first serve queue with no time quantum
# In an actual cpu more number of queues can be used,
# but for simpler implementation purposes 3 queues are sufficient


Queue1 = Queue(5)
Queue2 = Queue(7)
FCFS = Queue()
p = add()
currentTime = 0
end_time = 1000
while currentTime <= end_time:
	Scheduling(p)

print(processList)
