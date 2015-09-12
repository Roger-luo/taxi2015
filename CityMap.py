__author__="Lingyuan Ji"

import networkx as nx
import Position as ps


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

    def add_node(self, node_list):
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
        for node in node_list:
            self.graph.add_node(node)

    def add_arc(self, arc_tuple_list):
        """
        Parameters
        ----------
        self : CityMap
            self object

        Returns
        -------
        Null
        """
        self.graph.add_weighted_edges_from(arc_tuple_list)

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
        ans = self.graph.edge[arc_tuple[0]][arc_tuple[1]]["weight"]
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
        pass

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
        pass

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
        pass

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
                           self.graph.edge\
                           [position1.arc[0]][position1.arc[1]]["weight"]
        else:
            modified_graph = self.graph.copy
            begin1 = position1.arc[0]
            end1 = position1.arc[1]
            length1 = modified_graph.edge[begin1][end1]["weight"]
            modified_graph.remove_edge(begin1, end1)
            modified_graph.add_node("temp1")
            modified_graph.add_weighted_edges_from\
                ([(begin1, "temp1", length1*position1.location)])
            modified_graph.add_weighted_edges_from\
                ([("temp1", end1, length1*(1-position1.location))])
            begin2 = position2.arc[0]
            end2 = position2.arc[1]
            length2 = modified_graph.edge[begin2][end2]["weight"]
            modified_graph.remove_edge(begin2, end2)
            modified_graph.add_node("temp2")
            modified_graph.add_weighted_edges_from\
                ([(begin2, "temp2", length2*position2.location)])
            modified_graph.add_weighted_edges_from\
                ([("temp2", end2, length2*(1-position2.location))])
            min_distance = nx.shortest_path_length\
                           (modified_graph.to_undirected, \
                            "temp1", "temp2", weight="weight")
        return min_distance
