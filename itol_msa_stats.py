import os
import math
from Bio import SeqIO


def sep_path_basename_ext(file_in):
    f_path, f_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(f_name)
    f_ext = f_ext[1:]
    return f_name, f_path, f_base, f_ext


aln_file = '/Users/songweizhi/Desktop/concatenated.phy.fasta'

aln_name, aln_path, aln_base, aln_ext = sep_path_basename_ext(aln_file)
stats_txt      = '%s/%s_gap_pct.txt'         % (aln_path, aln_base)
stats_txt_itol = '%s/%s_gap_pct_iTOL.txt'    % (aln_path, aln_base)

max_gap_pct = 0
stats_txt_handle = open(stats_txt, 'w')
for each_seq in SeqIO.parse(aln_file, 'fasta'):
    seq_id = each_seq.id
    seq_seq = str(each_seq.seq)
    gap_pct = seq_seq.count('-')*100/len(seq_seq)
    gap_pct = float("{0:.2f}".format(gap_pct))
    if gap_pct > max_gap_pct:
        max_gap_pct = gap_pct
    stats_txt_handle.write('%s\t%s\n' % (seq_id, gap_pct))
stats_txt_handle.close()

max_scale_value = math.ceil(max_gap_pct/5) * 5
gap_pct_itol_cmd = 'TreeSAK iTOL -SimpleBar -lv %s -scale 0-25-50-75-100 -lt Gap_Pecentage -o %s' % (stats_txt, stats_txt_itol)
os.system(gap_pct_itol_cmd)

