
########################################################################################################################

# file in
metadata_txt    = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/iTOL_files/for_iTOL_lifestyle.txt'
gnm_id_txt      = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/6_combined_genomes_dereplicated_207_id.txt'

# file out
grouping_txt    = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/6_combined_genomes_dereplicated_207_grouping_enrich.txt'

########################################################################################################################

lifestyle_dict = dict()
for each in open(metadata_txt):
    each_split = each.strip().split('\t')
    lifestyle_dict[each_split[0]] = each_split[1]

grouping_txt_handle = open(grouping_txt, 'w')
for each_gnm in open(gnm_id_txt):
    gnm_id = each_gnm.strip()
    lifestyle = lifestyle_dict[gnm_id]
    gnm_grp = ''
    if lifestyle == 'sponge':
        gnm_grp = 'sponge'
    elif lifestyle == 'nonsponge':
        gnm_grp = 'nonsponge'
    elif lifestyle == 'na':
        gnm_grp = 'nonsponge'
    else:
        print('%s\t%s' % (gnm_id, lifestyle))
    grouping_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_grp))
grouping_txt_handle.close()



