import os

########################################################################################################################

meta_data_txt = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20251107.txt'
gnm_id_txt    = '/Users/songweizhi/Desktop/60.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

grp_to_gnm_dict = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if  gnm_id in gnm_id_set:
            tax = each_gnm_split[col_index['GTDB_Taxon_r226']]
            cpl = each_gnm_split[col_index['Completeness']]
            # if float(cpl) < 85:
                #print(gnm_id)
            if 'g__Cenarchaeum' in tax:
                print('%s\t%s\t%s' % (cpl, gnm_id, tax))

