import os


########################################################################################################################

meta_data_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260130.txt'
gnm_id_txt                  = '/Users/songweizhi/Desktop/Sponge_r226/08_Host_specificity/654.txt'
codiv_host_to_symbiont_txt  = '/Users/songweizhi/Desktop/Sponge_r226/08_Host_specificity/codiv_sponge_to_AOA.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

codiv_host_to_symbiont_txt_handle = open(codiv_host_to_symbiont_txt, 'w')
host_g_set = set()
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
            tax = each_gnm_split[col_index['GTDB_Taxon_r226']]
            host_taxon = each_gnm_split[col_index['Host_Taxon']]
            if host_taxon not in ['Freeliving']:
                host_taxon_split = host_taxon.split(';')
                host_g = 'g__'
                for each_r in host_taxon_split:
                    if each_r.startswith('g__'):
                        host_g = each_r
                if gnm_id.startswith('JL'):
                    host_g = '_'.join(gnm_id.split('_')[:-1])

                if host_g != 'g__':
                    print('%s\t%s' % (host_g, gnm_id))
                    codiv_host_to_symbiont_txt_handle.write('%s\t%s\n' % (host_g, gnm_id))
codiv_host_to_symbiont_txt_handle.close()
