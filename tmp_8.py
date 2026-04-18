import os.path

from Bio import SeqIO


def run_succeed(log_txt):

    last_line = ''
    for each_line in open(log_txt):
        last_line = each_line.strip()

    good_run = False
    if last_line.startswith('Date and Time'):
        good_run = True

    return good_run


# file in
# og_txt                  = '/Users/songweizhi/Desktop/13506OGs.txt'
# ale1_op_dir             = '/scratch/PI/ocessongwz/Sponge_r220/4_OMA_wd/OMA_wd/Output/ALE1_op_dir'
og_txt                  = '13506OGs.txt'
ale1_op_dir             = '/scratch/PI/ocessongwz/Sponge_r220/4_OMA_wd/OMA_wd/Output/ALE1_op_dir'

# file out
og_less_than_3_seq_txt  = 'og_with_less_than_3_seqs.txt'
good_run_txt            = 'good_run.txt'
bad_run_txt             = 'bad_run.txt'


good_run_txt_handle = open(good_run_txt, 'w')
bad_run_txt_handle = open(bad_run_txt, 'w')
og_less_than_3_seq_txt_handle = open(og_less_than_3_seq_txt, 'w')
for each_og in open(og_txt):
    each_og = each_og.strip()
    og_faa = '%s/%s.faa' % (ale1_op_dir, each_og)
    seq_num = 0
    for each_seq in SeqIO.parse(og_faa, 'fasta'):
        seq_num  +=1

    if seq_num <= 3:
        og_less_than_3_seq_txt_handle.write(each_og + '\n')
    else:
        log_txt = '%s/%s.log' % (ale1_op_dir, each_og)

        if os.path.isfile(log_txt)is False:
            good_run = False
        else:
            good_run = run_succeed(log_txt)

        if good_run is True:
            good_run_txt_handle.write(each_og + '\n')
        else:
            bad_run_txt_handle.write(each_og + '\n')

good_run_txt_handle.close()
bad_run_txt_handle.close()
og_less_than_3_seq_txt_handle.close()


