import subprocess
import graph
import pebbling
import all_graphs

def write_answer(n, d, answer, q, graph_num, folder_name='pebbling_nums'):
    with open(f'diameter-2/graph{n}-{q}.txt', 'a') as f:
        f.write(f'{graph_num} {n} {d} {answer}\n')

def do_all_n_q(n, q):
    graph_num = 1
    count_evaluated = 0
    lines = all_graphs.get_lines_by_graph_num(n, graph_num)

    while len(lines) > 1:
        print(graph_num)

        g = all_graphs.make_from_edge_list(lines[3])

        diameter = graph.Graph.calculate_diameter(g)

        ve_data = lines[2].split(' ')
            
        edges = int(ve_data[1])
        class_0_threshold = (n - 1) * (n - 2) / 2 + q
        if edges >= class_0_threshold:
            write_answer(n, diameter, (n - 1) * (q - 1) + 1, q, graph_num)
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            count_evaluated += 1
            continue

        if diameter > 2:
            graph_num += 1
            lines = all_graphs.get_lines_by_graph_num(n, graph_num)
            continue

        answer = pebbling.pebbling_number(g, q=q, d=diameter)
        count_evaluated += 1

        write_answer(n, diameter, answer, q, graph_num)

        graph_num += 1
        lines = all_graphs.get_lines_by_graph_num(n, graph_num)
    
    with open(f'diameter-2/graph{n}-{q}.txt', 'a') as f:
        f.write(f'Evaluated {count_evaluated} graphs\n')

if __name__ == '__main__':
    q = 2
    for n in range(3, 4):

        print(n)

        do_all_n_q(n, q)