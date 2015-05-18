This lib is going to be me building something based off of ideas from my
experiences with Go, GAE, Kafka and other task queue problems. An inspirational
design is the Factual Clojure durable-queue repo.

I have a lot of ideas for what I want this to do.

Perform like a normal Deque
Allow in order grouping. Retrieval based on a tag with the results being in the
same order as they would have been in the queue.

Traits
    -Task Name
    -Tag
    -Data/Payload
    -Retry
    -Complete

Queue
    - MaxSize
    - MaxTaskSize
    - Max queue size

Config
    - when/how to fsync - buffer based? every write? etc.

funcs

put(task, tasks)
take( n, timeout)

statistics of the queue
    num tasks
    retried
    completed

Need to research how to / if possible store functions to disk.

Page the data into a files vs file per task - slabs. Look at multiple readers etc.

Determine optimal block size to write etc. 
