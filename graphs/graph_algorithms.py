from dataclasses import asdict
from graph import Graph
import numpy as np

#Functions for perfomring graph algorithms are named as: Kruskal, Dijkstra, FordFulkerson

class Edge:
    def __init__(self, weight, _from, _to):
        if type(weight) != int:
            raise NotImplementedError("Edge_weight is empty")
        self.__weight__ = weight 
        self.__from__ = _from
        self.__to__ = _to
        self.__name__ = _from + _to

class Node:
    def __init__(self, type, name):
        #node_type values: 0 - beg, 1- middle, 2 - end
        if type not in [1, 2, 0]:
            raise NotImplementedError("Node_innit failure, type not in scope")
        if name is None:
            raise NotImplementedError("Node_innit failure, name is empty")
        self.__type__ = type  
        self.__name__ = name    

class WeightedGraph(Graph):
    def __init__(self, file_name):
        self.__nodes__ = list()
        self.__edges__ = list()
        self.__connections__ = None
    
    def nodes(self):
        return [Node(x.__type__, x.__name__) for x in self.__nodes__]

    def connections(self):
        return np.copy(self.__connections__)

    def edges(self):
        return [Edge(x.__weight__, x.__from__, x.__to__) for x in self.__edges__]
    
    def weight(self):
        return self.__weight__

    def copy(self):
        a = self.connections
        a[:] = 0
        return [a, self.__nodes__, self.__edges__]
    
    def create_edge(self, weight, _from, _to):
        self.__edges__.append(Edge(weight, _from, _to))
    
    def delete_edge(self, _from, _to):
        ind = [i.__name__ for i in self.__edges__].index(_from + _to)
        self.__edges__.pop(ind)

    def create_connection(self, weight, _from, _to, directed = False):
        #from, to are names of nodes
        ind_from = [i.__name__ for i in self.__nodes__].index(_from)
        ind_to = [i.__name__ for i in self.__nodes__].index(_to)

        self.__connections__[ind_from][ind_to] = 1
        self.create_edge(weight, _from, _to)
        if directed == False:
            self.__connections__[ind_to][ind_from] = 1

    def delete_connection(self, _from, _to, directed = False):
        ind_from = [i.__name__ for i in self.__nodes__].index(_from)
        ind_to = [i.__name__ for i in self.__nodes__].index(_to)

        self.__connections__[ind_from][ind_to] = 0
        self.delete_edge(_from, _to)
        if directed == False:
            self.__connections__[ind_to][ind_from] = 0

    def create_node(self, name, type = 1):
        if name in [i.__name__ for i in self.__nodes__]:
            raise NotImplementedError("Node.create failure, name not unique")
        if (type == 0 and type in [i.__type__ for i in self.__nodes__]) or (type == 2 and type in [i.__type__ for i in self.__nodes__]):
            raise NotImplementedError("Node_create failure, type already listed")

        self.__nodes__.append(Node(type,name))
        new_connections = np.zeros((1,1)) if self.__connections__ is None else np.zeros((self.__connections__.shape[0]+1, self.__connections__.shape[1]+1))
        new_connections[:-1, :-1] = self.__connections__
        self.__connections__ = new_connections
        
    def delete_node(self, name):
        ind = [i.__name__ for i in self.__nodes__].index(name)
        if self.__nodes__(ind).__type__ == 0:
            raise NotImplementedError("Node.delete failure, trying to delete starting node")
        self.__nodes__.pop(ind)
        self.__connections__ = np.delete(self.__connections__, ind, 0)
        self.__connections__ = np.delete(self.__connections__, ind, 1)

def weight(self):
    return self.__weight__

def Kruskal(G):
    A = G
    edges = A.__edges__
    edges.sort(key = weight)
    #Created priority queue
    tree = list()
    tree.append({edges[0].__from__, edges[0].__to__})
    new_edges = list()
    new_edges.append(Edge(edges[0].__weight__, edges[0].__from__, edges[0].__to__ ))

    for i in edges: 
        node1 = i.__from__
        node2 = i.__to__
        _set = list()
        for j in tree:
            if node1 in j and node2 not in j or node2 in j and node1 not in j:
                node = node1 if node2 in j and node1 not in j else node2
                _set = [node in x for x in tree]
                if True in _set:
                    ind = _set.index(True)
                    j.update(j.union(tree.pop(ind)))
                else:
                    j.add(node)
                new_edges.append(Edge(i.__weight__, node1, node2))
                break
            elif True not in [node1 in x or node2 in x for x in tree]:
                tree.append({node1, node2})
                new_edges.append(Edge(i.__weight__, node1, node2))
                break
    tree = list(tree[0])
    tree.sort()
    kruskalGraph = WeightedGraph("A")
    for i in tree:
        kruskalGraph.create_node(i)
    for j in new_edges:
        kruskalGraph.create_connection(j.__weight__, j.__from__, j.__to__)
    return kruskalGraph

