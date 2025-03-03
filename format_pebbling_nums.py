def format_n_q(n, q):
    raw_data = []
    with open(f'pebbling_nums/graph{n}-{q}.txt', 'r') as f:
        raw_data = f.readlines()

    nice_data = {}
    for line in raw_data:
        split_line = line.split(' ')
        edges = int(split_line[2])
        answer = int(split_line[3])
        if edges not in nice_data:
            nice_data[edges] = [answer, answer]

        if answer < nice_data[edges][0]:
            nice_data[edges][0] = answer

        if answer > nice_data[edges][1]:
            nice_data[edges][1] = answer

    print(nice_data)

    out_file = f'formatted/graph{n}-{q}.txt'
    min_edges = int(n - 1)
    max_edges = int(n * (n - 1) / 2)

    with open(out_file, 'w') as f:
        for e in range(min_edges, max_edges + 1):
            if e not in nice_data:
                f.write(f'{e},-1,-1\n')
            else:
                f.write(f'{e},{nice_data[e][0]},{nice_data[e][1]}\n')


if __name__ == '__main__':
    q = 2

    for n in range(3, 9):
        format_n_q(n, q)