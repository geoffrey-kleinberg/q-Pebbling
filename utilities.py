import graph
import subprocess
import itertools

def make_cycle_graph(n):
    file_path = f'graphs/cycle{n}.txt'

    with open(file_path, 'w') as f:
        f.write('')

    for i in range(n):
        with open(file_path, 'a') as f:
            f.write(f'{i}:{(i+1)%n},{(i-1)%n}\n')

def make_kneser_graph(n, k):
    file_path = f'graphs/kneser/k{n}k{k}.txt'

    with open(file_path, 'w') as f:
        f.write('')

    for c1 in zip(itertools.combinations(range(n), k), itertools.count()):
        neighbors = []
        for c2 in zip(itertools.combinations(range(n), k), itertools.count()):
            if len(set(c1[0]).intersection(set(c2[0]))) == 0:
                neighbors.append(c2[1])

        with open(file_path, 'a') as f:
            f.write(f'{c1[1]}:')
            for neighbor in neighbors:
                f.write(f'{neighbor},')
            f.write('\n')


def make_kn_cross_pm(n, m):
    file_path = f'graphs/kn_cross_pm/k{n}xp{m}.txt'

    with open(file_path, 'w') as f:
        f.write('')

    for i in range(m):
        for j in range(n):
            with open(file_path, 'a') as f:
                f.write(f'{i*n+j}:')
                for k in range(1, n):
                    f.write(f'{i*n+(j+k)%n},')
                if i > 0 and i < m-1:
                    f.write(f'{(i-1)*n+j},')
                    f.write(f'{(i+1)*n+j}')
                if i == m-1:
                    f.write(f'{(i-1)*n+j}')
                if i == 0:
                    f.write(f'{(i+1)*n+j}')

                f.write('\n')

def make_wheel_graph(n):
    file_path = f'graphs/wheels/wheel{n}.txt'

    with open(file_path, 'w') as f:
        f.write('')

    for i in range(0, n - 1):
        with open(file_path, 'a') as f:
            f.write(f'{i}:')
            f.write(f'{n-1},')
            f.write(f'{(i+1)%(n-1)},')
            f.write(f'{(i-1)%(n-1)}\n')

    with open(file_path, 'a') as f:
        f.write(f'{n-1}:')
        for i in range(0, n-2):
            f.write(f'{i},')
        f.write(f'{n-2}\n')


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

def clear_file(n, q, folder_name):
    with open(f'{folder_name}/graph{n}-{q}.txt', 'w') as f:
        f.write('')

def write_answer(n, edges, answer, q, graph_num, folder_name):
    with open(f'{folder_name}/graph{n}-{q}.txt', 'a') as f:
        f.write(f'{graph_num}: {answer}\n')

def make_from_edge_list(edge_list):
    g = graph.Graph()
    for edge in edge_list.split('  '):
        u, v = edge.split(' ')
        g.add_edge(int(u), int(v))
        g.add_edge(int(v), int(u))

    return g