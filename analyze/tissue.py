import os
import networkx as nx

class Tissue():
    def __init__(self, tissue_file, ixome):
        PATH = os.getcwd()
        self.genes = []
        with open(PATH + f"/tissue-genes-and-snps/{tissue_file}.txt") as f:
            for line in f:
                self.genes.append(int(line.strip()))

        self.subgraph = ixome.subgraph(self.genes, filter=True)
        self.pos = nx.spring_layout(self.subgraph)
