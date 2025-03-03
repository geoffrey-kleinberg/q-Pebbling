# $q$-Pebbling

This repository contains code for calculating the $q$-pebbling number of a graph, as well as computed information about Class $0_q$ graphs.

## Calculate the Pebbling Number of a Specific Graph

First, create a file containing the adjacency data of the graph in the following format:

```
a:b,c
b:a,c
c:a,b
```

List a vertex followed by a colon, followed by a comma-separated list of its neighbors. Note that a vertex can have any name and they can be listed in any order. Directed graphs are not supported, as a line
such as `a:b` will add an edge from `a` to `b` and from `b` to `a`.
