## Spark vs. Hadoop
- Hadoop pros:
Hadoop is based on **acyclic data flow** (input->mapper->reducer->output) from stable storage to stable storage.

- Hadoop cons:
It is inefficient for applications that repeatedly **reuse** a working set of data 
![[hadoopcons.png]]

## Spark
### overview
At a high level, every Spark application consists of a driver program that runs the user’s main function and executes various parallel operations on a 'cluster' manager. The main abstraction Spark provides is a resilient distributed dataset (RDD), which is a collection of elements partitioned across the nodes of the cluster that can be operated on in parallel. 

A second abstraction in Spark is shared variables that can be used in parallel operations. By default, when Spark runs a function in parallel as a set of tasks on different nodes, it ships a copy of each variable used in the function to each task. Sometimes, a variable needs to be shared across tasks, or between tasks and the driver program. Spark supports two types of shared variables: broadcast variables, which can be used to cache a value in memory on all nodes, and accumulators, which are variables that are only “added” to, such as counters and sums.

See more details [here at apache spark documentation](https://spark.apache.org/docs/latest/rdd-programming-guide.html#overview)

### spark work flow
If the program is iterative (no inter-dependencies in each iteration), put input data to distributed memories across machines; if the program is interactive, put input data in memory, so interaction in each iteration can be done fast.
![[sparkflow.png]]

### Resilient Distributed Datasets
RDD provides an interface with coarse-grained data transformations (balance between fault-tolerance, transformation tracking, and data manipulation granularity): `map`,`join`,`distinct`,`union`,`intersection`,`substract`...
![[spark_ops.png]]
Efficient fault recovery using **lineage** that tracks/logs RDD transformations.

### RDD operations
RDDs support two types of operations: **transformations**, which create a new dataset from an existing one, and **actions**, which return a value to the driver program after running a computation on the dataset. For example, map is a transformation that passes each dataset element through a function and returns a new RDD representing the results. On the other hand, reduce is an action that aggregates all the elements of the RDD using some function and returns the final result to the driver program (although there is also a parallel reduceByKey that returns a distributed dataset).

**All transformations in Spark are lazy, in that they do not compute their results right away. Instead, they just remember the transformations applied to some base dataset (e.g. a file). The transformations are only computed when an action requires a result to be returned to the driver program**. This design enables Spark to run more efficiently. For example, we can realize that a dataset created through map will be used in a reduce and return only the result of the reduce to the driver, rather than the larger mapped dataset. More on [RDD operations](https://spark.apache.org/docs/latest/rdd-programming-guide.html)

- RDD transformation
create a new RDD from an existing one.
e.g. `filter`,`map`

- RDD actions
driver program (main thread) sends RDD to worker threads managed by a cluster manager. 
e.g. `count`,`collect`,`reduce`...

### more on RDD cluster mode
![[spark_clustermode.png]]
Spark applications run as independent sets of processes on a cluster, coordinated by the SparkContext object in your main program (called the driver program).

Specifically, to run on a cluster, the SparkContext can connect to several types of cluster managers (either Spark’s own standalone cluster manager, **Mesos** or **YARN**), which allocate resources across applications. Once connected, Spark acquires executors on nodes in the cluster, which are processes that run computations and store data for your application. Next, it sends your application code (defined by JAR or Python files passed to SparkContext) to the executors. Finally, SparkContext sends tasks to the executors to run.

There are several useful things to note about this architecture:

1. Each application gets its own executor processes, which stay up for the duration of the whole application and run tasks in multiple threads. This has the benefit of isolating applications from each other, on both the scheduling side (each driver schedules its own tasks) and executor side (tasks from different applications run in different JVMs However, it also means that data cannot be shared across different Spark applications (instances of SparkContext without writing it to an external storage system.
2. Spark is agnostic to the underlying cluster manager. As long as it can acquire executor processes, and these communicate with each other, it is relatively easy to run it even on a cluster manager that also supports other applications (e.g. Mesos/YARN).
3. The driver program must listen for and accept incoming connections from its executors throughout its lifetime (e.g., see spark.driver.port in the network config section). As such, the driver program must be network addressable from the worker nodes.
4. Because the driver schedules tasks on the cluster, it should be run close to the worker nodes, preferably on the same local area network. **If you’d like to send requests to the cluster remotely, it’s better to open a RPC (remote procedure call) to the driver and have it submit operations from nearby than to run a driver far away from the worker nodes.**

See more details for [cluster mode](https://spark.apache.org/docs/latest/cluster-overview.html#components)

## Stack
![[sparkstack.png]]
- Yarn / Mesos: cluster manager (manage workers (threads other than main thread(driver program)))
