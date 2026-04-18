
import os

########################################################################################################################

gnm_id_txt      = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/gnm_id_284.txt'
meta_data_txt   = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/metadata_614.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

gnm_to_genus_dict = dict()
max_genus_len = 0
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            host_species = each_gnm_split[col_index['Host']]
            if host_species == 'nonsponge':
                pass
            elif host_species == 'na':
                pass
            else:
                print('cp %s.fna symbiont_genomes/' % gnm_id)
                # print('%s\t%s' % (gnm_id, host_species))





