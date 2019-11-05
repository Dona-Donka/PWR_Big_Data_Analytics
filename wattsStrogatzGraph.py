import networkx as nx
import matplotlib.pyplot as plt
import random

N = 10
k = 4
p = 0.6


def getRandom():
    return random.uniform(0.0, 1.0)

nodes = [x for x in range(0,N)]
ws = nx.Graph()
for i in range(0, N):
    ws.add_node(i)


for j in range(1, k // 2 + 1):
    targets = nodes[j:] + nodes[0:j]  # first j nodes are now last in list
    ws.add_edges_from(zip(nodes, targets))

edgesToDelete = []
for i  in ws.edges():
    randomParam = getRandom()
    if randomParam <= p:
        edgesToDelete.append(i)

for i in edgesToDelete:
    ws.remove_edge(*i)

position = nx.circular_layout(ws)
nx.draw_networkx(ws, position, width=3, edge_color="r", alpha=0.6)
plt.savefig('PATH')
