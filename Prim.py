# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:15:00 2023

@author: Gadiel Jimenez
"""
import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Arista \tPeso")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def primMST(self):
        key = [float("inf")] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for _ in range(self.V - 1):
            min_key = float("inf")
            for v in range(self.V):
                if not mstSet[v] and key[v] < min_key:
                    min_key = key[v]
                    min_index = v

            mstSet[min_index] = True

            for v in range(self.V):
                if self.graph[min_index][v] > 0 and not mstSet[v] and key[v] > self.graph[min_index][v]:
                    key[v] = self.graph[min_index][v]
                    parent[v] = min_index

        self.printMST(parent)

# Crea un grafo aleatorio de 6 vertices
V = 6
graph = Graph(V)
for i in range(V):
    for j in range(i + 1, V):
        if random.randint(0, 1) == 1:
            weight = random.randint(1, 10)
            graph.graph[i][j] = weight
            graph.graph[j][i] = weight

graph.primMST()
