
meta_data_txt                       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260408.txt'
gnm_id_txt                          = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/gnm_id_2287.txt'


gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

n = 0
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            gnm_tax        = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_dbscc      = each_gnm_split[col_index['DBSCC']]
            host_taxon_str = each_gnm_split[col_index['Host_Taxon']]
            gnm_label_str  = each_gnm_split[col_index['habitat_for_labelling']]

            if gnm_dbscc == 'D6':
                print(gnm_label_str, host_taxon_str)
                n += 1

print(n)





