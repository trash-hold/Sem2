from abc import ABC, abstractmethod, abstractproperty

class AbstractGraph(ABC):
    
    def __init__(self, file_name):
        self.__alphabet__ = list()
        self.__nodes__ = list()
        self.__connections__ = None
    
    @abstractproperty
    def nodes(self):
        pass

    @abstractproperty
    def connections(self):
        pass

    @abstractmethod
    def create_connection(self, _from, _to, directed = False):
        pass

    @abstractmethod
    def delete_connection(self, _from, _to, directed = False):
        pass

    @abstractmethod
    def create_node(self, type, name):
        pass

    @abstractmethod
    def delete_node(self, name):
        pass
