import graph
import utilities
import math
import itertools
import all_graphs

# https://users.cecs.anu.edu.au/~bdm/data/graphs.html

def all_configurations_work(g, pebbles, w, n, memo):

    memo[pebbles] = {}

    all_work = True

    for config in itertools.combinations(range(pebbles + n - 1), n - 1):
        config_arr = []
        prev = -1
        for i in config:
            config_arr.append(i - prev - 1)
            prev = i

        config_arr.append(pebbles + n - 1 - prev - 1)

        id = tuple(config_arr)

        possible = set(())

        # then, for each possible move add the child's possible vertices to this one's possible vertices
        for i in range(n):
            if config_arr[i] == 0:
                continue

            if config_arr[i] >= 1:
                possible.add(i)

            if config_arr[i] >= w:
                for neighbor in g.get_neighbors(i):
                    copy = list(config_arr)
                    copy[i] -= w
                    copy[neighbor] += 1
                    possible = possible.union(memo[pebbles - w + 1][tuple(copy)])

        memo[pebbles][id] = possible

        if len(possible) != n:
            all_work = False
            if pebbles == 34:
                print(config_arr)
                pass

    memo[pebbles - w + 1] = None

    return all_work

def pebbling_number(g, q=2, d=None, cap=float('inf')):

    n = g.size
    if d is None:
        d = graph.Graph.calculate_diameter(g)

    worst = (n - 1) * (q ** d - 1) + 1

    worst = min(worst + 1, cap + 1)

    memo = {}

    for pebbles in range(1, worst):
        if all_configurations_work(g, pebbles, q, n, memo):
            return pebbles
        
        if pebbles == worst - 1:
            return f'>{worst - 1}'
        
    return worst

if __name__ == '__main__':

    g = all_graphs.get_graph_by_graph_num(7, 446)
    print(g.graph)
    print(pebbling_number(g, q=4))