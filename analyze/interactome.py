import pandas as pd
import numpy as np
import networkx as nx
import os

PATH = os.getcwd()
INTERACTOME_FILE = "/interactome/menche.tsv"

class Interactome(object):

    def __init__(self, filepath):
        self.ixns = pd.read_csv(filepath, sep="\t")
        self.G = nx.Graph()

        for _, ixn in self.ixns.iterrows():
            src = ixn["gene_ID_1"]
            dest = ixn["gene_ID_2"]
            self.G.add_node(src)
            self.G.add_node(dest)
            self.G.add_edge(src, dest)
    
    def filter(self, genes):
        return list(filter(self.G.has_node, genes))
    
    def subgraph(self, genes, filter=True):
        if filter:
            filtered_genes = self.filter(genes)
        filtered_genes = genes

        return self.G.subgraph(filtered_genes)