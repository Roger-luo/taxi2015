__author__ = "Lingyuan Ji"

import networkx as nx
import Position as ps
import numpy as np
import matplotlib.pyplot as plt
from PassengerList import PassengerList
from TaxiList import TaxiList

class CityMap(object):
    """
    definition of class CityMap
    using the networkx module
    """
    def __init__(self):
        """
        Parameters
        ----------
        self : CityMap
            self object

        Returns
        -------
        Null
        """
        self.graph = nx.DiGraph()
        self.coordinate = {}

    def add_node(self, node_id, coordinate):
        """
        Parameters
        ----------
        self : CityMap
            self object
        node_list : node key type (use int)
            key ID of the node

        Returns
        -------
        Null
        """
        self.graph.add_node(node_id)
        self.coordinate[node_id] = coordinate

    def add_arc(self, i, j):
        """
        Parameters
        ----------
        self : CityMap
            self object

        Returns
        -------
        Null
        """
        node_i = self.coordinate[i]
        node_j = self.coordinate[j]
        norm = np.sqrt(np.dot(node_i-node_j, node_i-node_j))
        self.graph.add_edge(i, j, length=norm)

    def arc_length(self, arc_tuple):
        """
        Parameters
        ----------
        self : CityMap
            self object
        arc_tuple : tuple
            tuple describe arc

        Returns
        -------
        ans : float
            arc length of a given arc
        """
        ans = (self.graph.to_undirected()).edge[arc_tuple[0]][arc_tuple[1]]["length"]
        return ans

    def neighbor_nodes(self, node_id):
        """
        Parameters
        ----------
        self : CityMap
            self object
        node_id : int
            node id, between [0, n-1]

        Returns
        -------
        neighbor_nodes : list
            node id list of neighbor nodes
        """
        neighbor_nodes = [node for node in (self.graph.to_undirected()).edge[node_id]]
        return neighbor_nodes

    def direction(self, arc_tuple):
        if arc_tuple[1] in self.graph.edge[arc_tuple[0]]:
            return True
        else:
            return False

    def random_choose(self, node_id):
        tmp = self.neighbor_nodes(node_id)
        dice = np.random.randint(len(tmp))
        return tmp[dice]

    def coordinate(self, node_id):
        """
        Parameters
        ----------
        self : CityMap
            self object
        node_id : int
            node id, between [0, n-1]

        Returns
        -------
        coordinate : numpy.array
            the [x,y] coordinate of the node
        """
        coordinate = self.coordinate[node_id]
        return coordinate

    def position_coordinate(self, position):
        """
        Parameters
        ----------
        self : CityMap
            self object
        position : Position
            the Position description

        Returns
        -------
        coordinate : numpy.array
            the [x,y] coordinate of the position
        """
        if self.direction(position.arc) == True:
            begin_node = self.coordinate[position.arc[0]]
            end_node = self.coordinate[position.arc[1]]
            road_vector = end_node - begin_node
            relative_vector = road_vector * position.location
            position_vector = relative_vector + begin_node
        else:
            begin_node = self.coordinate[position.arc[1]]
            end_node = self.coordinate[position.arc[0]]
            road_vector = end_node - begin_node
            relative_vector = road_vector * (1 - position.location)
            position_vector = relative_vector + begin_node
        return position_vector

    def min_distance(self, position1, position2):
        """
        Parameters
        ----------
        self : CityMap
            self object
        position1 : Position
            position of object 1
        position2 : Position
            position of object 2

        Returns
        -------
        min_distance : float
            the minimal distance between the two object
        """

        if position1.arc == position2.arc:
            min_distance = abs(position1.location-position2.location)*\
                           (self.graph.to_undirected()).edge\
                           [position1.arc[0]][position1.arc[1]]["length"]
        else:
            modified_graph = self.graph.copy()
            begin1 = position1.arc[0]
            end1 = position1.arc[1]
            print begin1, end1
            length1 = modified_graph.edge[begin1][end1]["length"]
            modified_graph.remove_edge(begin1, end1)
            modified_graph.add_node("temp1")
            modified_graph.add_weighted_edges_from\
                ([(begin1, "temp1", length1*position1.location)])
            modified_graph.add_weighted_edges_from\
                ([("temp1", end1, length1*(1-position1.location))])
            begin2 = position2.arc[0]
            end2 = position2.arc[1]
            print begin2, end2
            length2 = modified_graph.edge[begin2][end2]["length"]
            modified_graph.remove_edge(begin2, end2)
            modified_graph.add_node("temp2")
            modified_graph.add_weighted_edges_from\
                ([(begin2, "temp2", length2*position2.location)])
            modified_graph.add_weighted_edges_from\
                ([("temp2", end2, length2*(1-position2.location))])
            min_distance = nx.shortest_path_length\
                           (modified_graph.to_undirected(), \
                            "temp1", "temp2", weight="length")
        return min_distance

    def plot_now(self, passenger_list, taxi_list):
        nodes_x=[self.coordinate[node][0] for node in self.coordinate]
        nodes_y=[self.coordinate[node][1] for node in self.coordinate]
        plt.plot(nodes_x, nodes_y, "ko", markersize=10.0, alpha=0.75)
        for node_i in self.graph.edge:
            for node_j in self.graph.edge[node_i]:
                node_i_x=self.coordinate[node_i][0]
                node_i_y=self.coordinate[node_i][1]
                node_j_x=self.coordinate[node_j][0]
                node_j_y=self.coordinate[node_j][1]
                plt.plot([node_i_x, node_j_x],[node_i_y, node_j_y], "k-", alpha=0.5, linewidth=3.0)
        passenger_coordinate=\
        [self.position_coordinate(passenger.position) for passenger in passenger_list]
        passengers_x=[passenger[0] for passenger in passenger_coordinate]
        passengers_y=[passenger[1] for passenger in passenger_coordinate]
        plt.plot(passengers_x, passengers_y, "yo", markersize=10.0, alpha=0.75)
        taxi_coordinate=\
        [self.position_coordinate(taxi.position) for taxi in taxi_list]
        taxis_x=[taxi[0] for taxi in taxi_coordinate]
        taxis_y=[taxi[1] for taxi in taxi_coordinate]
        plt.plot(taxis_x, taxis_y, "go", markersize=10.0, alpha=0.75)
        plt.show()
