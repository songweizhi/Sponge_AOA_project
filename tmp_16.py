import os
import sys


'''
RefSeqs_with_AOA_18S_iden99_f_representatives_JL.fasta
RefSeqs_with_AOA_18S_iden99_g_representatives_JL.fasta
RefSeqs_with_AOA_18S_iden99_o_representatives_JL.fasta
RefSeqs_with_AOA_COI_iden95_f_representatives_JL.ffn
RefSeqs_with_AOA_COI_iden95_g_representatives_JL.ffn
RefSeqs_with_AOA_COI_iden95_o_representatives_JL.ffn
'''


def sep_path_basename_ext(file_in):

    f_path, f_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(f_name)
    f_ext = f_ext[1:]

    return f_name, f_path, f_base, f_ext

# js_index = 1
# for each_file in open('/Users/songweizhi/Desktop/aaa.txt'):
#     f_name, f_path, f_base, f_ext = sep_path_basename_ext(each_file.strip())
#     mafft_cmd  = 'mafft %s > %s.aln' % (f_name, f_base)
#     iqtree_cmd = 'BioSAK hpc4 -wt 119:59:59 -t 36 -q amd -a marmolecol -conda mybase2 -n iqtree%s -c "mkdir %s; iqtree2 -T 36 -B 1000 --alrt 1000 --quiet -s %s.aln --prefix %s/%s -m GTR+I+G -g sponge_phylogeny_Maria_%s_guide_tree.tre"' % (js_index, f_base, f_base, f_base, f_base, f_base)
#     iqtree_cmd = 'iqtree2 -T 10 -B 1000 --alrt 1000 --quiet -s %s.aln --prefix %s/%s -m GTR+I+G -g sponge_phylogeny_Maria_%s_guide_tree.tre' % (f_base, f_base, f_base, f_base)
#     print(iqtree_cmd)
#     js_index += 1


for each_file in open('/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_g_representatives_JL_wd/taxa_list.txt'):
    file_name       = each_file.strip()
    select_cmd      = 'BioSAK select -i ../RefSeqs_with_AOA_18S_iden99_g_representatives_JL.fasta -id %s.txt -o %s.fa'                  % (file_name, file_name)
    mafft_cmd       = 'mafft %s.fa > %s.aln'                                                                                            % (file_name, file_name)
    iqtree_cmd      = 'mkdir %s; iqtree -m GTR+I+G -bb 1000 --wbtl -nt 10 -s %s.aln -pre %s/%s'                                         % (file_name, file_name, file_name, file_name)
    root_tree_cmd   = 'TreeSAK RootTree -i %s/%s.treefile -o %s_rooted.treefile -og og_leaves'                                          % (file_name, file_name, file_name)
    subset_tree_cmd = 'TreeSAK subset -i %s_rooted.treefile -fi 0 -k %s_without_outgroup.txt -o %s_without_outgroup_rooted.tree -fo 9'  % (file_name, file_name, file_name)
    print(subset_tree_cmd)


# tax_lineage_dict = dict()
# for each_line in open('/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/tax_to_tax_lineage.txt'):
#     each_line_split = each_line.strip().split('\t')
#     tax_lineage_dict[each_line_split[0]] = each_line_split[1]
#
# for each_line in open('/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_g_representatives_JL_wd/RefSeqs_with_AOA_18S_iden99_g_representatives_JL.txt'):
#     each_line = each_line.strip()
#     if each_line.startswith('#'):
#         print(each_line)
#     else:
#         if len(each_line.strip()) > 0:
#             print(each_line, tax_lineage_dict[each_line], sep='\t')
#         else:
#             print()
