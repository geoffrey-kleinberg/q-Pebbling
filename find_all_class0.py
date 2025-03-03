import all_graphs
import graph
import pebbling

def write_class_0(n, edges, q, graph_num):
    with open(f'class0/graphs-{q}-2.txt', 'a') as f:
        f.write(f'{n}: {graph_num} {edges}\n')

def do_all_n_q(n, q):
    class_0_pebbles = (n - 1) * (q - 1) + 1

    graph_num = 1
    lines = all_graphs.get_lines_by_graph_num(n, graph_num)

    checked = 0

    while len(lines) > 1:
        if graph_num % 100 == 0:
            print(graph_num)

        ve_data = lines[2].split(' ')
        vertices = int(ve_data[0])
        if vertices != n:
            print(f'Error: vertices = {vertices}, n = {n}')
            break
            
        edges = int(ve_data[1])

        if edges != 17:
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            continue
        else:
            checked += 1
            print(f'checking = {checked} of 31400')
        

        class_0_threshold = (n - 1) * (n - 2) / 2 + q
        if edges >= class_0_threshold:
            write_class_0(n, edges, q, graph_num)
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            continue

        g = all_graphs.make_from_edge_list(lines[3])

        diameter = graph.Graph.calculate_diameter(g)

        if q ** diameter > class_0_pebbles:
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            continue

        answer = pebbling.pebbling_number(g, q=q, d=diameter, cap=class_0_pebbles)

        if answer == class_0_pebbles:
            write_class_0(n, edges, q, graph_num)
        
        

        graph_num += 1
        lines = all_graphs.get_lines_by_graph_num(n, graph_num)

if __name__ == '__main__':
    q = 3

    for n in range(9, 10):
        print(f'n = {n}')
        do_all_n_q(n, q)