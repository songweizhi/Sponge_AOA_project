from pip._internal.resolution.resolvelib import found_candidates

meta_data_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'
gnm_id_txt                  = '/Users/songweizhi/Desktop/AOA_for_dating_99.txt'


gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])


found_set = set()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            gnm_taxon_r232       = each_gnm_split[col_index['GTDB_Taxon_r232']]
            gnm_dbscc            = each_gnm_split[col_index['DBSCC']]
            aoa_f_r232 = ''
            aoa_g_r232 = ''
            for each_r in gnm_taxon_r232.split(';'):
                if each_r.startswith('f__'):
                    aoa_f_r232 = each_r
                if each_r.startswith('g__'):
                    aoa_g_r232 = each_r

            if gnm_dbscc != 'na':
                print(gnm_id, gnm_dbscc, sep='\t')
                found_set.add(gnm_id)
            else:
                if aoa_f_r232 in ['f__Nitrosocaldaceae', 'f__Nitrososphaeraceae', 'f__UBA213']:
                    print(gnm_id, aoa_f_r232, sep='\t')
                    found_set.add(gnm_id)
                else:
                    print(gnm_id, aoa_g_r232, sep='\t')
                    found_set.add(gnm_id)

print(len(found_set))
