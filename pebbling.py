import graph
import utilities
import math
import itertools
import all_graphs

# https://users.cecs.anu.edu.au/~bdm/data/graphs.html

def all_configurations_work(g, pebbles, q, n, memo):

    '''
    memo is a dictionary where the keys are the number of pebbles
    and the values are dictionaries where the keys are configurations
    of pebbles and the values are sets of vertices that can be
    q-pebbled from that configuration. memo[pebbles] is initialized
    as an empty dictionary
    '''
    memo[pebbles] = {}

    # We begin by assuming that all configurations of pebbles work
    all_work = True

    # We iterate over all possible configurations of pebbles
    # using the stars and bars technique
    for config in itertools.combinations(range(pebbles + n - 1), n - 1):

        # This array stores the number of pebbles on each vertex
        config_arr = []
        prev = -1
        for i in config:
            config_arr.append(i - prev - 1)
            prev = i
        config_arr.append(pebbles + n - 1 - prev - 1)
        id = tuple(config_arr)

        # This set stores the vertices that can be q-pebbled
        # from the current configuration
        possible = set(())

        # We iterate over all vertices
        for i in range(n):
            # If there are no pebbles on the vertex, we skip it
            if config_arr[i] == 0:
                continue

            # If there is at least one pebble on the vertex, we add it
            # to the set of possible vertices
            if config_arr[i] >= 1:
                possible.add(i)

            # If there are at least q pebbles on the vertex, we can make
            # a move to a neighbor
            if config_arr[i] >= q:
                for neighbor in g.get_neighbors(i):
                    copy = list(config_arr)
                    # Perform the move
                    copy[i] -= q
                    copy[neighbor] += 1

                    # For each neighbor that we move to, we add the vertices 
                    # that can be q-pebbled from the new configuration to 
                    # the set of possible vertices
                    possible = possible.union(memo[pebbles - q + 1][tuple(copy)])

        # We store the set of possible vertices in the memo
        memo[pebbles][id] = possible

        # If any vertex is not in the set of possible vertices, then
        # the current configuration does not work, so we set all_work
        # to False
        if len(possible) != n:
            all_work = False

    # We can delete the memo entry for pebbles - q + 1
    memo[pebbles - q + 1] = None

    return all_work

def pebbling_number(g, q=2, d=None, cap=float('inf')):

    # n is the number of vertices
    n = g.size
    # If d is not given, we calculate the diameter of the graph
    if d is None:
        d = graph.Graph.calculate_diameter(g)

    # We use the bound given in Theorem 2.2.8 to calculate the worst case
    worst = (n - d) * (q ** d - 1) + 1

    # If the user specifies a cap, we take the minimum of the worst case
    # and the cap
    worst = min(worst + 1, cap + 1)

    memo = {}

    # Counting upwards from 1 to the worst case, we check if all
    # configurations of pebbles work
    for pebbles in range(1, worst):
        if all_configurations_work(g, pebbles, q, n, memo):
            return pebbles
        
        if pebbles == worst - 1:
            return f'>{worst - 1}'

if __name__ == '__main__':

    g = graph.Graph.make_from_file('graphs/cycle3.txt')
    print(pebbling_number(g, q=2))