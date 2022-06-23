from abstract_graph import AbstractGraph
from abc import ABC, abstractmethod, abstractproperty
import numpy as np

class Node:
    def __init__(self, type, name):
        #node_type values: 0 - beg, 1- middle, 2 - end
        if type not in [1, 2, 0]:
            raise NotImplementedError("Node_innit failure, type not in scope")
        if name is None:
            raise NotImplementedError("Node_innit failure, name is empty")
        self.__type__ = type  
        self.__name__ = name    

class Graph(AbstractGraph):
    def __init__(self, file_name):
        self.__alphabet__ = list()
        self.__nodes__ = list()
        self.__connections__ = None
    
    def nodes(self):
        return [Node(x.__type__, x.__name__) for x in self.__nodes__]

    def connections(self):
        return np.copy(self.__connections__)

    def create_connection(self, _from, _to, directed = False):
        #from, to are names of nodes
        ind_from = [i.__name__ for i in self.__nodes__].index(_from)
        ind_to = [i.__name__ for i in self.__nodes__].index(_to)

        self.__connections__[ind_from][ind_to] = 1
        if directed == False:
            self.__connections__[ind_to][ind_from] = 1

    def delete_connection(self, _from, _to, directed = False):
        ind_from = [i.__name__ for i in self.__nodes__].index(_from)
        ind_to = [i.__name__ for i in self.__nodes__].index(_to)

        self.__connections__[ind_from][ind_to] = 0
        if directed == False:
            self.__connections__[ind_to][ind_from] = 0

    def create_node(self, type, name):
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

if __name__ == "__main__":
    G = Graph(None)
    G.create_node(0, "A")
    G.create_node(1, "B")
    G.create_node(1, "C")
    print(G.__connections__)
    G.create_connection("A", "B")
    print(G.__connections__)
    G.create_connection("A", "C")
    print(G.__connections__)