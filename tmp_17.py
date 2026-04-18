import os
import argparse
from ete3 import Tree


leaf_taxonomy_txt                   = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/tax_to_tax_lineage.txt'
maria_topo_genus_level_sponge_tree  = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_g_representatives_JL_wd/Sponge_phylogeny_Maria_topo_genus_level.tree'
rank_to_plot_str                    = 'c,sc,o'
rank_to_plot_str                    = 'o'
op_leaf_grp_txt                     = '/Users/songweizhi/Desktop/leaf_grp.txt'
rename_leaf_txt                     = '/Users/songweizhi/Desktop/rename_leaf.txt'

rank_to_plot_list = rank_to_plot_str.split(',')

tax_lineage_dict = dict()
for each_line in open(leaf_taxonomy_txt):
    each_line_split = each_line.strip().split('\t')
    tax_lineage_dict[each_line_split[0]] = each_line_split[1]

sponge_tre = Tree(maria_topo_genus_level_sponge_tree, quoted_node_names=True, format=0)
sponge_tre_leaves = [i.name for i in sponge_tre.get_leaves()]

rename_leaf_txt_handle = open(rename_leaf_txt, 'w')
op_leaf_grp_txt_handle = open(op_leaf_grp_txt, 'w')
for leaf in sponge_tre_leaves:
    leaf_tax = tax_lineage_dict[leaf]
    leaf_tax_split = leaf_tax.split(';')
    value_to_write = []
    for each_rank in rank_to_plot_list:
        current = '%s__' % each_rank
        for each_r in leaf_tax_split:
            each_r_level = each_r.split('__')[0]
            if each_r_level == each_rank:
                value_to_write.append(each_r)
    print(value_to_write)

    str_to_write = '%s\t%s' % (leaf, ';'.join(value_to_write))
    str_to_write2 = '%s\t%s__%s' % (leaf, ';'.join(value_to_write), leaf)
    rename_leaf_txt_handle.write(str_to_write2 + '\n')
    op_leaf_grp_txt_handle.write(str_to_write + '\n')

rename_leaf_txt_handle.close()
op_leaf_grp_txt_handle.close()
