

# n = 1
# for each_line in open('/Users/songweizhi/Desktop/Sponge_r226/10_ALE/genome_tree_leaf_rename.txt'):
#     gnm_id = each_line.strip().split('\t')[1]
#     gapseq_cmd = 'gapseq find -p all -t Archaea -b 100 -c 70 -l all -M prot -K 12 -T /project/spongeholobiont/tmp_dir_gapseq /project/spongeholobiont/Sponge_r226/AOA_genomes_faa/%s.faa' % gnm_id
#     gapseq_cmd = 'BioSAK hpc4 -q amd -a marmolecol -wt 23:59:59 -t 12 -conda gapseq -n gapseq%s -c "%s"' % (n, gapseq_cmd)
#     n += 1
#     print(gapseq_cmd)


n = 1
for gnm_id in open('/Users/songweizhi/Desktop/229.txt'):
    gnm_id = gnm_id.strip()
    gapseq_cmd = 'gapseq find -p all -t Archaea -b 100 -c 70 -l all -M prot -K 12 -T /project/spongeholobiont/tmp_dir_gapseq /project/spongeholobiont/Sponge_r226/07_ALE/ALE6_op_dir_75/faa_files/%s.faa' % gnm_id
    gapseq_cmd = 'BioSAK hpc4 -q amd -a marmolecol -wt 23:59:59 -t 12 -conda gapseq -n gapseq%s -c "%s"' % (n, gapseq_cmd)
    n += 1
    print(gapseq_cmd)



