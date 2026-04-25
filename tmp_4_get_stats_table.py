
meta_data_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'
gnm_id_txt                  = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_r232_2395.txt'


gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

host_genus_to_full_lineage_dict = dict()
host_species_to_dbscc_dict = dict()
dbscc_to_genus_dict = dict()
jl_host_taxa_dict = dict()
jl_sample_set = set()
tmp_dict = dict()
aoa_f_stats_dict = dict()
m = 0
n = 0
habitat_type_set = set()
gnm_habitat_dict = dict()
gnm_habitat_dict_g = dict()
host_cate_dict = dict()
gnm_f_count_dict = dict()
gnm_g_count_dict = dict()
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
            host_species         = each_gnm_split[col_index['Host_Species']]
            host_grp             = each_gnm_split[col_index['Host_Group']]
            host_taxon_str       = each_gnm_split[col_index['Host_Taxon']]
            host_taxon_str_split = host_taxon_str.split(';')
            gnm_size             = each_gnm_split[col_index['Size_Mbp_adjusted_by_cpl']]
            gc_content           = each_gnm_split[col_index['GC']]
            gnm_taxon            = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_taxon_r232       = each_gnm_split[col_index['GTDB_Taxon_r232']]
            gnm_habitat_1        = each_gnm_split[col_index['Habitat_1']]
            gnm_habitat_2        = each_gnm_split[col_index['Habitat_2']]
            gnm_habitat_3        = each_gnm_split[col_index['Habitat_3']]
            gnm_habitat_4        = each_gnm_split[col_index['Habitat_4']]
            gnm_dbscc            = each_gnm_split[col_index['DBSCC']]

            aoa_f_r232 = ''
            aoa_g_r232 = ''
            for each_r in gnm_taxon_r232.split(';'):
                if each_r.startswith('f__'):
                    aoa_f_r232 = each_r
                if each_r.startswith('g__'):
                    aoa_g_r232 = each_r

            ##### get family level stats #####

            if aoa_f_r232 not in aoa_f_stats_dict:
                aoa_f_stats_dict[aoa_f_r232] = 0
            aoa_f_stats_dict[aoa_f_r232] += 1

            ##################################

            if host_species not in ['Freeliving', 'Sponge', 'Coral']:

                # print(host_species)
                # host_genus = ''
                # for hr in host_taxon_str_split:
                #     if hr.startswith('g__'):
                #         host_genus = hr
                # print(host_genus)

                if ' sp.' not in host_species:
                    if gnm_dbscc != 'na':
                        if host_taxon_str not in host_species_to_dbscc_dict:
                            host_species_to_dbscc_dict[host_taxon_str] = set()
                        host_species_to_dbscc_dict[host_taxon_str].add(gnm_dbscc)





            ##################################

            ##################################

            # if aoa_f_r232 == 'f__Nitrosopumilaceae':
            #     print(gnm_habitat_3)
            #     if gnm_habitat_3 not in tmp_dict:
            #         tmp_dict[gnm_habitat_3] = 0
            #     tmp_dict[gnm_habitat_3] += 1
            #     n += 1

            # if gnm_habitat_3 in ['Marine', 'Coast', 'Estuary', 'Intertidal zone']:
            #     n += 1
            #     if aoa_f_r232 == 'f__Nitrosopumilaceae':
            #         m += 1
            # elif gnm_habitat_3 in ['Terrestrial', 'Groundwater and hot spring', 'Freshwater']:
            #     pass
            # else:
            #     print(gnm_habitat_3)
            # if gnm_habitat_3 not in tmp_dict:
            #     tmp_dict[gnm_habitat_3] = 0
            # tmp_dict[gnm_habitat_3] += 1

            ##################################

            # # get gnm_habitat_dict at genus level
            # if gnm_f == 'f__Nitrosopumilaceae':
            #     if gnm_g not in gnm_habitat_dict_g:
            #         gnm_habitat_dict_g[gnm_g] = dict()
            #     if gnm_habitat_4 not in gnm_habitat_dict_g[gnm_g]:
            #         gnm_habitat_dict_g[gnm_g][gnm_habitat_4] = 0
            #     gnm_habitat_dict_g[gnm_g][gnm_habitat_4] += 1
            #     habitat_type_set.add(gnm_habitat_4)
            #     n += 1
            #
            # # get gnm_habitat_dict
            # if gnm_f not in gnm_habitat_dict:
            #     gnm_habitat_dict[gnm_f] = dict()
            # if gnm_habitat_4 not in gnm_habitat_dict[gnm_f]:
            #     gnm_habitat_dict[gnm_f][gnm_habitat_4] = 0
            # gnm_habitat_dict[gnm_f][gnm_habitat_4] += 1
            # # habitat_type_set.add(gnm_habitat_4)
            #
            # if host_cate not in host_cate_dict:
            #     host_cate_dict[host_cate] = 0
            # host_cate_dict[host_cate] += 1
            #
            # if gnm_f not in gnm_f_count_dict:
            #     gnm_f_count_dict[gnm_f] = dict()
            #     gnm_f_count_dict[gnm_f]['symbiont']   = 0
            #     gnm_f_count_dict[gnm_f]['freeliving'] = 0
            # if host_cate == 'Freeliving':
            #     gnm_f_count_dict[gnm_f]['freeliving'] += 1
            # else:
            #     gnm_f_count_dict[gnm_f]['symbiont'] += 1
            #
            # if gnm_f == 'f__Nitrososphaeraceae':
            #     if gnm_g not in gnm_g_count_dict:
            #         gnm_g_count_dict[gnm_g] = dict()
            #         gnm_g_count_dict[gnm_g]['symbiont']   = 0
            #         gnm_g_count_dict[gnm_g]['freeliving'] = 0
            #     if host_cate == 'Freeliving':
            #         gnm_g_count_dict[gnm_g]['freeliving'] += 1
            #     else:
            #         gnm_g_count_dict[gnm_g]['symbiont'] += 1

