"""
Connected components and graph resilience
"""
import poc_queue
import random
import alg_module2_graphs
#import codeskulptor

#codeskulptor.set_timeout(50)

# LoS = [set([1,2]), set([0])]
# print LoS.extend(set([5]))

EX_GRAPH0 = {0: set([1, 2]), 1: set([0]), 2: set([0]), 3: set([4]),
             4: set([3]), 5: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]),
             3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
             3: set([7]), 4: set([1]), 5: set([2]), 6: set([]),
             7: set([3]), 8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def bfs_visited(ugraph, start_node):
    """
    Takes starting node and visit its neighbor
    and neigbor of neigbor until all are visited.
    No path to starting node won't be returned.
    """
    visited = set([])
    visited.add(start_node)

    _queue = poc_queue.Queue()
    _queue.enqueue(start_node)
    while _queue:
        key = _queue.dequeue()
        for value in ugraph[key]:
            if value not in visited:
                visited.add(value)
                _queue.enqueue(value)
    return visited


def cc_visited(ugraph):
    """
    Takes a undirected graph and computes the nodes
    in a connected component. Return a list of set.
    """

    renodes = set([])
    _cc = []
    for value in ugraph.values():
        renodes = set(ugraph.keys()).union(value)
    while renodes:
        node = random.choice(list(renodes))
        visited = bfs_visited(ugraph, node)
        _cc.append(visited)
        renodes.difference_update(visited)
    return _cc


def largest_cc_size(ugraph):
    """
    Takes a undirected graph and computes the
    largest size of connected component.
    """
    max_val = 0
    for value in cc_visited(ugraph):
        if len(value) > max_val:
            max_val = len(value)
    return max_val


def compute_resilience(ugraph, attack_order):
    """
    Takes a directed graph and computes the
    unnormalized distribution of the in-degrees
    of the graph.
    """
    value = []
    value.append(largest_cc_size(ugraph))
    for node in attack_order:
        for edge in list(ugraph.pop(node)):
            ugraph[edge].remove(node)
        value.append(largest_cc_size(ugraph))

    return value


## print make_complete_graph(4)
# print bfs_visited(EX_GRAPH0, 0)
# print "cc_visited", cc_visited(EX_GRAPH0)


# print "largest_cc_size", largest_cc_size(alg_module2_graphs.GRAPH0)
print bfs_visited(alg_module2_graphs.GRAPH5, "cat")
# attack_order = [1,4]
# print compute_resilience(EX_GRAPH0, attack_order)
# print compute_resilience(alg_module2_graphs.GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])
## print in_degree_distribution(EX_GRAPH1)
