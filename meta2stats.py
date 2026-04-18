
########################################################################################################################

meta_data_txt = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20251107.txt'
gnm_id_txt    = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/gnm_id_1389.txt'
gnm_id_txt    = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/gnm_id_1369.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

host_species_set = set()
genus_to_host_species_dict = dict()
host_cate_dict = dict()
genus_set = set()
genus_stats_dict_all = dict()
genus_stats_dict_sym = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if  gnm_id in gnm_id_set:
            gnm_taxa     = each_gnm_split[col_index['GTDB_Taxon_r226']]
            host_cate    = each_gnm_split[col_index['Host_Category']]
            host_species = each_gnm_split[col_index['Host_Species']]
            host_genus = host_species
            if ' ' in host_species:
                host_genus = host_species.split(' ')[0]

            host_species = host_genus
            host_species_set.add(host_species)
            if host_cate not in host_cate_dict:
                host_cate_dict[host_cate] = 0
            host_cate_dict[host_cate] += 1
            gnm_taxa_split = gnm_taxa.split(';')
            gnm_genus = 'g__'
            for r in gnm_taxa_split:
                if r.startswith('g__'):
                    gnm_genus = r
            genus_set.add(gnm_genus)

            if gnm_genus not in genus_to_host_species_dict:
                genus_to_host_species_dict[gnm_genus] = dict()
            if host_species not in genus_to_host_species_dict[gnm_genus]:
                genus_to_host_species_dict[gnm_genus][host_species] = 0
            genus_to_host_species_dict[gnm_genus][host_species] += 1

            if gnm_genus not in genus_stats_dict_all:
                genus_stats_dict_all[gnm_genus] = 0
            genus_stats_dict_all[gnm_genus] += 1
            if host_cate  not in ['Freeliving']:
                if gnm_genus not in genus_stats_dict_sym:
                    genus_stats_dict_sym[gnm_genus] = 0
                genus_stats_dict_sym[gnm_genus] += 1

# print('\n\tAll\tSymbiont')
# for g in genus_set:
#     num_all = genus_stats_dict_all.get(g, 0)
#     num_sym = genus_stats_dict_sym.get(g, 0)
#     print('%s\t%s\t%s' % (g, num_all, num_sym))

print()

print('\t' + '\t'.join(sorted(list(host_species_set))))
for each_genus in sorted(list(genus_to_host_species_dict.keys())):
    num_list = [each_genus]
    for each_host_species in sorted(list(host_species_set)):
        current_num = genus_to_host_species_dict[each_genus].get(each_host_species, 0)
        num_list.append(str(current_num))
    print('\t'.join(num_list))