# print(gnm_f_count_dict)
# for each in host_cate_dict:
#     print(each, host_cate_dict[each], sep='\t')

# for each in gnm_f_count_dict:
#     print(each, gnm_f_count_dict[each]['freeliving'], gnm_f_count_dict[each]['symbiont'],sep='\t')

# for each in gnm_g_count_dict:
#     print(each, gnm_g_count_dict[each]['freeliving'], gnm_g_count_dict[each]['symbiont'],sep='\t')


# habitat_type_list_sorted = sorted(list(habitat_type_set))
# print('\t' + '\t'.join(habitat_type_list_sorted))
# # get habitat table
# for each_tax in gnm_habitat_dict:
#     genome_num_list = [each_tax]
#     for each_habitat in habitat_type_list_sorted:
#         gnm_num = gnm_habitat_dict[each_tax].get(each_habitat, 0)
#         #print(each_habitat, gnm_habitat_dict[each_tax])
#         #print(gnm_num, gnm_habitat_dict[each_tax])
#         genome_num_list.append(gnm_num)
#     print('\t'.join(map(str, genome_num_list)))

# habitat_type_list_sorted = sorted(list(habitat_type_set))
# print('\t' + '\t'.join(habitat_type_list_sorted))
# # get habitat table
# for each_tax in gnm_habitat_dict_g:
#     genome_num_list = [each_tax]
#     for each_habitat in habitat_type_list_sorted:
#         gnm_num = gnm_habitat_dict_g[each_tax].get(each_habitat, 0)
#         genome_num_list.append(gnm_num)
#     print('\t'.join(map(str, genome_num_list)))

######################################################## report ########################################################

# get family level stats
# print(aoa_f_stats_dict)


print('==================================================')

print(tmp_dict)
for i in tmp_dict:
    print(i, tmp_dict[i], sep='\t')
print('n: %s' % n)
print('m: %s' % m)

print('==================================================\n')




for i in jl_host_taxa_dict:
    print(i, jl_host_taxa_dict[i], sep='\t')



for i in sorted(list(host_species_to_dbscc_dict.keys())):
    value_list_sorted = sorted(list(host_species_to_dbscc_dict[i]))
    if len(value_list_sorted) > 1:
        print(','.join(value_list_sorted), i, sep='\t')
