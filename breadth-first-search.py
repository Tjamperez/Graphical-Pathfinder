from queue import Queue

##Attempt to write a Breadth-First-Search algorithm

# #Assign ‘a’ as the root node and insert it into the Queue.
# Extract node ‘a’ from the queue and insert the child nodes of ‘a’, i.e., ‘b’ and ‘c’.
# Print node ‘a’.
# The queue is not empty and has node ‘b’ and ‘c’. Since ‘b’ is the first node in the queue, let’s extract it and insert the child nodes of ‘b’, i.e., node ‘d’ and ‘e’.
# Repeat these steps until the queue gets empty. Note that the nodes that are already visited should not be added to the queue again.


# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.



#lista teste
test = ["a","b","c","d","e","f"]


class explore:
    def __init__(self,size,list):
        self.size = size
        self.list = list

    def queue(self):
        listin = self.list
        bfs = Queue(maxsize = self.size)
        while listin is not None:
            firstque =  listin.pop(0) 
            bfs.put(firstque)
     
class frontier:
        pass
class dequeue:
        pass