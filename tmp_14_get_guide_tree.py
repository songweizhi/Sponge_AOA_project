from ete3 import Tree

########################################################################################################################

dbscc_genomes_txt   = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/DBSCC_genomes.txt'
meta_data_txt       = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/metadata_614.txt'
gnm_id_txt          = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/gnm_id_406.txt'
gnm_id_txt          = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/gnm_id_611.txt'
tree_in_txt         = '/Users/songweizhi/Desktop/Sponge_r220/9_the_big_tree/guide_tree_genus_level.treefile'
tree_out_txt        = '/Users/songweizhi/Desktop/guide_tree_genome_level_611.txt'

########################################################################################################################

gnm_to_dbscc_dict = dict()
for each in open(dbscc_genomes_txt):
    each_split = each.strip().split('\t')
    gnm_to_dbscc_dict[each_split[0]] = each_split[1]

gnm_to_genus_dict = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        gnm_taxon = each_gnm_split[col_index['Taxon']]
        gnm_taxon_split = gnm_taxon.split(';')
        gnm_genus = gnm_taxon_split[5]
        gnm_to_genus_dict[gnm_id] = gnm_genus

group_to_member_dict = dict()
for each in open(gnm_id_txt):
    gnm_id = each.strip()
    gnm_grp = ''
    if gnm_id in gnm_to_dbscc_dict:
        gnm_grp = gnm_to_dbscc_dict[gnm_id]
    else:
        gnm_grp = gnm_to_genus_dict[gnm_id]
    if gnm_grp not in group_to_member_dict:
        group_to_member_dict[gnm_grp] = set()
    group_to_member_dict[gnm_grp].add(gnm_id)

t = Tree(tree_in_txt, format=0)
for leaf in t:
    leaf_name = leaf.name
    if leaf_name in group_to_member_dict:
        leaf_member = group_to_member_dict[leaf_name]
        leaf_member_str = ','.join(leaf_member)
        if len(leaf_member) >= 2:
            leaf_member_str = '(' + leaf_member_str + ')'
        if len(leaf_member) == 1:
            leaf.name = leaf_member_str
        else:
            leaf_p = leaf.up
            leaf_p.add_child(Tree((leaf_member_str + ';'), format=0))
            leaf_p.remove_child(leaf)
t.write(outfile=tree_out_txt, format=9)
