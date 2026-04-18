import os
import glob
import subprocess

file_dir = '/home/ocessongwz/scratch/Sponge_r226/03_AOA_genomes_1369_dRep85_263_OMA_wd/Output/OMA_dRep85_260_cov85/SplitScore1_op_dir'
file_ext = 'log'

file_re = '%s/*.%s' % (file_dir, file_ext)
file_list = glob.glob(file_re)

for each in file_list:
    last_line = subprocess.check_output(['tail', '-1', each])
    if 'Date and Time: ' in str(last_line):
        id = each.split('/')[-1][:-4]
        os.system('mv %s.aln done/' % id)
        os.system('mv %s.bionj done/' % id)
        os.system('mv %s.ckp.gz done/' % id)
        os.system('mv %s.contree done/' % id)
        os.system('mv %s.fa done/' % id)
        os.system('mv %s.iqtree done/' % id)
        os.system('mv %s.log done/' % id)
        os.system('mv %s.mldist done/' % id)
        os.system('mv %s.splits.nex done/' % id)
        os.system('mv %s.treefile done/' % id)
        os.system('mv %s_trimmed.aln done/' % id)
        os.system('mv %s.ufboot done/' % id)
