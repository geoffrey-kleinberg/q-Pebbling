import all_graphs
import graph
import pebbling

def find_num_to_check(n, q):

    class_0_pebbles = (n - 1) * (q - 1) + 1

    num_to_check = 0

    graph_num = 1
    lines = all_graphs.get_lines_by_graph_num(n, graph_num)

    while len(lines) > 1:
        if graph_num % 100 == 0:
            print(graph_num)

        ve_data = lines[2].split(' ')
        vertices = int(ve_data[0])
        if vertices != n:
            print(f'Error: vertices = {vertices}, n = {n}')
            break
            
        edges = int(ve_data[1])
        

        class_0_threshold = (n - 1) * (n - 2) / 2 + q
        if edges >= class_0_threshold:
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            continue
            

        g = all_graphs.make_from_edge_list(lines[3])

        diameter = graph.Graph.calculate_diameter(g)

        if q ** diameter > class_0_pebbles:
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            continue

        num_to_check += 1

        graph_num += 1
        lines = all_graphs.get_lines_by_graph_num(n, graph_num)


    return num_to_check

if __name__ == '__main__':
    q = 3

    for n in range(9, 10):
        print(f'n = {n}')
        num_to_check = find_num_to_check(n, q)
        print(f'num_to_check = {num_to_check}')