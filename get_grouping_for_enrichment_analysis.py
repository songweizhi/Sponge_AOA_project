
meta_data_txt   = '/Users/songweizhi/Desktop/Sponge_r220/metadata/metadata_614.txt'
gnm_id_txt      = '/Users/songweizhi/Desktop/Sponge_r220/metadata/gnm_id_291.txt'

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

col_index = {}
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id   = each_gnm_split[col_index['Genome']]
        gnm_size = float(each_gnm_split[col_index['Size_Mbp_adjusted_by_cpl']])
        gnm_gc   = float(each_gnm_split[col_index['GC']])

        if gnm_id in gnm_id_set:
            host_species = each_gnm_split[col_index['Host']]

            if host_species == 'nonsponge':
                print('%s\t%s\t%s' % ('gnm_id', gnm_id, 'freeliving'))
                pass
            elif host_species == 'sponge':
                print('%s\t%s\t%s' % ('gnm_id', gnm_id, 'symbiont'))
                pass
            elif host_species == 'na':
                pass
            elif 'coral' in host_species:
                pass
            else:
                print('%s\t%s\t%s' % ('gnm_id', gnm_id, 'symbiont'))
                pass
