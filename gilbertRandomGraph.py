import networkx as nx
import random
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# number of nodes
N = 10
p = 0.45

# define a Gilbert random graph G(N,p)
# Each pair of N labeled nodes is connected with probability p

def getRandom():
        return random.uniform(0.0, 1.0)

def predictEdges(p,N):
        return(p*N*(N-1))/2

pE = predictEdges(p, N)

print("-- GILBERT RANDOM GRAPH --")
print("nodes 'N': ", N, "\n"
        "probability 'p': ", p, "\n"
        "predicted number of edges: ", pE)

# drawing a graph
gilbert = nx.Graph()
for i in range(1, N):
        gilbert.add_node(i)

totalEsges = 0

for i in range(0, N):
    for j in range(i,N):
        randomParam = getRandom()
        if randomParam < p and i != j:
            gilbert.add_edge(i, j)
            print("new edge: ", i, j)
            totalEsges+=1

print("Total edges: ", totalEsges)

nx.draw_networkx(gilbert, pos=nx.circular_layout(gilbert))
#plt.show()
plt.savefig(PATH)
