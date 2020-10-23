import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

G = nx.read_gml("lesmis.gml")

matrix_dist = nx.floyd_warshall_numpy(G)

minimo = []
maximo = []
somatorio = []
menor = 99999
maior = 0
soma = 0

for i in range(0, (G.number_of_nodes())):
	for j in range(0, (G.number_of_nodes()-1)):
		if(matrix_dist[i][j] < menor and i != j):
			menor = matrix_dist[i][j]
		if(matrix_dist[i][j] > maior):
			maior = matrix_dist[i][j]
		soma = soma + matrix_dist[i][j]
	somatorio.append(soma)
	minimo.append(menor)
	maximo.append(maior)
	soma = 0
	menor = 999999
	maior = 0

print(maximo)
print(minimo)
print(somatorio)