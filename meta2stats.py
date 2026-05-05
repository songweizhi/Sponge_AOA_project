
########################################################################################################################

meta_data_txt = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'
gnm_id_txt    = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_r232_2383.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])


habitat_set= set()
habitat_dict_f = dict()
habitat_dict_Nitrosopumilaceae = dict()

life_style_dict_f = dict()
life_style_dict_Nitrosopumilaceae = dict()
host_species_set = set()
genus_to_host_species_dict = dict()
host_grp_dict = dict()
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

            ############################################################################################################

            if aoa_f_r232 not in life_style_dict_f:
                life_style_dict_f[aoa_f_r232] = dict()
                life_style_dict_f[aoa_f_r232]['Free-living'] = 0
                life_style_dict_f[aoa_f_r232]['Host-associated'] = 0
            if host_grp not in ['NA', 'Na', 'na']:
                if host_grp == 'Freeliving':
                    life_style_dict_f[aoa_f_r232]['Free-living'] += 1
                else:
                    life_style_dict_f[aoa_f_r232]['Host-associated'] += 1

            ############################################################################################################

            if aoa_f_r232 == 'f__Nitrosopumilaceae':

                if aoa_g_r232 not in life_style_dict_Nitrosopumilaceae:
                    life_style_dict_Nitrosopumilaceae[aoa_g_r232] = dict()
                    life_style_dict_Nitrosopumilaceae[aoa_g_r232]['Free-living'] = 0
                    life_style_dict_Nitrosopumilaceae[aoa_g_r232]['Host-associated'] = 0
                if host_grp not in ['NA', 'Na', 'na']:
                    if host_grp == 'Freeliving':
                        life_style_dict_Nitrosopumilaceae[aoa_g_r232]['Free-living'] += 1
                    else:
                        life_style_dict_Nitrosopumilaceae[aoa_g_r232]['Host-associated'] += 1

            ############################################################################################################

            if host_grp not in ['Freeliving']:
                if host_grp not in host_grp_dict:
                    host_grp_dict[host_grp] = 0
                host_grp_dict[host_grp] += 1

            ############################################################################################################

            habitat_to_use = gnm_habitat_4
            if aoa_f_r232 not in habitat_dict_f:
                habitat_dict_f[aoa_f_r232] = dict()
            if habitat_to_use not in habitat_dict_f[aoa_f_r232]:
                habitat_dict_f[aoa_f_r232][habitat_to_use] = 0
            habitat_set.add(habitat_to_use)
            habitat_dict_f[aoa_f_r232][habitat_to_use] += 1

            ############################################################################################################

            habitat_to_use = gnm_habitat_4
            if aoa_f_r232 == 'f__Nitrosopumilaceae':
                if aoa_g_r232 not in habitat_dict_Nitrosopumilaceae:
                    habitat_dict_Nitrosopumilaceae[aoa_g_r232] = dict()
                if habitat_to_use not in habitat_dict_Nitrosopumilaceae[aoa_g_r232]:
                    habitat_dict_Nitrosopumilaceae[aoa_g_r232][habitat_to_use] = 0
                habitat_set.add(habitat_to_use)
                habitat_dict_Nitrosopumilaceae[aoa_g_r232][habitat_to_use] += 1


# print('-----------------------------------------------------------------------------------------------------------------')
# print('\tFree-living\tHost-associated')
# for each_f in life_style_dict_f:
#     print(each_f, life_style_dict_f[each_f]['Free-living'], life_style_dict_f[each_f]['Host-associated'], sep='\t')
# print('-----------------------------------------------------------------------------------------------------------------')
#
#
# print('-----------------------------------------------------------------------------------------------------------------')
# print('\tFree-living\tHost-associated')
# for each_g in life_style_dict_Nitrosopumilaceae:
#     print(each_g, life_style_dict_Nitrosopumilaceae[each_g]['Free-living'], life_style_dict_Nitrosopumilaceae[each_g]['Host-associated'], sep='\t')
# print('-----------------------------------------------------------------------------------------------------------------')
#
# for each_host in host_grp_dict:
#     print('%s(%s)\t%s' % (each_host, host_grp_dict[each_host], host_grp_dict[each_host]))
#
# # print('-----------------------------------------------------------------------------------------------------------------')
#
# habitat_list_sorted = sorted(list(habitat_set))
# print('\t%s'% '\t'.join(habitat_list_sorted))
# for each_f in habitat_dict_f:
#     current_dict = habitat_dict_f[each_f]
#     value_list = [each_f]
#     for each_habitat in habitat_list_sorted:
#         value_list.append(str(current_dict.get(each_habitat, 0)))
#     print('\t'.join(value_list))
#
# print('-----------------------------------------------------------------------------------------------------------------')

habitat_list_sorted = sorted(list(habitat_set))
print('\t%s'% '\t'.join(habitat_list_sorted))
for each_g in habitat_dict_Nitrosopumilaceae:
    current_dict = habitat_dict_Nitrosopumilaceae[each_g]
    value_list = [each_g]
    for each_habitat in habitat_list_sorted:
        value_list.append(str(current_dict.get(each_habitat, 0)))
    print('\t'.join(value_list))

print('-----------------------------------------------------------------------------------------------------------------')
