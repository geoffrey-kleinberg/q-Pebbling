import graph
import pebbling
import utilities

def do_all_n_q(n, q):

    utilities.clear_file(n, q, 'class0')

    class_0_pebbles = (n - 1) * (q - 1) + 1

    graph_num = 1
    lines = utilities.get_lines_by_graph_num(n, graph_num)

    evaluated = 0

    while len(lines) > 1:

        ve_data = lines[2].split(' ')
        vertices = int(ve_data[0])
        if vertices != n:
            print(f'Error: vertices = {vertices}, n = {n}')
            break
            
        edges = int(ve_data[1])
        

        class_0_threshold = (n - 1) * (n - 2) / 2 + q
        if edges >= class_0_threshold:
            utilities.write_answer(n, edges, class_0_pebbles, q, graph_num, 'class0')
            graph_num += 1
            lines = utilities.get_lines_by_graph_num(n, graph_num)
            continue

        g = utilities.make_from_edge_list(lines[3])

        diameter = graph.Graph.calculate_diameter(g)

        if q ** diameter > class_0_pebbles:
            graph_num += 1
            lines = utilities.get_lines_by_graph_num(n, graph_num)
            continue

        answer = pebbling.pebbling_number(g, q=q, d=diameter, cap=class_0_pebbles)
        evaluated += 1

        if answer == class_0_pebbles:
            utilities.write_answer(graph_num, edges, class_0_pebbles, q, graph_num, 'class0')

        graph_num += 1
        lines = utilities.get_lines_by_graph_num(n, graph_num)

    with open(f'diameter-2/graph{n}-{q}.txt', 'a') as f:
        f.write(f'Evaluated {evaluated} graphs\n')

    

if __name__ == '__main__':
    q = 2

    for n in range(4, 5):
        print(f'n = {n}')
        do_all_n_q(n, q)