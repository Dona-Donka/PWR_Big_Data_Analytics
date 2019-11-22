import networkx as nx
import matplotlib.pyplot as plt
import random

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

size = 3
def computeComponent(graph, size):
    components = []
    components1 = []
    graph1 = graph.copy()
    list = [x[0] for x in sorted(dict(graph.degree()).items(), reverse=True, key=lambda x: x[1])]

    for r in range(1,100):
        graph.remove_nodes_from(list[:int((10**size)*0.01)])
        list = list[int((10**size)*0.01):]
        components1.append(len(max(nx.connected_components(graph))))

        graph1.remove_nodes_from(random.sample(graph1.nodes(), int((10**size)*0.01)))
        components.append(len(max(nx.connected_components(graph1))))

    x = [x*0.01 for x in range(1,100)]
    plt.plot(x, [x/10**size for x in components1], 'b-',
             x, [x/10**size for x in components], 'r-')

    plt.title("Robustness of networks")
    plt.xlabel("Removed nodes")
    plt.ylabel("connected components coefficient")
    plt.savefig(PATH)


ws = nx.watts_strogatz_graph(10 ** size, 4, 0.01)
ba = nx.barabasi_albert_graph(10**size, 2)
er = nx.erdos_renyi_graph(10**size, 2)

computeComponent(ws,3)
