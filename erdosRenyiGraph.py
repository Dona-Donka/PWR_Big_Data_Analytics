# define Erdos and Renyi graph
# N labeled nodes are connected with L randomly placed links.
# EnR used this def. to their string of papers on random networks.
# G(N,p) fixes the prob that two nodes are connected, G(N, L)
#model fixes the total number od links L.

print("-- EnR RANDOM GRAPH --")

nodesTable = [x for x in range(0, N)]

def getNode(nodesTable, nodes):
    randomNode = random.choice(nodesTable)
    item = nodesTable.index(randomNode)
    nodesTable.pop(item)
    return randomNode

def getElemets(nodesTable, L):
    nodes = []
    for i in range(0, L):
        node = getNode(nodesTable, nodes)
        nodes.append(node)
    return nodes

def getEdge(EnR, nodes):
    nodesList = list(EnR.nodes())
    edge = getElemets(nodesList, 2)
    if edge not in nodes:
        print("edge: ", edge)
        return edge

def getEdges(EnR, N):
    edges = []
    for i in range(0, N):
        edges.append(getEdge(EnR, edges))
    return edges

L = 5
nodes = getElemets(nodesTable, L)
EnR = nx.Graph()
for i in range(0, N):
    EnR.add_node(i)
EnR.add_edges_from((getEdges(EnR, L)))


nx.draw_networkx(EnR, pos=nx.circular_layout(EnR))
#plt.show()
plt.savefig(PATH)
