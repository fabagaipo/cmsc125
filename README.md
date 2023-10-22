Machine Problem 1:

# On Multiprogramming with time-sharing systems

1. Generate a random number of resources (1-30). Label them by resource number, between 1-30. 
2. Generate a random number of users (1-30). Label them by user number between, 1-30.
3. Generate the random resource that a user will need and the length of the time that the user will 
use the resource (1-30 seconds). The resource(s) that a user will request must only be those 
randomly generated resources (from #1).
4. The program should be able to display the status of the resources, including the user currently 
using the resource, the time (or time left) that the user needs to use the resource.
5. The program should also be able to list the users “in waiting” of a resource, if there are any, 
and when these users will be able to start using the resource.
6. Finally, the program should be able to say when the resources will be free of users (meaning, 
no user needs to use the resource).


Machine Problem 2:

# On Processor Management and Job Scheduling

Implement the FCFS, SJF, SRPT, Priority and Round-robin scheduling. Sample data is given to you

• For FCFS and SJF, assume all processes arrived at time 0 in that order.

• For SRPT, consider the arrival time of each processes.

• For Priority, assume that lower-value priorities have higher priorities (that means 0 is the
highest priority).

• For round-robin scheduling, assume a uniform time slice of 4 millisecond.

Display the waiting time for each process for every algorithm, as well as their average computing time.

Also, perform an algorithm evaluation, based on the datasets given to you


Machine Problem 3:

# On Memory Management and Allocation Strategies

a) Write an event-driven simulation to help you decide which storage placement strategy should be used at this installation. Your program would use the job stream and memory partitioning as indicated. Run the program until all jobs have been executed with the memory as is (in order by address). This will give you the first-fit type performance results.

b) Do the same as (a), but this time implement the worst-fit placement scheme.

c) Sort the memory partitions by size and run the program a second time; this will give you the best-fit performance results. For all parts (a), (b) and (c) you are investigating the performance of the system using a typical job stream by measuring:


1. Throughput (how many jobs are processed per given time unit)
2. Storage utilization (percentage of partitions never used, percentage of partitions heavily used, etc.)
3. Waiting queue length
4. Waiting time in queue
5. Internal fragmentation

d) Look at the results from the first-fit, worst-fit and best-fit. Explain what the results indicate
about the performance of the system for this job mix and memory organization. Is one method of partitioning better than the other? Why or why not? Could you recommend one method over the
other based on your sample run? Would this hold in all cases? Write some conclusions and
recommendations. 

ANSWER:

From the results we can see that the first fit actually performs a better average of jobs or processes completed over time and storage utilization compared to the other two methods. For this particular program, the first fit is the best allocation method to use however this may not stay true for other jobs and blocks.

In fixed partitioning, the main memory is not utilized effectively. The memory assigned to each process is of the same size that can cause some processes to have more memory than they need. In dynamic partitioning, the main memory is utilized very effectively. The memory assigned to each process is exactly what is needed for the execution of the process. One advantages of fixed partitions is that you can prevent data loss during power outages or when software fails. However, a disadvantage is the loss of disk space from the total disk space available when running different operating systems on the same hard disk. Whereas, dynamic partitioning tries to overcome the problems caused by fixed partitioning but when processes finish and new processes are brought in, the main memory becomes more and more fragmented, and memory use declines.
