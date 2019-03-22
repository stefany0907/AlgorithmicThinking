"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""
GRAPH1 = {1001: set(
    [9304045, 1004, 1002, 9311042, 1019, 9404151, 9407087, 1016, 1011, 9503124, 9504090, 9504145, 9505025, 9505054,
     9505105, 9505162, 9506048, 9506112, 9506144, 9507050, 9507158, 9508094, 9508155, 1017, 1013, 1018, 9511030,
     9511171, 9601108, 9602022, 9602114, 9603003, 9603150, 9603161, 9603167, 9605184, 9605222, 9606017, 9606040,
     9607163, 1001, 9608086, 9609070, 9609071, 9609239, 9611137, 9612108, 1009, 1007, 9702155, 1015, 9703082, 9703166,
     9704097, 9705030, 9705044, 9705104, 9705220, 9706005, 9707014, 9707042, 9707049, 9710230, 9711036, 9711104,
     9712028, 9712042, 9802194, 9805056, 9805206, 9806094, 9810188, 9811217, 9905036, 9907041, 9908007, 9908144,
     9909108, 9909120, 9909229, 9910238, 9910248, 9910268]), 1002: set(
    [9201007, 1016, 9210123, 9304062, 9306005, 1001, 9604090, 9803235, 9807051, 9809015, 9810063, 9812035, 9902125,
     9902155, 9904017, 9905012, 9905210, 9906064, 9906194, 9907070, 9907209, 9908076, 9908116, 9908186, 9909001,
     9909041, 9909053, 9909058, 9909121, 9909134, 9910149, 9910219, 9912012, 9912118, 9912132, 9912187]),
          1003: set([9912242]), 1004: set([9810131]), 1005: set(
        [1004, 9506135, 9601078, 9603097, 9611092, 9611194, 9712257, 9805026, 9811178, 9901099, 9902132, 9904145,
         9908025, 9908036, 9908040, 9909030, 9909114, 9909140, 9909163, 9910148, 9912239]), 1006: set([9910243]),
          1007: set([9405171, 9807069, 9901148, 9911150]),
          1008: set([9301008, 1007, 9303112, 9405029, 9409139, 9507046]), 1009: set([9610215]),
          1010: set([9603136, 9608174, 9706225, 9808157, 9901128]), 1011: set(
        [9510135, 9610043, 9612115, 1011, 9703078, 9708039, 9710231, 9711162, 9711200, 9712072, 9804041, 9804163,
         9805069, 9902004, 9903205, 9907211, 9908019, 9908142, 9909081, 9909176]),
          1012: set([9205059, 9206053, 9302035, 9306002, 9403141, 9405136, 9506136, 9507109, 9702190, 9911110]),
          1013: set([1002, 1003, 9906064, 9907209, 9909076, 9909127, 9909130, 9909205, 9911055, 9911234, 9912276]),
          1014: set([9502097, 9606100, 9803011, 9806244, 9807215, 1015, 9903266, 1004]), 1015: set([9811016]),
          1016: set([9607049, 9711002, 9711200, 9802109, 9802150, 9805114, 9806087, 9806217, 9807226, 9808057, 9810126,
                     9902012, 9903190, 9903241, 9906164, 9907158, 9911215, 9912012, 9912018]),
          1017: set([9609035, 9610193, 9807069, 9808129, 9811053, 9811077, 9811171, 9902140, 9903223, 9905215]),
          1018: set([9603087, 9604035, 9604179, 9609212, 9701042, 9801049, 9802163, 9906048, 9906064, 9908076, 9909130,
                     9909205, 9911043, 9911218, 9912118, 9912135, 9912175, 9912242]),
          1019: set([2049, 9605022, 9703097, 9707253, 9908101, 9908149, 9909210, 9912176, 9912223]),
          1020: set([9805177]), 1021: set(
        [9401139, 9406206, 9505186, 9510017, 9604136, 9606187, 9609198, 9701178, 9704157, 9705105, 9705193, 9801102,
         9806068, 9906007, 9912105]), 1022: set([1016, 1004, 1012])}