def Dijkstra(G, base_node):
    edges = G.__edges__
    nodes = [i.__name__ for i in G.__nodes__]
    queue = {x: None for x in nodes}
    queue[base_node] = 0
    checked = []
    #Keys are the destination nodes values are node from
    path = {}
    distance = {}
    #distance from Node1 to Node2
    for edge in edges:
        if distance.get(edge.__from__) == None:
            distance[edge.__from__] = {edge.__to__: edge.__weight__}
        else:
            distance[edge.__from__][edge.__to__] = edge.__weight__

    while set(checked) != set(nodes):
        current = findMin(queue, checked)
        if distance.get(current) == None:
            checked.append(current) 
            continue
        for i in distance[current]:
            if queue[i] == None:
                queue[i] = distance[current][i] + queue[current]
                path[i] = current
            elif distance[current][i] + queue[current] < queue[i]:
                queue[i] = distance[current][i] + queue[current]
                path[i] = current
        checked.append(current) 

    print(queue)
    print(path)

def findMin(queue, checked):
    min = None
    key = None
    for i in set(queue) - set(checked):
        if min == None:
            min = queue[i]
            key = i
        elif queue[i] != None:
            if queue[i] < min:
                min = queue[i] 
                key = i
    return key

def FordFulkerson(G, start_node, end_node, directed = False):
    edges = G.__edges__
    flow = {x.__name__: 0 for x in edges}
    max_flow = {x.__name__: x.__weight__ for x in edges}
    full = []
    connections = {}
    for x in edges:
        if connections.get(x.__from__) == None:
            connections[x.__from__] = [x.__to__]
        else:
            connections[x.__from__].append(x.__to__)
        if directed == False:
            if connections.get(x.__to__) == None:
                connections[x.__to__] = [x.__from__]
            elif connections:
                connections[x.__to__].append(x.__from__)

    path = augmenting_paths(G, start_node, end_node, full)
    #while paths:
    while path != None:
        minimum = None
        edges_names = [str(path[i]) + str(path[i+1]) for i in range(0, len(path)-1)]
        for i in edges_names:
            i_flow = max_flow[i] - flow[i]
            if minimum == None:
                minimum = i_flow
            elif minimum > i_flow and i_flow > 0: minimum = i_flow
        if minimum <= 0:
            for i in edges_names:
                full.append(i)
            path = augmenting_paths(G, start_node, end_node, full)
            continue
        for i in edges_names:
            flow[i] = flow[i] + minimum
    print(flow)

        
def augmenting_paths(G, start_node, end_node, full, directed = False):
    #Using BFS algorithm to find all paths between start and end node
    edges = G.__edges__
    connections = {}
    for x in edges:
        if x.__name__ in full:
                continue
        
        if connections.get(x.__from__) == None:
            connections[x.__from__] = [x.__to__]
        else:
            connections[x.__from__].append(x.__to__)

        if directed == False:
            if connections.get(x.__to__) == None:
                connections[x.__to__] = [x.__from__]
            else:
                connections[x.__to__].append(x.__from__)
    
    nodes = [x.__name__ for x in G.__nodes__]        
    visited = []
    paths = []
    if start_node not in nodes or end_node not in nodes:
        raise NotImplementedError("BFS Error: No node of given name")
    #nodes = nodes.pop(end_node)
    #nodes.insert(0, nodes.pop(nodes.index(start_node)))
    queue = [start_node]
    paths = [[start_node]]
    while queue:
        current_node = queue[0]
        #Handling exepction
        if connections.get(current_node) == None:
            visited.append(queue.pop(0))
            continue
        for i in connections[current_node]:
            if i not in visited or queue:
                visited.append(i)
                queue.append(i)
                #Saving possible paths
                if findParent(paths, current_node) != None:
                    parent_path = paths.pop(findParent(paths, current_node))
                    if len(connections[current_node]) > 1:
                        for j in connections[current_node]:
                            #X D!
                            temp = parent_path.copy()
                            temp.append(j)
                            if j == end_node:
                                return temp
                            paths.append(temp) 
                    else:
                        temp = parent_path.copy()
                        temp.append(i) 
                        if i == end_node:
                                return temp
                        paths.append(temp)
        queue.pop(0)

    return None

def findParent(paths, parent):
    p_index = None
    for i in paths:
        if i[-1] == parent:
            p_index = paths.index(i)
            return p_index
    return None


if __name__ == "__main__":
    G = WeightedGraph(None)
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    for i in nodes:
        G.create_node(i)
        
    G.create_connection(7, "A","B")
    G.create_connection(5, "A","D")
    G.create_connection(8, "B","C")
    G.create_connection(7, "B","E")
    G.create_connection(9, "D","B")
    G.create_connection(15, "D","E")
    G.create_connection(6, "D","F")
    G.create_connection(8, "E","F")
    G.create_connection(5, "E","C")
    G.create_connection(9, "E","G")
    G.create_connection(11, "F","G")
    #print(G.__connections__)

    if False:
        B = Kruskal(G)
        print("Kruskal:")
        print(B.__connections__)
        print("Edges:")
        print([x.__name__ for x in B.__edges__])

    if False:
        Dijkstra(G, "A")

    if False: 
        FordFulkerson(G, 'A', 'F')

