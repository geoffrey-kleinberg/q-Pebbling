import graph
import pebbling
import utilities

def do_all_n_q(n, q):
    utilities.clear_file(n, q, 'pebbling_nums')

    graph_num = 1
    lines = utilities.get_lines_by_graph_num(n, graph_num)

    evaluated = 0

    while len(lines) > 1:
        print(graph_num)

        ve_data = lines[2].split(' ')
        vertices = int(ve_data[0])
        if vertices != n:
            print(f'Error: vertices = {vertices}, n = {n}')
            break
            
        edges = int(ve_data[1])
        

        class_0_threshold = (n - 1) * (n - 2) / 2 + q
        if edges >= class_0_threshold:
            utilities.write_answer(n, edges, (n - 1) * (q - 1) + 1, q, graph_num, 'pebbling_nums')
            graph_num += 1
            lines = utilities.get_lines_by_graph_num(n, graph_num)
            continue


        g = utilities.make_from_edge_list(lines[3])

        diameter = graph.Graph.calculate_diameter(g)
        evaluated += 1

        answer = pebbling.pebbling_number(g, q=q, d=diameter)

        utilities.write_answer(n, edges, answer, q, graph_num, 'pebbling_nums')

        graph_num += 1
        lines = utilities.get_lines_by_graph_num(n, graph_num)

    with open(f'pebbling_nums/graph{n}-{q}.txt', 'a') as f:
        f.write(f'Evaluated {evaluated} graphs\n')

if __name__ == '__main__':
    
    q = 2
    n = 3

    do_all_n_q(n, q)