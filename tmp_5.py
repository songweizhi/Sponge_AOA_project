
metadata_txt    = '/Users/songweizhi/Desktop/Sponge_r226/AOA_genomes_combined_1221_metadata.txt'
cdb_csv         = '/Users/songweizhi/Desktop/Sponge_r226/03_AOA_genomes_dRep/Cdb_ANI99_reformatted.csv'

m = 0
metadata_dict = dict()
col_index = dict()
line_num_index = 0
for each_line in open(metadata_txt):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        col_index = {key: i for i, key in enumerate(line_split)}
    else:
        gnm_id                  = line_split[col_index['Genome']]
        host_species            = line_split[col_index['Host_species']]
        host_cate            = line_split[col_index['Host_category']]
        metadata_dict[gnm_id]   = host_species

        if host_cate == 'Sponge_AOA_project':
            print('cp %s.fna /scratch/PI/ocessongwz/Sponge_r226/03_AOA_genomes_1221_dRep99_plus_all_sponge_symbionts/000/' % gnm_id)
            m += 1

print(m)

cdb_dict = dict()
for each_line in open(cdb_csv):
    each_line_split = each_line.strip().split('\t')
    c_id = each_line_split[0]
    c_gnm_list = each_line_split[1:]
    cdb_dict[c_id] = c_gnm_list

# gnms_to_keep = set()
# n = 0
# for each_c in cdb_dict:
#     c_gnm_list = cdb_dict[each_c]
#     meta_list = set()
#     for each_gnm in c_gnm_list:
#         gnm_host = metadata_dict[each_gnm]
#         meta_list.add(gnm_host)
#
#     if len(meta_list) > 1:
#         if meta_list != {'na', 'Freeliving'}:
#             print(each_c, c_gnm_list, meta_list)
#             for g in c_gnm_list:
#                 gnms_to_keep.add(g)
#             n += 1
#
# print(n)
# print(gnms_to_keep)
# print(len(gnms_to_keep))
