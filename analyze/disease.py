import os
import networkx as nx
import matplotlib.pyplot as plt

class Disease(object):
    def __init__(self, disease_file, ixome):
        """
        disease_file: string
        ixome: Interactome
        """
        # Get all the genes associated with a disease
        PATH = os.getcwd()
        self.genes = set()
        with open(PATH + f"/disease-genes/{disease_file}.txt") as f:
            for line in f:
                self.genes.add(int(line.strip()))
        
        # Filter those genes by the ones that are in the interactome
        self.subgraph = ixome.subgraph(self.genes, filter=True)
        self.ixome_genes = set(self.subgraph.nodes)
    
    def show_disease_graph(self, tissue):
        """
        tissue: Tissue
        """
        genes_in_tissue = list(filter(tissue.subgraph.has_node, self.ixome_genes))
        plt.figure(figsize=(12, 12))
        nx.draw_networkx_nodes(tissue.subgraph, tissue.pos,
                               label="Tissue Genes",
                               node_color="r", node_size=3, alpha=0.5)
        nx.draw_networkx_nodes(tissue.subgraph, tissue.pos,
                               label="Disease Genes",
                               nodelist=genes_in_tissue,
                               node_color="b", alpha=1.0, node_size=12)
        nx.draw_networkx_labels(tissue.subgraph, tissue.pos,
                               labels={n:n for n in genes_in_tissue})
        nx.draw_networkx_edges(tissue.subgraph, tissue.pos,
                               width=1.0, alpha=0.3)
        plt.legend()
        plt.show()
