import networkx as nx
import random
import pytest

def find_impostor(edgelist, pseudocenters):
    # Create the graph from the edge list
    G = nx.Graph()
    G.add_edges_from(edgelist)
    
    ego_edges_count = {}
  
    for center in pseudocenters:
       
        ego_network = nx.ego_graph(G, center)
        
     
        ego_edges_count[center] = ego_network.number_of_edges()
    
    impostor = min(ego_edges_count, key=ego_edges_count.get)
    
    return impostor

def read_facebook_graph(filename):
    edges = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line into two integers representing an edge
            node1, node2 = map(int, line.strip().split())
            edges.append((node1, node2))
    return edges

if __name__ == "__main__":
    
    edges = read_facebook_graph('facebook_combined.txt')
    
    
    pseudocenters = [0, 107, 1684, 1912, 3437, 348, 612, 3980, 414, 686, 698]
    
    impostor = find_impostor(edges, pseudocenters)
    
    print("The impostor is:", impostor)


centers = [0, 107, 1684, 1912, 3437, 348, 3980, 414, 686, 698]
pseudocenters = [0, 107, 1684, 1912, 3437, 348, 612, 3980, 414, 686, 698]
real_impostor = 612

edges = read_facebook_graph('facebook_combined.txt')

@pytest.mark.parametrize('execution_number', range(6))
def test_impostor(execution_number):
    # Shuffle the vertices and test if the impostor is correctly found
    vertices = list(range(0, 4039))
    random.shuffle(vertices)
    newedges = list(map(lambda uv: (vertices[uv[0]], vertices[uv[1]]), edges))
    newpseudocenters = list(map(lambda u: vertices[u], pseudocenters))
    newimp = find_impostor(newedges, newpseudocenters)
    print(str(newimp) + " " + str(vertices[real_impostor]))
    assert newimp == vertices[real_impostor]
