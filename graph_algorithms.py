from dataclasses import asdict
from graph import Graph
import numpy as np

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
    tree = list()
    #check if that necessesary, try tree.append(set())
    tree.append({edges[0].__from__, edges[0].__to__})
    #tree.append(set())
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

if __name__ == "__main__":
    """
    tree = list()
    tree.append({1,2,4})
    tree.append({0,5,7,8})
    tree.append({3,5,6})
    node2 = 3
    _set = [node2 in x for x in tree]
    if True in _set:
        ind = _set.index(True)
        print(ind)
        tree[0] = tree[0].union(tree[ind])
    print(tree[0])
    """
    G = WeightedGraph(None)
    G.create_node("A")
    G.create_node("B")
    G.create_node("C")
    G.create_node("D")
    G.create_node("E")
    G.create_node("F")
    G.create_node("G")
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
    print(G.__connections__)

    B = Kruskal(G)
    print("Kruskal:")
    print(B.__connections__)
    print("Edges:")
    print([x.__name__ for x in B.__edges__])

#1. stworzenie grafu który ma takie same krawędzie, węzły ale nie połączenia 
#2. posortowanie krawędzi 
#3 funkcja, check if no cycle 
#4 dodanie lub nie krawędzi
#5 przejście do kolejnej krawędzi 
