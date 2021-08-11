### MapReduce system
MapReduce processes distributed data. Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner. 

> Typically the compute nodes and the storage nodes are the same, that is, the MapReduce framework and the Hadoop Distributed File System (see HDFS Architecture Guide) are running on the same set of nodes. This configuration allows the framework to effectively schedule tasks on the nodes where data is already present, resulting in very high aggregate bandwidth across the cluster.

The MapReduce framework consists of a single cluster-master **JobTracker** and one slave **TaskTracker** per cluster-node. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master. Minimally, applications specify the input/output locations and supply map and reduce functions via implementations of appropriate interfaces and/or abstract-classes. These, and other job parameters, comprise the job configuration. The Hadoop job client then submits the job (jar/executable etc.) and configuration to the JobTracker which then assumes the responsibility of distributing the software/configuration to the slaves, scheduling tasks and monitoring them, providing status and diagnostic information to the job-client.

The MapReduce framework operates exclusively on **<key, value>** pairs, that is, **the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job**, conceivably of different types. The key and value classes have to be serializable by the framework and hence need to implement the [Writable](https://hadoop.apache.org/docs/r1.2.1/api/org/apache/hadoop/io/Writable.html) interface. Additionally, the key classes have to implement the [WritableComparable](https://hadoop.apache.org/docs/r1.2.1/api/org/apache/hadoop/io/WritableComparable.html) interface to facilitate sorting by the framework.

- Input and Output types of a MapReduce job:
> (input) <k1, v1> -> **map** -> <k2, v2> -> **combine** -> <k2, v2> -> **reduce** -> <k3, v3> (output)

- MapReduce demonstration
![[mapreduce.png|600]]

##### Mapper
Mapper splits and processes the input data-set into independent chunks in a completely parallel manner, which, (intermediary data) are then shuffled, sorted and fed to Reducer in partition. The total number of partitions is the same as the number of reduce tasks for the job.

Users can optionally specify a **combiner**, via `JobConf.setCombinerClass(Class)`, to perform local aggregation of the intermediate outputs, which helps to cut down the amount of data transferred from the Mapper to the Reducer.

- *How Many Maps?*
The number of maps is usually driven by the total size of the inputs, that is, the total number of blocks of the input files. The right level of parallelism for maps seems to be around 10-100 maps per-node, although it has been set up to 300 maps for very cpu-light map tasks. Task setup takes a while, so it is best if the maps take at least a minute to execute.

##### Reducer
**Reducer reduces a set of intermediate values which share a key to a smaller set of values.**

### Hive
API to Hadoop's "database" across its distributed file systems. Data definition language is SQL-like.

### Pig
Data ETL

### DFS