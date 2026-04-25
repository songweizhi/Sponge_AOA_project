
########################################################################################################################

meta_data_txt   = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'
gnm_id_txt      = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_r232_2395.txt'
gnm_grp_txt     = '/Users/songweizhi/Desktop/Sponge_r226/08_Host_specificity/genome_group_.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

n = 0
grp_to_gnm_dict = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if  gnm_id in gnm_id_set:
            gnm_tax_str   = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_genus = gnm_tax_str.split(';')[5]
            gnm_dbscc = each_gnm_split[col_index['DBSCC']]

            if gnm_dbscc != 'na':
                if gnm_dbscc not in grp_to_gnm_dict:
                    grp_to_gnm_dict[gnm_dbscc] = set()
                grp_to_gnm_dict[gnm_dbscc].add(gnm_id)
            else:
                if gnm_genus != 'g__':
                    if gnm_genus not in grp_to_gnm_dict:
                        grp_to_gnm_dict[gnm_genus] = set()
                    grp_to_gnm_dict[gnm_genus].add(gnm_id)
                else:
                    print(gnm_id)

            n += 1

gnm_grp_txt_handle = open(gnm_grp_txt, 'w')
for each_grp in grp_to_gnm_dict:
    for each_gnm in grp_to_gnm_dict[each_grp]:
        gnm_grp_txt_handle.write('%s\t%s\n' % (each_gnm, each_grp))
gnm_grp_txt_handle.close()
