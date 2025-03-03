import subprocess
import graph
import pebbling

def get_graph_by_graph_num(n, graph_num):
    lines = get_lines_by_graph_num(n, graph_num)

    g = make_from_edge_list(lines[3])

    return g

def get_lines_by_graph_num(n, graph_num):
    graph = subprocess.run(['./showg', f'-p{graph_num}', '-e', f'all_graphs/graph{n}c.g6'], check=True, capture_output=True).stdout.decode('utf-8')

    graph = graph.split('\n')

    if len(graph) < 4:
        return []

    graph[3] = '  '.join([i.strip() for i in graph[3:]]).strip()

    return graph

def write_answer(n, edges, answer, q, graph_num, folder_name='pebbling_nums'):
    with open(f'{folder_name}/graph{n}-{q}.txt', 'a') as f:
        f.write(f'{graph_num}: {n} {edges} {answer}\n')

def make_from_edge_list(edge_list):
    g = graph.Graph()
    for edge in edge_list.split('  '):
        u, v = edge.split(' ')
        g.add_edge(int(u), int(v))
        g.add_edge(int(v), int(u))

    return g

def do_all_n_q(n, q):
    graph_num = 1
    lines = get_lines_by_graph_num(n, graph_num)

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
            write_answer(n, edges, (n - 1) * (q - 1) + 1, q, graph_num)
            graph_num += 1
            lines = get_lines_by_graph_num(n, graph_num)
            continue


        g = make_from_edge_list(lines[3])

        diameter = graph.Graph.calculate_diameter(g)

        answer = pebbling.pebbling_number(g, q=q, d=diameter)

        write_answer(n, edges, answer, q, graph_num)

        graph_num += 1
        lines = get_lines_by_graph_num(n, graph_num)

if __name__ == '__main__':
    q = 3
    for n in range(3, 7):

        print(n)

        do_all_n_q(n, q)