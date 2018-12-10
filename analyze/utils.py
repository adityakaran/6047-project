import pandas as pd
import os
import mygene

def tissue_gtex_to_entrez(filename):
    mapping = pd.read_csv("./gene-map/ensembl_to_ncbi.txt", sep="\t")
    ensembl_to_ncbi = {}
    for _, row in mapping.iterrows():
        ensembl_to_ncbi[row["Gene stable ID"]] = row["NCBI gene ID"]
    PATH = os.getcwd()
    genes = pd.read_csv(f"{PATH}/{filename}", sep="\t")["gene_id"]
    genes = set(map(lambda x: x.split(".")[0], genes))
    tissue_genes = []
    for gene in genes:
        try:
            tissue_genes.append(str(int(ensembl_to_ncbi[gene])))
        except:
            pass
    return tissue_genes
