import networkx as nx
import random
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# task04 facebook:
path = "facebook_combined.txt"
fb = nx.read_edgelist(path, nodetype=int, create_using=nx.Graph())
N = [x for x in fb.nodes()]
plt.title("Histogram of degree distributions \n facebook")
plt.xlabel("degree P(k)")
plt.ylabel("Number of edges")
plt.hist([fb.degree[x] for x in N], bins='auto')
plt.savefig('fb_histogram.png')



import statistics
# Distribution of clustering
print("facebook model (clust): ", nx.clustering(fb))
clustering = [x for x in nx.clustering(fb).values()]
print("Average: ", statistics.mean(clustering))

# Distribution of the shortest path

pathLength =  dict(nx.all_pairs_shortest_path_length(fb))
for node in range(0,N):
    print("node: ", node, " Shortest paths: ", pathLength[1][node])
print("Average paths: ", statistics.mean([int(v) for v in pathLength[1].values()]))
print("Diameter: ", nx.diameter(fb))
