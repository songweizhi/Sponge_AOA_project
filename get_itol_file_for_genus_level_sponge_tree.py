
########################################################################################################################

color_code_sponge_txt   = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_sponge.txt'
tax_to_tax_lineage_txt  = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/tax_to_tax_lineage.txt'
tree_leaf_txt           = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_g_representatives_JL_wd/Sponge_phylogeny_Maria_topo_genus_level_leaves.txt'

########################################################################################################################

color_code_dict = dict()
for each_line in open(color_code_sponge_txt):
    each_line_split = each_line.strip().split('\t')
    color_code_dict[each_line_split[0]] = each_line_split[1]

tree_leaf_set = set()
for tree_leaf in open(tree_leaf_txt):
    tree_leaf_set.add(tree_leaf.strip())

tax_wanted_set = set()
for each_line in open(tax_to_tax_lineage_txt):
    each_line_split = each_line.strip().split('\t')
    tax_name = each_line_split[0]
    lineage_str = each_line_split[1]
    lineage_str_split = lineage_str.strip().split(';')

    if tax_name in tree_leaf_set:
        tax_c = ''
        tax_sc = ''
        tax_o = ''
        for each_r in lineage_str_split:
            if each_r.startswith('o__'):
                tax_o = each_r
            if each_r.startswith('sc__'):
                tax_sc = each_r
            if each_r.startswith('c__'):
                tax_c = each_r

        tax_wanted = tax_o
        if tax_c in ['c__Hexactinellida', 'c__Homoscleromorpha']:
            tax_wanted = tax_c
        # print(tax_name, tax_wanted, sep='\t')
        tax_wanted_set.add(tax_wanted)

for each_tax in tax_wanted_set:
    print('"%s"\t%s' % (color_code_dict.get(each_tax, ''), each_tax))


# tax_lineage_dict = dict()
# max_leaf_name_len = 0
# max_tax_len_dict = dict()
# for each_line in open(tax_to_tax_lineage_txt):
#     if (each_line.startswith('g__')) or (each_line.startswith('JL')):
#         each_line_split = each_line.strip().split('\t')
#         g_name = each_line_split[0]
#         lineage_str = each_line_split[1]
#         lineage_str_split = lineage_str.strip().split(';')
#
#         tax_lineage_dict[g_name] = lineage_str
#         if len(g_name) > max_leaf_name_len:
#             max_leaf_name_len = len(g_name)
#
#         for each_r in lineage_str_split:
#             rank_alphabet = each_r.split('__')[0]
#             if rank_alphabet not in max_tax_len_dict:
#                 max_tax_len_dict[rank_alphabet] = 0
#             if len(each_r) > max_tax_len_dict[rank_alphabet]:
#                 max_tax_len_dict[rank_alphabet] = len(each_r)
