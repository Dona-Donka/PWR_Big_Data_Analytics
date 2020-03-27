import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.legend as ax
import random
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def connectedComponentsList(graph, nodeList, size):
    list = []
    giant = sorted(nx.connected_components(graph), key=len, reverse=True)
    g0 = (graph.subgraph(giant[0])).size()
    for r in range(1,100):

        graph.remove_nodes_from(nodeList[:int((10 ** size) * 0.01)])
        nodeList = nodeList[int((10 ** size) * 0.01):]
        giant1 = sorted(nx.connected_components(graph), key=len, reverse=True)
        g1_0 = (graph.subgraph(giant1[0])).size()
        list.append(g1_0/g0)
    return list

def computeMean(list):
    return np.mean(list, axis=0)

def computeComponent(size):
    randomCompMean = []
    degreeCompMean = []
    closenessCompMean = []
    betweennessCompMean = []

    for r in range(1,2):
        print("step: ", r)
        graph = nx.erdos_renyi_graph(1000, 0.1)
        graph1 = graph.copy()
        graph2 = graph.copy()
        graph3 = graph.copy()

        # Remove high-degree nodes,  create a list of conneted_components lenght (attack)
        listDegree = [x[0] for x in sorted(dict(graph.degree()).items(), reverse=True, key=lambda x: x[1])]
        degreeCompMean.append(connectedComponentsList(graph, listDegree,size))
        print("degree")

        # Remove random sample nodes, create a list of connected_components lenght
        listRandomNodes = random.sample(graph1.nodes(), len(graph1.nodes()))
        randomCompMean.append(connectedComponentsList(graph1, listRandomNodes,size))
        print("random")
        # Remove high closeness_centrality nodes, create a list of connected_components lenght
        listClosenessCentrality = [x[0] for x in sorted(dict(nx.closeness_centrality(graph2)).items(), reverse=True, key=lambda x: x[1])]
        closenessCompMean.append(connectedComponentsList(graph2, listClosenessCentrality,size))
       # Remove high betweeness_centrality nodes, create a list of connected_components lenght
        listBetweennessCentrality = [x[0] for x in sorted(dict(nx.betweenness_centrality(graph3)).items(), reverse=True, key=lambda x: x[1])]
        betweennessCompMean.append(connectedComponentsList(graph3, listBetweennessCentrality,size))
        #print("bet")
    degreeCompMean = computeMean(degreeCompMean)
    randomCompMean = computeMean(randomCompMean)
    closenessCompMean = computeMean(closenessCompMean)
    betweennessCompMean = computeMean(betweennessCompMean)

    # plotting:
    x = [x*0.01 for x in range(1,100)]
    print("x: ", x)
    degree, = plt.plot(x, degreeCompMean, label = "degree (attack)", color='b')
    randoms, = plt.plot(x, randomCompMean, label = "random", color='y')
    closeness, =   plt.plot(x, closenessCompMean, label = "closeness", color = 'g')
    betweeness = plt.plot(x, betweennessCompMean, label = "betweenness", color = 'r')

    # drawing legend and titles:
    legend = plt.legend(bbox_to_anchor=(0.96, 0.94), loc = "upper right", borderaxespad=0.)
    plt.gca().add_artist(legend)
    #plt.title("Robustness of networks" + "\n" + "Watts, N = 1000, k = 8")
    plt.xlabel("Removed nodes")
    plt.ylabel("connected components coefficient")
    plt.savefig("ER_robustness1.jpg")

 

computeComponent(3)
