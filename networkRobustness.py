import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.legend as ax
import random
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

size = 3

def connectedComponentsList(graph, nodeList):
    list = []
    for r in range(1,100):
        graph.remove_nodes_from(nodeList[:int((10 ** size) * 0.01)])
        nodeList = nodeList[int((10 ** size) * 0.01):]
        list.append(len(max(nx.connected_components(graph))))
    return list

def computeMean(list):
    return np.mean(list, axis=0)

def computeComponent(size):
    randomCompMean = []
    degreeCompMean = []
    closenessCompMean = []
    betweennessCompMean = []

    for r in range(1,250):
        graph = nx.watts_strogatz_graph(10 ** size, 4, 0.01)
        graph1 = graph.copy()
        graph2 = graph.copy()
        graph3 = graph.copy()

        # Remove high-degree nodes,  create a list of conneted_components lenght (attack)
        listDegree = [x[0] for x in sorted(dict(graph.degree()).items(), reverse=True, key=lambda x: x[1])]
        degreeCompMean.append(connectedComponentsList(graph, listDegree))
        
        # Remove random sample nodes, create a list of connected_components lenght
        listRandomNodes = random.sample(graph1.nodes(), len(graph1.nodes()))
        randomCompMean.append(connectedComponentsList(graph1, listRandomNodes))

        # Remove high closeness_centrality nodes, create a list of connected_components lenght
        listClosenessCentrality = [x[0] for x in sorted(dict(nx.closeness_centrality(graph)).items(), reverse=True, key=lambda x: x[1])]
        closenessCompMean.append(connectedComponentsList(graph2, listClosenessCentrality))

        # Remove high betweeness_centrality nodes, create a list of connected_components lenght
        listBetweennessCentrality = [x[0] for x in sorted(dict(nx.betweenness_centrality(graph)).items(), reverse=True, key=lambda x: x[1])]
        betweennessCompMean.append(connectedComponentsList(graph3, listBetweennessCentrality))

    degreeCompMean = computeMean(degreeCompMean)
    randomCompMean = computeMean(randomCompMean)
    closenessCompMean = computeMean(closenessCompMean)
    betweennessCompMean = computeMean(betweennessCompMean)

    # plotting:
    x = [x*0.01 for x in range(1,100)]
    degree, = plt.plot(x, [x/10**size for x in degreeCompMean], label = "degree (attack)")
    randoms, = plt.plot(x, [x/10**size for x in randomCompMean], label = "random")
    closeness, =   plt.plot(x, [x/10**size for x in closenessCompMean], label = "closeness")
    betweeness = plt.plot(x, [x/10**size for x in betweennessCompMean], label = "betweeness")

    # drawing legend and titles:
    legend = plt.legend(bbox_to_anchor=(0.96, 0.94), loc = "upper right", borderaxespad=0.)
    plt.gca().add_artist(legend)
    plt.title("Robustness of networks" + "\n" + "Watts-Strogatz, N = 1000, k = 4, p = 0.01")
    plt.xlabel("Removed nodes")
    plt.ylabel("connected components coefficient")
    plt.savefig("/home/dona/Pulpit/complexy_3.jpg")


ws = nx.watts_strogatz_graph(10 ** size, 4, 0.01)
ba = nx.barabasi_albert_graph(10**size, 2)
er = nx.erdos_renyi_graph(10**size, 2)

computeComponent(3)
