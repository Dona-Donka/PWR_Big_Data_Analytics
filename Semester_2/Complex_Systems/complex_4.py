# based on: "Arkadiusz Jedrzejewski, Pair approximation fortheq-voter model with independence on complex networks, PRE 95, 012307 (2017)" article
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy


# initialize a q-voter graph with N nodes, probability p, q votes and concentrations c (0)
def initQVoterGraph(N,p,q,c):
    graph = nx.erdos_renyi_graph(N, p)
    zeroVotes = random.sample(range(N), int(c*N))
    for i in range(N):
        if i in zeroVotes:
            graph.add_node(i, vote =  0)
        else:
            graph.add_node(i, vote =  random.randint(1,q-1))
    return graph

# take a neighbour nodes, assign a random neighbor attribute, iterate by all nodes
def monteCarloStep(graph):
    for node in graph.nodes():
        graph.node[node]["vote"] = graph.node[random.choice([x[1] for x in graph.edges(node)])]["vote"]
    return graph

# get concentration c(0)
def computeZerosConcentrations(graph):
    voteList = []
    for node in graph.nodes():
        voteList.append(graph.nodes[node]["vote"])
    return numpy.mean(voteList)

def drawChart(concentration, steps):
    print("5000_02_2_02.jpg", concentration)
    plt.plot(steps, concentration, 'g-')
    axes = plt.gca()
    axes.set_ylim([0,1])
    plt.title("Sample trajectories of the up spins concentrations")
    plt.xlabel("Monte Carlo Steps")
    plt.ylabel("concentration")
    return plt.savefig('conc_q_6.jpg')

MCS = 50
concentration = []
steps = [x for x in range(MCS)]

for i in range(MCS): 
    print(i*2, "%")

    graph = monteCarloStep(initQVoterGraph(10000,0.2,6, 0.5))
    concentration.append(computeZerosConcentrations(graph))
drawChart(concentration, steps)
