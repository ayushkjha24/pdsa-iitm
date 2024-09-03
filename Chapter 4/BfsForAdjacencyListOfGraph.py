# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue == [])    
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)    
    def __str__(self):
        return(str(self.queue))

# BFS Implementation For Adjacency list
def BFSList(AList,start_vertex):
    # Initialization
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False    
    
    # Create Queue object q
    q = Queue()
    
    # Mark the start_vertex visited and insert it into the queue 
    visited[start_vertex] = True
    q.enqueue(start_vertex)
    
    # Repeat the following until the queue is empty 
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit each adjacent of the removed vertex (if not visited), mark that visited, and insert it into the queue 
        for adj_vertex in AList[curr_vertex]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)               
    return(visited)

AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSList(AList,0))