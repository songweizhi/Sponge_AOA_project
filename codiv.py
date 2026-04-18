import pickle
from skbio.stats.evolve import hommola_cospeciation
import skbio as skb
import numpy as np
import pandas as pd
from skbio import TreeNode
from io import StringIO
from Bio import AlignIO


def rn_fn(x):
    return(x.replace(' ','_').replace('.','_').replace('-','_'))


########################################################################################################################

sponge_tree         = '/Users/songweizhi/Desktop/Sponge_r226/08_Host_specificity/codiv_data/Host_Tree.nwk'
aoa_tree            = '/Users/songweizhi/Desktop/Sponge_r226/08_Host_specificity/codiv_data/Symbiont_Tree.treefile'
sponge_to_aoa_table = '/Users/songweizhi/Desktop/Sponge_r226/08_Host_specificity/codiv_data/Host_to_Symbiont.txt'

########################################################################################################################

# Load up host tree
host_tree_fp = '../data/listofhostspecies-fixed.nwk'
host_tree_fp = sponge_tree
host_tree = TreeNode.read(host_tree_fp)
for tip in host_tree.tips():
    tip.name = rn_fn(tip.name)

# Load bacterial tree
bact_tree_fp = '../data/gtdbtk.bac120.user_msa.fasta.treefile'
bact_tree_fp = aoa_tree
bact_tree = TreeNode.read(bact_tree_fp)
bact_tree.assign_ids()
for tip in bact_tree.tips():
    tip.name = rn_fn(tip.name)

# Define interactions
mags_table_fp = '../data/Metadata_12_29_2021.xlsx'
mags_table_df = pd.read_excel(mags_table_fp)




















