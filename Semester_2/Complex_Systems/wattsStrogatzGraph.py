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






# Histogram of deg. distribution P(k)
plt.hist([ws.degree[x] for x in range(0,N)], bins='auto')
plt.savefig('PATH')


import statistics
# Distribution of clustering
print("Watts-Strogatz model: ", nx.clustering(ws))
clustering = [x for x in nx.clustering(ws).values()]
print("Average: ", statistics.mean(clustering))

# Distribution of the shortest path

pathLength =  dict(nx.all_pairs_shortest_path_length(ws))
for node in range(0,N):
    print("node: ", node, " Shortest paths: ", pathLength[1][node])
print("Average paths: ", statistics.mean([int(v) for v in pathLength[1].values()]))
print("Diameter: ", nx.diameter(ws))

############################################################################################

import networkx as nx
import matplotlib.pyplot as plt

averagePathList = []
averageClusteringCoeffc = []
dataList = [0.0001, 0.0005, 0.001, 0.0025, 0.005, 0.010, 0.025, 0.050, 0.1, 0.15, 0.25, 0.35, 0.5, 0.65, 0.85, 1]
for data in dataList:
    ws1 = nx.watts_strogatz_graph(1000, 8, data)
    averagePathList.append(nx.average_shortest_path_length(ws1))
    averageClusteringCoeffc.append(nx.average_clustering(ws1))

averagePathList1 = []
for item in averagePathList:
    averagePathList1.append(item/averagePathList[0])

averageClusteringCoeffc1 = []
for item in averageClusteringCoeffc:
    averageClusteringCoeffc1.append(item/averageClusteringCoeffc[0])

#p1 = plt.scatter(dataList, averageClusteringCoeffc1, color='seagreen')
#p2 = plt.scatter(dataList, averagePathList1, color='brown')

#plt.title("Increasing randomness")
#plt.xlabel("p")
#plt.legend((p1,p2),("<C[p]>/<C[0]>", "d[p]/d[0]"))
#plt.savefig(PATH)

import numpy as np

N = [5, 10, 20, 30, 50, 75, 100, 150, 200, 250, 500, 750, 1000, 1250]
averageDiameters = []
averagePaths = []
theoreticalResults = []

for data in N:
    ws2 = nx.watts_strogatz_graph(data, 4, 0.25)
    averagePaths.append(nx.average_shortest_path_length(ws2))
    averageDiameters.append(nx.diameter(ws2))
    theoreticalResults.append(np.log(data)/np.log(4))

p3 = plt.scatter(N, averagePaths, color='darkslategray')
p4 = plt.scatter(N, averageDiameters, color='midnightblue')
p5 = plt.scatter(N, theoreticalResults, color='black')
plt.xlabel("N")
plt.legend((p3,p4, p5),("Paths", "Diameters", "theoretical"))
plt.savefig(PATH)
