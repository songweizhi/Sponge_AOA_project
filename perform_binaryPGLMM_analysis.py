import os
import glob


def sep_path_basename_ext(file_in):
    f_path, file_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(file_name)
    return f_path, f_base, f_ext


########################################################################################################################

# # file in
# gapseq_wd       = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/GapSeq_wd'
# gnm_host_txt    = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/iTOL_files/for_iTOL_lifestyle.txt'
# presence_min    = 3
# presence_max    = 200

# # file out
# ignored_pwy_txt = '/Users/songweizhi/Desktop/ignored_pwy.txt'
# op_data_matrix  = '/Users/songweizhi/Desktop/op_data_matrix.txt'

########################################################################################################################

'''
gnm_group_main_symbionts_clade1_18.txt
gnm_group_main_symbionts_clade2_4.txt
gnm_group_main_symbionts_clades.txt
'''

# file in
gapseq_wd       = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/GapSeq_wd'
gnm_group_txt   = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/12_PhyloBiAssoc_wd/gnm_group_main_symbionts_clade1_18.txt'
presence_min    = 3
presence_max    = 200

# file out
ignored_pwy_txt = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/12_PhyloBiAssoc_wd/ignored_pwy.txt'
op_data_matrix  = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/12_PhyloBiAssoc_wd/gapseq_pwy_df_gnm_grouped_by_major_symbionts_clade1_18.txt'

########################################################################################################################

gnm_group_dict = dict()
for each in open(gnm_group_txt):
    each_split = each.strip().split('\t')
    gnm_group_dict[each_split[0]] = each_split[1]

pathways_tbl_re   = '%s/*-all-Pathways.tbl' % gapseq_wd
pathways_tbl_list = glob.glob(pathways_tbl_re)

gnm_id_set = set()
pwy_desc_dict = dict()
pwy_to_gnm_dict = dict()
gnm_to_pwy_dict = dict()
for each_pathways_tbl in pathways_tbl_list:
    f_path, f_base, f_ext = sep_path_basename_ext(each_pathways_tbl)
    gnm_id = f_base.split('-all-Pathways')[0]
    gnm_id_set.add(gnm_id)
    gnm_to_pwy_dict[gnm_id] = set()
    for each_pwy in open(each_pathways_tbl):
        if not each_pwy.startswith('#'):
            if not each_pwy.startswith('ID	Name	Prediction	Completeness'):
                each_pwy_split = each_pwy.strip().split('\t')
                pwy_id = each_pwy_split[0]
                if '|' in pwy_id:
                    pwy_id = pwy_id.replace('|', '')
                pwy_desc = each_pwy_split[1]
                presence = each_pwy_split[2]

                # add to pwy_desc_dict
                if pwy_id not in pwy_desc_dict:
                    pwy_desc_dict[pwy_id] = pwy_desc

                if presence == 'true':

                    # add to pwy_to_gnm_dict
                    if pwy_id not in pwy_to_gnm_dict:
                        pwy_to_gnm_dict[pwy_id] = {gnm_id}
                    else:
                        pwy_to_gnm_dict[pwy_id].add(gnm_id)

                    # add to gnm_to_pwy_dict
                    gnm_to_pwy_dict[gnm_id].add(pwy_id)


ignored_pwy_set = set()
ignored_pwy_txt_handle = open(ignored_pwy_txt, 'w')
qualified_pwy_set = set()
for pwy in pwy_to_gnm_dict:
    detected_in = pwy_to_gnm_dict[pwy]
    if presence_min <= len(detected_in) <= presence_max:
        qualified_pwy_set.add(pwy)
    else:
        ignored_pwy_set.add(pwy)
        ignored_pwy_txt_handle.write('%s\t%s/%s\t%s\n' % (pwy, len(detected_in), len(gnm_id_set), pwy_desc_dict[pwy]))
ignored_pwy_txt_handle.close()

if len(ignored_pwy_set) == 0:
    os.system('rm %s' % ignored_pwy_txt)

qualified_pwy_list_sorted = sorted(list(qualified_pwy_set))

# write out data matrix for binaryPGLMM analysis
op_data_matrix_handle = open(op_data_matrix, 'w')
op_data_matrix_handle.write('ID\tcate\t%s\n' % '\t'.join(qualified_pwy_list_sorted))
for each_gnm in sorted(list(gnm_id_set)):
    gnm_encoded_pwys = gnm_to_pwy_dict[each_gnm]
    gnm_cate = gnm_group_dict[each_gnm]
    pa_list = [each_gnm, gnm_cate]
    for each_pwy in qualified_pwy_list_sorted:
        if each_pwy in gnm_encoded_pwys:
            pa_list.append('1')
        else:
            pa_list.append('0')
    op_data_matrix_handle.write('\t'.join(pa_list) + '\n')
op_data_matrix_handle.close()


print('detected genome:\t%s'              % len(gnm_id_set))
print('qualified/detected pwy:\t%s/%s'    % (len(qualified_pwy_set), len(pwy_to_gnm_dict)))
print('data matrix exported to:\t%s'      % op_data_matrix)


rooted_tree_file = '/Users/songweizhi/Documents/Research/Sponge/11_ALE_wd/OMA_cov85_213_top25_BMGE.rooted.treefile'
PhyloBiAssoc_cmd = 'TreeSAK PhyloBiAssoc -t 10 -i %s -d %s -o PhyloBiAssoc_wd_gnm_grouped_by_major_symbionts_clade1_18' % (rooted_tree_file, op_data_matrix)
print(PhyloBiAssoc_cmd)

'''
BioSAK PhyloBiAssoc -t demo.tre -d demo.txt
cd /Users/songweizhi/Documents/Research/Sponge_AOA_project/12_ALE_wd
TreeSAK PhyloBiAssoc -i /Users/songweizhi/Documents/Research/Sponge_AOA_project/11_ALE_wd/OMA_cov85_213_top25_BMGE.rooted.treefile -d op_data_matrix.txt

cd /Users/songweizhi/Documents/Research/Sponge_AOA_project/12_ALE_wd
TreeSAK PhyloBiAssoc -t /Users/songweizhi/Documents/Research/Sponge_AOA_project/11_ALE_wd/OMA_cov85_213_top25_BMGE.rooted.treefile -d /Users/songweizhi/Documents/Research/Sponge_AOA_project/12_PhyloBiAssoc_wd/gapseq_pwy_df_gnm_grouped_by_major_symbionts_clades.txt -o PhyloBiAssoc_wd_gnm_grouped_by_major_symbionts_clades

'''