# general imports
import urllib2
import math
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    import SimpleGUICS2Pygame.simpleplot as simpleplot

import random

# Set timeout for CodeSkulptor if necessary
#import codeskulptor

#codeskulptor.set_timeout(50)

###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and
    returns a dictionary corresponding to a complete
    directed graph with the specified number of nodes.
    """
    assert num_nodes > 0, "num_nodes is negative."
    graph = {}
    for node in range(num_nodes):
        setlst = range(num_nodes)
        setlst.remove(node)
        ## print setlst
        graph[node] = set(setlst)
    return graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph and computes the
    in-degrees for the nodes in the graph.
    """
    graph = {}
    for key in digraph.keys():
        graph[key] = 0

    for value in digraph.values():
        for items in value:
            if items not in graph:
                graph[items] = 1
            else:
                graph[items] += 1
    return graph


def in_degree_distribution(digraph):
    """
    Takes a directed graph and computes the
    unnormalized distribution of the in-degrees
    of the graph.
    """
    graph = {}
    dstr = compute_in_degrees(digraph)
    for value in dstr.values():
        if value not in graph:
            graph[value] = 1
        else:
            graph[value] += 1
    return graph


def normal_distribution(distribution):
    """
    Take in_degree_distribution graph do normalization.
    """
    dist_log = {}
    dist_sum = sum(distribution.values())
    distribution.pop(0)
    print distribution
    print "dist_sum=", dist_sum
    print "math.log()", math.log10(2424)
    for key in distribution:
        # print float(distribution[key])/dist_sum
        dist_log[math.log(key)] = math.log(1.0 * (distribution[key]) / dist_sum)
    return dist_log


def compute_avg_out_degrees(digraph):
    sum = 0
    _i = 0
    for value in digraph.values():
        sum = sum + len(value)
        _i = _i + 1
    print "_i, sum", _i, sum
    return round(sum * 1.0 / _i * 1.0)


def ER(n, p):
    graph = {}
    for _i in range(n):
        items = set([])
        for _j in range(n):
            a = random.random()
            if _i != _j:
                if a < p:
                    items.add(_j)
        graph[_i] = items
    return graph


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        # update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


print "-----------------assignment 1--------------------------"
# citation_graph = load_graph(CITATION_URL)
# GRAPH1 = citation_graph
# print citation_graph
# print compute_in_degrees(GRAPH1)
# print "out_dg=", compute_avg_out_degrees(GRAPH1)

# dist = in_degree_distribution(GRAPH1)
# print dist

# print sum(in_degree_distribution(GRAPH1).values())
# distlog = normal_distribution(dist)
# print "distlog=", [distlog]

# simpleplot.plot_scatter("Normalized in Degree Distribution log-log", 600, 600,
#                        "in-degree (log)", "counts (log)", [distlog])


print "-----------------assignment 2--------------------------"
print
# k = 13*1.0 / 27700
# GRAPH2 = ER(1, k)
# dist2 = in_degree_distribution(GRAPH2)
# print "dist2=", dist2
# distlog2 = normal_distribution(dist2)

# simpleplot.plot_scatter("Normalized in Degree Distribution log-log", 600, 600,
#                      "in-degree", "counts", [distlog2])

print "-----------------assignment 3--------------------------"

m = 13
n = 27700

print "-----------------assignment 4--------------------------"

# m = 2
# n = 5
digraph = make_complete_graph(m)
print digraph
DPA = DPATrial(m)
# print "DPA._num_nodes", DPA._num_nodes
# print "DPA._node_numbers", DPA._node_numbers
print "trial1", DPA.run_trial(m)
print "node_number_after_trial=", DPA._node_numbers
# print "trial2", DPA.run_trial(m+1)
# print DPA._node_numbers
for idx in range(m, n):
    digraph[idx] = DPA.run_trial(m)
print digraph
dist4 = in_degree_distribution(digraph)
distlog4 = normal_distribution(dist4)
simpleplot.plot_scatter("Normalized in Degree Distribution log-log", 600, 600,
                        "in-degree", "counts", [distlog4])
