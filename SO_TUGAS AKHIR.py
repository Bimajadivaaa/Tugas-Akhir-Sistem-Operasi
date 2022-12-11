class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __str__(self):
        return f"Process ID: {self.process_id}, Arrival Time: {self.arrival_time}, Burst Time: {self.burst_time}, Priority: {self.priority}"

class PrioritySchedullingNonPreemptive:
    def processData(self, nomer_process):
        process_data = []
        for i in range (nomer_process):
            temp = []
            process_id = int(input("Masukkan ID Proccess : "))
            
            waktu_burst = int(input(f"Masukkan Burst Time untuk Proccess {process_id} : "))
            waktu_prioritas = int(input(f"Masukkan Prioritas untuk Proses {process_id} : "))
            temp.extend([process_id, 0 , waktu_burst, waktu_prioritas])
            
            process_data.append(temp)
        return process_data

    def printGanttChart(self, process_queue):
        print("Gantt Chart:")
        print("0", end="")
        for i in range(len(process_queue)):
            print("----P" + str(process_queue[i].process_id), end="")
        print("----", end="")
        print()

   
    def findWaitingTime(self, process_queue, waiting_time):
        service_time = [0] * len(process_queue)
        service_time[0] = 0
        waiting_time[0] = 0

        for i in range(1, len(process_queue)):
            service_time[i] = (service_time[i - 1] + process_queue[i - 1].burst_time)
            waiting_time[i] = service_time[i] - process_queue[i].arrival_time + 1

            if waiting_time[i] < 0:
                waiting_time[i] = 0

    def findTurnAroundTime(self, process_queue, waiting_time, turnaround_time):
        for i in range(len(process_queue)):
            turnaround_time[i] = process_queue[i].burst_time + waiting_time[i]

    def findavgTime(self, process_queue):
        waiting_time = [0] * len(process_queue)
        turnaround_time = [0] * len(process_queue)

        self.findWaitingTime(process_queue, waiting_time)
        self.findTurnAroundTime(process_queue, waiting_time, turnaround_time)

        print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
        total_waiting_time = 0
        total_turnaround_time = 0
        for i in range(len(process_queue)):
            total_waiting_time = total_waiting_time + waiting_time[i]
            total_turnaround_time = total_turnaround_time + turnaround_time[i]
            print(str(process_queue[i].process_id) + "\t\t" + str(process_queue[i].burst_time) + "\t\t" + 
                  str(waiting_time[i]) + "\t\t" + str(turnaround_time[i]))

        print("Average waiting time = " + str(total_waiting_time / len(process_queue)))
        print("Average turnaround time = " + str(total_turnaround_time / len(process_queue)))

    def schedule(self, process_queue):
        self.printGanttChart(process_queue)
        self.findavgTime(process_queue)
        self.printTable(process_queue)

    def printTable(self, process_queue):
        print("Process ID\tBurst Time\tPriority")
        for i in range(len(process_queue)):
            print(str(process_queue[i].process_id) + "\t\t" + str(process_queue[i].burst_time) + "\t\t" + str(process_queue[i].priority))

            
    def run(self):
        process_queue = []
        process_data = self.processData(int(input("Masukkan Jumlah Proses : ")))
        for i in range(len(process_data)):
            process_queue.append(Process(process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3]))
        process_queue.sort()
        self.schedule(process_queue)

if __name__ == "__main__":
    priority_schedulling_non_preemptive = PrioritySchedullingNonPreemptive()
    priority_schedulling_non_preemptive.run()


