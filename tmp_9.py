import os
import glob


# og_txt  = '/Users/songweizhi/Desktop/bad_run.txt'
# cmd_txt = '/Users/songweizhi/Desktop/ALE1_op_dir_cmds.txt'

# og_set = set()
# for each_og in open(og_txt):
#     og_set.add(each_og.strip())

# for each_cmd in open(cmd_txt):
#     og_id = each_cmd.split('.faa > ')[0].split(' --quiet ')[1]
#     if og_id in og_set:
#         print(each_cmd.strip())

# finished_og_set = set()
# for each_og in open('/Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/finished_OG.txt'):
#     finished_og_set.add(each_og.strip())
#
# file_dir = '/Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE1_op_dir_ufboot'
# file_ext = 'ufboot'
# file_re = '%s/*.%s' % (file_dir, file_ext)
# file_list = glob.glob(file_re)

# for each in file_list:
#     og_id = each.split('/')[-1].split('.')[0]
#     print(og_id)
#     if og_id in finished_og_set:
#         os.system('mv %s /Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE1_op_dir_ufboot_done/' % each)
#     else:
#         os.system('mv %s /Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE1_op_dir_ufboot_rest/' % each)


op_file_dir     = '/Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE2_op_dir'
op_file_ext     = 'uml_rec'
op_file_re      = '%s/*.%s' % (op_file_dir, op_file_ext)
op_file_list    = glob.glob(op_file_re)


ufboot_file_dir = '/Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE1_op_dir_ufboot_rest_4'
ufboot_file_ext = 'ufboot'
ufboot_file_re = '%s/*.%s' % (ufboot_file_dir, ufboot_file_ext)
ufboot_file_list = glob.glob(ufboot_file_re)


completed_og_set = set()
for i in op_file_list:
    og_id = i.split('genome_tree.newick_')[1].split('.ufboot.ale.')[0]
    completed_og_set.add(og_id)

for each_file in ufboot_file_list:
    og = each_file.split('/')[-1].split('.')[0]
    if og in completed_og_set:
        print(og)
        os.system('mv %s /Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE1_op_dir_ufboot_rest_4_done/' % each_file)
    else:
        os.system('mv %s /Users/songweizhi/Desktop/Sponge_r220/7_reconstruct_ancestral_genomes/ALE1_op_dir_ufboot_rest_4_rest/' % each_file)

