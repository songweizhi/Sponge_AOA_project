
def get_shared_uniq_elements(list_1, list_2):
    shared_set = set(list_1).intersection(list_2)
    list_1_uniq = []
    for e1 in list_1:
        if e1 not in shared_set:
            list_1_uniq.append(e1)
    list_2_uniq = []
    for e2 in list_2:
        if e2 not in shared_set:
            list_2_uniq.append(e2)
    return shared_set, list_1_uniq, list_2_uniq


meta_data_txt                       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260419.txt'
gnm_id_txt_drep95                   = '/Users/songweizhi/Desktop/Sponge_r226/10_OMA/AOA_2279_dRep95_905.txt'
gnm_id_txt_drep85                   = '/Users/songweizhi/Desktop/Sponge_r226/10_OMA/AOA_2279_dRep85_317.txt'
interested_taxa_list                = ['f__Nitrosocaldaceae', 'f__Nitrososphaeraceae', 'g__Nitrosotalea', 'g__TA-20', 'g__JACQFM01', 'g__JBBDNF01', 'g__UBA8516', 'g__Nitrosarchaeum', 'g__Nitrosomaritimum', 'g__Nitrosarchaeum_A', 'g__DRGT01', 'g__CSP1-1', 'g__VHBM01', 'g__Nitrosotenuis', 'g__Nitrosopelagicus']

'''
'''









gnm_id_set_drep95 = set()
for each_gnm in open(gnm_id_txt_drep95):
    gnm_id_set_drep95.add(each_gnm.strip().split()[0])

gnm_id_set_drep85 = set()
for each_gnm in open(gnm_id_txt_drep85):
    gnm_id_set_drep85.add(each_gnm.strip().split()[0])

shared_set, drep95_uniq, drep85_uniq = get_shared_uniq_elements(gnm_id_set_drep95, gnm_id_set_drep85)

n = 0
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in drep95_uniq:
            gnm_tax_226        = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_tax_232        = each_gnm_split[col_index['GTDB_Taxon_r232']]
            from_interested_taxa = False
            for interested_taxa in interested_taxa_list:
                if (interested_taxa + ';') in gnm_tax_226:
                    from_interested_taxa = True
            if from_interested_taxa is True:
                print('mv %s.fa 000/' % gnm_id)


                n += 1

print(n)
'''
f__Nitrosocaldaceae_____GCA938030895_1
f__Nitrosocaldaceae_____GCA046299465_1

'''