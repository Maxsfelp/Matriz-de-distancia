import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

G = nx.read_gml("football/football.gml")

matrix_dist = nx.floyd_warshall_numpy(G)

pd.DataFrame(matrix_dist).to_csv("matrix.csv", header=None, index=None)

nx.draw(G, with_labels=True, font_weight='bold', width=1)
plt.savefig("grafo.png", dpi=100)
plt.show()