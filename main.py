import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

G = nx.read_gml("football/football.gml")

nx.draw(G, with_labels=True, font_weight='bold', width=1)
plt.show()
plt.savefig("grafo.png")