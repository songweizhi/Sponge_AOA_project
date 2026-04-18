
meta_data_txt       = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/metadata_614.txt'
gnm_id_txt          = '/Users/songweizhi/Desktop/3_combined_genomes_50_5_dRep97_284_id.txt'
gnm_id_txt          = '/Users/songweizhi/Desktop/dRep95_214.txt'
dbscc_gnm_id_txt    = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/gnm_id_291_DBSCCs.txt'
completeness_cutoff = 80

op_txt_symbiont     = '/Users/songweizhi/Desktop/214_grouping_symbiont_vs_freeliving.txt'
op_txt_dbscc        = '/Users/songweizhi/Desktop/214_grouping_DBSCC_vs_nonDBSCC_and_freeliving.txt'


gnm_id_set = set()
for each in open(gnm_id_txt):
    gnm_id_set.add(each.strip())

dbscc_gnm_id_set = set()
for each in open(dbscc_gnm_id_txt):
    dbscc_gnm_id_set.add(each.strip().split()[0])

op_txt_symbiont_handle = open(op_txt_symbiont, 'w')
op_txt_dbscc_handle = open(op_txt_dbscc, 'w')
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            gnm_cpl      = float(each_gnm_split[col_index['Completeness']])
            host_species = each_gnm_split[col_index['Host']]

            if gnm_cpl >= completeness_cutoff:
                if not 'coral' in host_species:
                    if host_species != 'na':

                        # write out symbiont_vs_freeliving
                        if host_species == 'nonsponge':
                            op_txt_symbiont_handle.write('%s\tFreeliving\n' % gnm_id)
                        else:
                            op_txt_symbiont_handle.write('%s\tSymbiont\n' % gnm_id)

                        # write out DBSCC_vs_nonDBSCC_and_freeliving
                        if gnm_id in dbscc_gnm_id_set:
                            op_txt_dbscc_handle.write('%s\tDBSCC\n' % gnm_id)
                        else:
                            op_txt_dbscc_handle.write('%s\tnonDBSCC\n' % gnm_id)

op_txt_symbiont_handle.close()
op_txt_dbscc_handle.close()

