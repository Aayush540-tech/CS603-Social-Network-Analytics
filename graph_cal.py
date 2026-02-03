import networkx as nx
import matplotlib.pyplot as plt

# 1. Setup Data
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)]

# Create Graphs
G_undirected = nx.Graph()
G_undirected.add_nodes_from(nodes)
G_undirected.add_edges_from(edges)

G_directed = nx.DiGraph()
G_directed.add_nodes_from(nodes)
G_directed.add_edges_from(edges)

# 2. Visualization
plt.figure(figsize=(12, 5))

# Plot Undirected
plt.subplot(121)
plt.title("Undirected Graph")
nx.draw(G_undirected, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')

# Plot Directed
plt.subplot(122)
plt.title("Directed Graph")
nx.draw(G_directed, with_labels=True, node_color='lightcoral', node_size=800, font_weight='bold', arrowsize=20)

plt.show()

# 3. Cardinality Calculations
def print_graph_stats(G, name, is_directed=False):
    print(f"--- {name} ---")
    print(f"Graph Cardinality: |V| = {G.number_of_nodes()}, |E| = {G.number_of_edges()}")
    
    if not is_directed:
        print("Node Cardinality (Degree):")
        for node, deg in G.degree():
            print(f"  Node {node}: {deg}")
    else:
        print("Node Cardinality (In-Degree / Out-Degree):")
        for node in G.nodes():
            in_deg = G.in_degree(node)
            out_deg = G.out_degree(node)
            print(f"  Node {node}: In={in_deg}, Out={out_deg}")
    print("\n")

print_graph_stats(G_undirected, "Undirected Graph")
print_graph_stats(G_directed, "Directed Graph", is_directed=True)