import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._areoporti = DAO.getAllAereoporti()
        self._grafo = nx.Graph()
        self._idMapAereoporti = {}
        for v in self._areoporti:
            self._idMapAereoporti[v.ID] = v

    def buildGraph(self,distanza):
        self._grafo.add_nodes_from(self._areoporti)
        self._grafo.clear_edges()
        self.addEdges(distanza)

    def addEdges(self, distanza):
        """
        Faccio una query che prende tutti gli archi e poi
        lavoro su python
        """
        self._grafo.clear_edges()

        allEdges = DAO.getAllEdges()
        for edge in allEdges:
            u = self._idMapAereoporti[edge.ORIGIN_AIRPORT_ID]
            v = self._idMapAereoporti[edge.DESTINATION_AIRPORT_ID]
            print(edge.DISTANCE)
            if edge.DISTANCE >= int(distanza):
                print(edge)
                self._grafo.add_edge(u, v, weight=edge.DISTANCE)


    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)