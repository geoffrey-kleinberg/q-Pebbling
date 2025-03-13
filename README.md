# $q$-Pebbling

This repository contains code for calculating the $q$-pebbling number of a graph, as well as computed information about Class $0_q$ graphs.

## Calculate the $q$-Pebbling Number of a Specific Graph

First, create a file containing the adjacency data of the graph in the following format:

```
a:b,c
b:a,c
c:a,b
```

List a vertex followed by a colon, followed by a comma-separated list of its neighbors. Note that a vertex can have any name and they can be listed in any order. Directed graphs are not supported, as a line such as `a:b` will add an edge from `a` to `b` and from `b` to `a`.

Use the following code to calculate the $q$-pebbling number of this graph, where `graph.txt` is the file containing the adjacency data. Optional arguments to `pebbling_number` include `q`, the diameter `d` (will be calculated if not provided), and `cap` which is the maximum value for the $q$-pebbling number that will be checked.

```python
g = graph.Graph.make_from_file('graph.txt')
print(pebbling_number(g, q=q))
```

You can also create a graph from an adjaceny matrix:

```python
g = graph.Graph.make_from_adjacency_matrix(matrix)
print(pebbling_number(g, q=q))
```

## Find the $q$-Pebbling Number of Many Graphs

The `all_graphs` directory contains every connected graph on 3 to 9 vertices. These files can be found on [this page](https://users.cecs.anu.edu.au/~bdm/data/graphs.html). Graph data is stored in g6 format. Information on how to read a graph stored in g6 format is found [here](https://users.cecs.anu.edu.au/~bdm/data/formats.html). For the code in this repo, download the executable corresponding to your machine and place it in this repo's directory. For further information on the g6 format, see [this page](https://users.cecs.anu.edu.au/~bdm/data/formats.txt).

Several functions are already included. Using `all_graphs.py`, you can calculate the $q$-pebbling number of all graphs of order $n$. For most cases, this will take an extraordinarily long time to run. To find the $q$-pebbling number of all graphs on $n$ vertices of diameter 2, use `diameter2_all.py`. To find all Class $0_q$ graphs on $n$ vertices, use `find_all_class0.py`. 

Each of these programs will save the output to a file in a corresponding directory. Results are written in the following format:
```
graph_num: pebbling_num
```
The file will also include the total number of graphs evaluated with the `pebbling_number` function as the last line.