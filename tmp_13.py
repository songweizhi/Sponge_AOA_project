from pprint import pprint

metadata_txt = '/Users/songweizhi/Desktop/metadata_614.txt'
habitat_txt  = '/Users/songweizhi/Desktop/habitat.txt'
op_txt       = '/Users/songweizhi/Desktop/metadata_614_new.txt'


gnm_habitat1_dict = dict()
gnm_habitat2_dict = dict()
gnm_location_dict = dict()
for each_line in open(habitat_txt):
    each_line_split = each_line.strip().split('\t')
    gnm_id = each_line_split[0]
    if ('GCA_' in gnm_id) or ('GCF_' in gnm_id):
        gnm_id = gnm_id.replace('GCA_', 'GCA').replace('GCF_', 'GCF').replace('.', '_')
    gnm_habitat1_dict[gnm_id] = each_line_split[1]
    gnm_habitat2_dict[gnm_id] = each_line_split[2]
    gnm_location_dict[gnm_id] = each_line_split[3]

op_txt_handle = open(op_txt, 'w')
col_index = dict()
for each_gnm in open(metadata_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
        op_txt_handle.write(each_gnm)
    else:
        gnm_id          = each_gnm_split[col_index['Genome']]
        host_type       = each_gnm_split[col_index['Host_type']]

        gnm_habitat1 = 'na'
        gnm_habitat2 = 'na'
        gnm_location = 'na'
        if host_type in ['sponge', 'coral']:
            gnm_habitat1 = host_type
            gnm_habitat2 = host_type
            gnm_location = 'na'
        else:
            gnm_habitat1 = gnm_habitat1_dict.get(gnm_id, 'na')
            gnm_habitat2 = gnm_habitat2_dict.get(gnm_id, 'na')
            gnm_location = gnm_location_dict.get(gnm_id, 'na')

        if (gnm_habitat1 == 'na') and (gnm_habitat2 == 'na') and (gnm_location == 'na'):
            print(gnm_id)

        op_txt_handle.write('%s\t%s\t%s\t%s\n' % (each_gnm.strip(), gnm_habitat1, gnm_habitat2, gnm_location))
op_txt_handle.close()
