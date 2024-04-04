import numpy as np
import random

def generate_random_graph(num_vertices, edge_density=0.5, max_weight=10):
    """
    Generates a random graph with weights and returns its adjacency matrix.
    
    Parameters:
    - num_vertices: Number of vertices in the graph.
    - edge_density: Probability of an edge existing between two vertices.
    - max_weight: Maximum weight of an edge.
    
    Returns:
    - A numpy array representing the weighted adjacency matrix of the graph.
    """
    graph = np.full((num_vertices, num_vertices), float('inf'))
    np.fill_diagonal(graph, 0)
    
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if random.random() < edge_density:
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
                
    return graph

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = graph.copy()
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

def print_graph(graph):
    print("Generated Graph (Adjacency Matrix):")
    for row in graph:
        print(["∞" if x == float('inf') else int(x) for x in row])

def print_shortest_paths(dist):
    print("\nShortest Paths Between All Pairs of Vertices:")
    for i, row in enumerate(dist):
        for j, val in enumerate(row):
            print(f"Shortest distance from vertex {i} to vertex {j}: {'∞' if val == float('inf') else int(val)}")

# User Input
num_vertices = int(input("Enter the number of vertices: "))
edge_density = float(input("Enter the edge density (0 to 1): "))
max_weight = int(input("Enter the maximum weight of edges: "))

# Generate graph and compute shortest paths
graph = generate_random_graph(num_vertices, edge_density, max_weight)
print_graph(graph)

shortest_paths = floyd_warshall(graph)
print_shortest_paths(shortest_paths)
