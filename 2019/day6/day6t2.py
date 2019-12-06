import networkx as nx
graph = nx.DiGraph()
for data in open("input.txt").readlines():
    graph.add_edge(*[x.strip() for x in data.split(')')])
print(nx.transitive_closure(graph).size())
print(nx.shortest_path_length(graph.to_undirected(), "YOU", "SAN")-2)
