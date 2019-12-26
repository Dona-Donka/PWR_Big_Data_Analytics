# based on: "Arkadiusz Jedrzejewski, Pair approximation fortheq-voter model with independence on complex networks, PRE 95, 012307 (2017)" article
import networkx as nx
import matplotlib.pyplot as plt
import random, numpy


# initialize a q-voter graph with N nodes, probability p, q votes and concentrations c (0)
def initQVoterGraph(N,p,c):
    graph = nx.erdos_renyi_graph(N, p)
    for i in range(N):
        randomNumber = random.randint(0, 100) * 0.01
        if randomNumber <= c:
            graph.add_node(i, vote=1)
        else:
            graph.add_node(i, vote=0)
    return graph

def monteCarloStep(graph, q):
    for myNode in graph.nodes():
        voteList = []
        for n in range(q):
            voteList.append(graph.node[random.choice([x[1] for x in graph.edges(myNode)])]["vote"])
        print(voteList)
        if (len(set(voteList))==1):
            graph.node[myNode]["vote"] = int(voteList[0])
    return graph

# get concentration c(0)
def computeZerosConcentrations(graph):
    voteList = []
    for node in graph.nodes():
        voteList.append(graph.nodes[node]["vote"])
    return numpy.mean(voteList)

def drawChart(concentration, steps):
    plt.plot(steps, concentration, 'ro')
    plt.title("Sample trajectories of the up spins concentrations")
    plt.xlabel("Monte Carlo Steps")
    plt.ylabel("concentration")
    return plt.savefig(PATH)

MCS = 10000
concentration = []
steps = [x for x in range(MCS)]

for i in range(MCS):
    graph = monteCarloStep(initQVoterGraph(100,0.2,2, 0.6))
    concentration.append(computeZerosConcentrations(graph))
drawChart(concentration, steps)
