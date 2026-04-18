from Bio import SeqIO


meta_data_txt   = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260130.txt'

fa_file         = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_g_representatives_JL.fasta'
wd              =  '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_g_representatives_JL_wd_WoRMS'

fa_file         = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_COI_iden95_g_representatives_JL.ffn'
wd              =  '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_COI_iden95_g_representatives_JL_wd_WoRMS'

genus_grp_dict = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        host_taxon_str_split = each_gnm_split[col_index['Host_Taxon']].split(';')
        host_c  = 'c__'
        host_sc = 'sc__'
        host_o  = 'o__'
        host_g  = 'g__'
        for each in host_taxon_str_split:
            if each.startswith('o__'):
                host_o = each
            if each.startswith('g__'):
                host_g = each
            if each.startswith('sc__'):
                host_sc = each
            if each.startswith('c__'):
                host_c = each

        if host_c in ['c__Hexactinellida', 'c__Homoscleromorpha']:
            genus_grp_dict[host_g] = host_c
            if gnm_id.startswith('JL'):
                genus_grp_dict[gnm_id.split('_bin')[0]] = host_c
        elif host_sc in ['sc__Keratosa', 'sc__Verongimorpha']:
            genus_grp_dict[host_g] = host_sc
            if gnm_id.startswith('JL'):
                genus_grp_dict[gnm_id.split('_bin')[0]] = host_sc
        else:
            genus_grp_dict[host_g] = host_o
            if gnm_id.startswith('JL'):
                genus_grp_dict[gnm_id.split('_bin')[0]] = host_o

o_to_g_dict = dict()
for each_seq in SeqIO.parse(fa_file,'fasta'):
    seq_id = each_seq.id
    seq_o = genus_grp_dict[seq_id]
    if seq_o not in o_to_g_dict:
        o_to_g_dict[seq_o] = set()
    o_to_g_dict[seq_o].add(seq_id)

for each_grp in sorted(list(o_to_g_dict.keys())):
    member_list = o_to_g_dict[each_grp]
    member_list_sorted = sorted(list(member_list))
    #print(each_grp, ','.join(member_list_sorted), sep='\t')

    if len(member_list_sorted) > 1:

        # op_txt = '%s/%s.txt' % (wd, each_grp)
        # op_txt_handle = open(op_txt, 'w')
        # op_txt_handle.write('\n'.join(member_list_sorted) + '\n')
        # op_txt_handle.close()

        select_seq_cmd  = 'BioSAK select -i %s -id %s_with_outgroup.txt -o %s_with_outgroup.fa'                                                             % (fa_file, each_grp, each_grp)
        #print(select_seq_cmd)
        mafft_cmd       = 'mafft %s_with_outgroup.fa > %s_with_outgroup.aln'                                                                                % (each_grp, each_grp)
        print(mafft_cmd)
        iqtree_cmd      = 'mkdir %s_with_outgroup; iqtree -m GTR+I+G -bb 1000 --wbtl -nt 10 -s %s_with_outgroup.aln -pre %s_with_outgroup/%s_with_outgroup' % (each_grp, each_grp, each_grp, each_grp)
        print(iqtree_cmd)
        root_tree_cmd   = 'TreeSAK RootTree -i %s_with_outgroup/%s_with_outgroup.treefile -o %s_with_outgroup_rooted.treefile -og '                         % (each_grp, each_grp, each_grp)
        #print(root_tree_cmd)
        subset_tree_cmd = 'TreeSAK subset -i %s_with_outgroup_rooted.treefile -fi 0 -k %s.txt -o %s_rooted.treefile -fo 9'                                  % (each_grp, each_grp, each_grp)
        #print(subset_tree_cmd)



