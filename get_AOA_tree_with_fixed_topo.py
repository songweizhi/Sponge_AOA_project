from ete3 import Tree

########################################################################################################################

#file in
meta_data_txt       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260408.txt'
gnm_id_txt          = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/gnm_id_2279.txt'
topo_tree_file      = '/Users/songweizhi/Desktop/Sponge_r226/06_AOA_tree/dRep85_256_freeliving_132_plus_DBSCCs_topo1.tre'
gap_stats_txt       = '/Users/songweizhi/Desktop/gtdbtk.ar53.user_msa.gap_stats.txt'
outgroup_txt        = '/Users/songweizhi/Desktop/outgroup.txt'

# file out
op_guide_tree_txt   = '/Users/songweizhi/Desktop/guide_tree_genome_2263.tree'
op_dir              = '/Users/songweizhi/Desktop/op_dir'

########################################################################################################################

def rm_leaf(main_tre, leaves_to_remove_list):

    main_tre_leaves = [i.name for i in main_tre.get_leaves()]
    leaves_to_keep = []
    for each_leaf in main_tre_leaves:
        if each_leaf not in leaves_to_remove_list:
            leaves_to_keep.append(each_leaf)
    main_tre.prune(leaves_to_keep)

    return main_tre


gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

topo_tree = Tree(topo_tree_file, quoted_node_names=True, format=0)
topo_tree_leaves = [i.name for i in topo_tree.get_leaves()]

group_to_member_dict = dict()
for i in topo_tree_leaves:
    if i != 'nonAOA_taxa':
        group_to_member_dict[i] = set()

n = 1
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        gnm_taxon = each_gnm_split[col_index['GTDB_Taxon_r226']]
        gnm_dbscc = each_gnm_split[col_index['DBSCC']]
        gnm_taxon_split = gnm_taxon.split(';')
        gnm_genus = gnm_taxon_split[5]
        if gnm_id in gnm_id_set:
            if (gnm_dbscc != 'na') and (gnm_dbscc in topo_tree_leaves):
                group_to_member_dict[gnm_dbscc].add(gnm_id)
            else:
                current_grp = ''
                for j in gnm_taxon_split:
                    if j in topo_tree_leaves:
                        current_grp = j
                if current_grp != '':
                    group_to_member_dict[current_grp].add(gnm_id)
                else:
                    # print(n, gnm_id, gnm_taxon, sep='\t')
                    # print('rm %s.fna' % gnm_id)
                    pass
                    n += 1

# remove the nonAOA_taxa leaf from topo tree
if 'nonAOA_taxa' in topo_tree_leaves:
    topo_tree = rm_leaf(topo_tree, ['nonAOA_taxa'])

# replace topo tree leaves with genome ids
for leaf in topo_tree:
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

# write out tree
topo_tree.write(outfile=op_guide_tree_txt, format=9)

gap_dict = dict()
for each_gnm in open(gap_stats_txt):
    if not each_gnm.startswith('Sequence\tGap'):
        each_gnm_split = each_gnm.strip().split('\t')
        gap_dict[each_gnm_split[0]] = float(each_gnm_split[1])

grp_min_gap_gnm_dict = dict()
for each_grp in group_to_member_dict:
    grp_member_set = group_to_member_dict[each_grp]
    current_grp_min_gap = 100
    current_grp_min_gap_gnm = ''
    for grp_member in grp_member_set:
        member_gap = gap_dict[grp_member]
        if member_gap < current_grp_min_gap:
            current_grp_min_gap = member_gap
            current_grp_min_gap_gnm = grp_member
    grp_min_gap_gnm_dict[each_grp] = current_grp_min_gap_gnm

outgroup_dict = dict()
for each_line in open(outgroup_txt):
    each_line_split = each_line.strip().split('\t')
    outgroup_dict[each_line_split[0]] = each_line_split[1]

for each_grp in group_to_member_dict:
    grp_member_set = group_to_member_dict[each_grp]
    grp_outgroup = outgroup_dict[each_grp]
    grp_outgroup_gnm = grp_min_gap_gnm_dict[grp_outgroup]
    grp_member_set_with_og_gnm = grp_member_set.copy()
    grp_member_set_with_og_gnm.add(grp_outgroup_gnm)

    if len(grp_member_set) > 2:
        gnm_id_txt_with_og_gnm = '%s/%s_with_outgroup.txt' % (op_dir, each_grp)
        gnm_id_txt_with_og_gnm_handle = open(gnm_id_txt_with_og_gnm, 'w')
        gnm_id_txt_with_og_gnm_handle.write('%s\n' % '\n'.join(grp_member_set_with_og_gnm))
        gnm_id_txt_with_og_gnm_handle.close()

        # subseu MSA
        subset_msa_cmd = 'BioSAK select_seq -i gtdbtk.ar53.user_msa_chi2p30.fasta -id %s_with_outgroup.txt -o %s_with_outgroup.aln' % (each_grp, each_grp)

        iqtree_cmd = 'BioSAK hpc4 -q amd -a marmolecol -wt 23:59:59 -t 36 -conda mybase2 -n PMSF_%s -c "TreeSAK PMSF -i %s_with_outgroup.aln -o %s_PMSF_tree_wd -t 36"' % (each_grp, each_grp, each_grp)

        root_tree_cmd = 'TreeSAK RootTree -i %s_PMSF_tree_wd/PMSF.treefile -o %s_with_outgroup_rooted.treefile -og %s' % (each_grp, each_grp, grp_outgroup_gnm)
        print(root_tree_cmd)

        rm_outgroup_gnm_cmd = 'TreeSAK rm_leaf -i %s_with_outgroup_rooted.treefile -o %s_with_outgroup_rooted.treefile -l %s' % (each_grp, each_grp, grp_outgroup_gnm)
        #print(rm_outgroup_gnm_cmd)





