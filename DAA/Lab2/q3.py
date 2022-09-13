from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self,s):
        visited = [False] * (len(self.graph))
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s=queue.pop(0)
            print(s,end=" ")

            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        print()

    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v]= True
        print(v,end=" ")

        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    
    def DFS(self):
        visited = [False] * (len(self.graph))
        
        for i in  range(len(self.graph)):
            if visited[i]==False:
                self.DFSUtil(i, visited)            
            
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(3, 0)

print ("BFS")
g.BFS(3)
print("DFS")
g.DFS()