
def get_best_gnm(gnm_list, gnm_quality_dict):
    best_gnm = ''
    current_score = 0
    for gnm in gnm_list:
        g_id = '.'.join(gnm.split('.')[:-1])
        gnm_qc = gnm_quality_dict[g_id]
        if gnm_qc > current_score:
            best_gnm = gnm
            current_score = gnm_qc
    return best_gnm

########################################################################################################################

meta_data_txt                = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20251107.txt'
Cdb_dRep95_reformatted_1_csv = '/Users/songweizhi/Desktop/Sponge_r226/03_AOA_genomes_dRep/Cdb_dRep95_reformatted_1.csv'

########################################################################################################################

# read in metadata
gnm_quality_score_dict = dict()
gnm_host_species_dict = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        host_species = each_gnm_split[col_index['Host_Species']]
        quality_index = float(each_gnm_split[col_index['Quality_Index']])
        gnm_host_species_dict[gnm_id] = host_species
        gnm_quality_score_dict[gnm_id] = quality_index

# read in dRep output
drep_cluster_to_gnm_dict = dict()
for each_c in open(Cdb_dRep95_reformatted_1_csv):
    each_c_split = each_c.strip().split('\t')
    c_id = each_c_split[0]
    gnm_list  = each_c_split[1:]
    drep_cluster_to_gnm_dict[c_id] = gnm_list

# get representative genomes
representative_gnm_set = set()
for each_cluster in drep_cluster_to_gnm_dict:
    gnm_member_list = drep_cluster_to_gnm_dict[each_cluster]
    if len(gnm_member_list) == 1:
        representative_gnm_set.add(gnm_member_list[0])
    else:
        # put genomes into groups
        grp_dict = dict()
        for each_gnm in gnm_member_list:
            g_id = '.'.join(each_gnm.split('.')[:-1])
            gnm_host_species = gnm_host_species_dict[g_id]
            quality_index = gnm_quality_score_dict[g_id]
            if gnm_host_species not in grp_dict:
                grp_dict[gnm_host_species] = []
            grp_dict[gnm_host_species].append(each_gnm)

        for each_grp in grp_dict:
            gnm_list = grp_dict[each_grp]
            rep_gnm = get_best_gnm(gnm_member_list, gnm_quality_score_dict)
            # print('%s\t%s\t%s\t%s' % (each_cluster, each_grp, gnm_list, rep_gnm))
            representative_gnm_set.add(rep_gnm)

print('representative genomes (%s)\n' % len(representative_gnm_set))
print('\n'.join(representative_gnm_set))
print('\nrepresentative genomes (%s)' % len(representative_gnm_set))

