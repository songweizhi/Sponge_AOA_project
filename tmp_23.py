
# file in
meta_data_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20251217.txt'
gnm_id_txt                  = '/Users/songweizhi/Desktop/2279.txt'

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

count_dict = dict()
n=0
col_index = dict()
cols_to_include_in_label_dict = dict()
cols_to_include_in_label_max_len_dict = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            gnm_taxon = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_taxon_split = gnm_taxon.split(';')
            gnm_family = gnm_taxon_split[4]
            if gnm_family not in count_dict:
                count_dict[gnm_family] = 0
            count_dict[gnm_family] += 1
            print(gnm_taxon)
            n+= 1

print(n)
print(count_dict)

