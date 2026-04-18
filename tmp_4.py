import os
import glob
from Bio import SeqIO


def sep_path_basename_ext(file_in):

    f_path, f_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(f_name)

    return f_name, f_path, f_base, f_ext[1:]


########################################################################################################################

fa_dir_in   = '/Users/songweizhi/Desktop/best_20'
fa_dir_out  = '/Users/songweizhi/Desktop/best_20_115_genomes'
gnm_id_txt  = '/Users/songweizhi/Desktop/3_combined_genomes_75_5_dRep85_115_id.txt'
file_ext    = 'fa'

fa_dir_in   = 'worst_20'
fa_dir_out  = 'worst_20_115_genomes'
gnm_id_txt  = '/scratch/PI/ocessongwz/Sponge_r220/3_combined_genomes_75_5_dRep85_115_id.txt'
file_ext    = 'fa'

########################################################################################################################

gnm_id_set = set()
for each in open(gnm_id_txt):
    gnm_id_set.add(each.strip())

fa_file_re = '%s/*.%s' % (fa_dir_in, file_ext)
fa_file_list = glob.glob(fa_file_re)

for each_fa in fa_file_list:
    fa_name, fa_path, fa_base, fa_ext = sep_path_basename_ext(each_fa)
    fa_out = '%s/%s' % (fa_dir_out, fa_name)
    fa_out_handle = open(fa_out, 'w')
    n = 0
    for each_seq in SeqIO.parse(each_fa, 'fasta'):
        seq_id = each_seq.id
        gnm_id = '_'.join(seq_id.split('_')[:-1])
        if gnm_id in gnm_id_set:
            fa_out_handle.write('>%s\n' % seq_id)
            fa_out_handle.write('%s\n' % each_seq.seq)
            n += 1
    fa_out_handle.close()
    print(n)
