import graph
import all_graphs
import math

def all_a_in_b(a ,b):
    for i in a:
        if i not in b:
            print(i)
    return True

if __name__ == '__main__':
    two_pebbling_nums = {}
    three_pebbling_nums = {}

    for n in range(3, 7):
        two_pebbling_nums[n] = {}
        three_pebbling_nums[n] = {}
        with open(f'pebbling_nums/graph{n}-2.txt', 'r') as f:
            for line in f:
                data = line.split(': ')
                two_pebbling_nums[n][int(data[0])] = int(data[1].split(" ")[2])

        with open(f'pebbling_nums/graph{n}-3.txt', 'r') as f:
            for line in f:
                data = line.split(': ')
                three_pebbling_nums[n][int(data[0])] = int(data[1].split(" ")[2])
    
    # print(two_pebbling_nums)
    # print(three_pebbling_nums)

    for n in range(3, 7):
        for id in range(1, max(three_pebbling_nums[n].keys()) + 1):
            lines = all_graphs.get_lines_by_graph_num(n, id)
            g = all_graphs.make_from_edge_list(lines[3])
            diameter = graph.Graph.calculate_diameter(g)
            
            pi2 = two_pebbling_nums[n][id]
            pi3 = three_pebbling_nums[n][id]
            if pi3 > pi2 + (3 ** diameter - 2 ** diameter) * math.floor(pi2 / (2 ** diameter - 1)):
                print(diameter)
                print(f'{n}: {id} pi2 = {pi2}, pi3 = {pi3}')