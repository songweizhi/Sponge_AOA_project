import os

# selected_genome_txt = '/Users/songweizhi/Desktop/aaa.txt'
# gnm_dir             = '/srv/scratch/z5265700/Shan_z5095298/z5095298/Weizhi/Sponge_2023_08_25/s1_get_genome/Nitrosopumilaceae_50_5_dRep97_195'
# gnm_ext             = 'fna'
# prokka_cmds_txt     = '/Users/songweizhi/Desktop/aaa_prokka.txt'


# prokka_cmds_txt_handle = open(prokka_cmds_txt, 'w')
# for each_gnm in open(selected_genome_txt):
#     gnm_id = each_gnm.strip().split('.fna')[0]
#     pwd_gnm_file = '%s/%s.%s' % (gnm_dir, gnm_id, gnm_ext)
#     prokka_cmd     = 'prokka --force --compliant --cpus 1 --kingdom Archaea --prefix %s --locustag %s --strain %s --outdir %s_prokka_wd %s' % (gnm_id, gnm_id, gnm_id, gnm_id, pwd_gnm_file)
#     prokka_cmds_txt_handle.write(prokka_cmd + '\n')
# prokka_cmds_txt_handle.close()


# selected_genome_txt = '/Users/songweizhi/Desktop/Nitrososphaerales_50_5_GTDB_416.txt'
# gnm_dir             = '/scratch/PI/ocessongwz/Sponge_r220/8_AOA_habitat/Nitrososphaerales_50_5_GTDB_416'
# gnm_ext             = 'fna'
# prokka_cmds_txt     = '/Users/songweizhi/Desktop/Nitrososphaerales_50_5_GTDB_416_prokka.txt'
#
#
# prokka_cmds_txt_handle = open(prokka_cmds_txt, 'w')
# for each_gnm in open(selected_genome_txt):
#     gnm_id = each_gnm.strip().split('.fna')[0]
#     pwd_gnm_file = '%s/%s.%s' % (gnm_dir, gnm_id, gnm_ext)
#     prokka_cmd     = 'prokka --force --compliant --cpus 1 --kingdom Archaea --prefix %s --locustag %s --strain %s --outdir %s_prokka_wd %s' % (gnm_id, gnm_id, gnm_id, gnm_id, pwd_gnm_file)
#     prokka_cmds_txt_handle.write(prokka_cmd + '\n')
# prokka_cmds_txt_handle.close()

n = 1
for each_gnm in open('/Users/songweizhi/Desktop/157.txt'):
    gnm_id = each_gnm.strip()
    prokka_cmd     = 'BioSAK hpc4 -q amd -a marmolecol -wt 02:59:59 -t 1 -conda prokka -n prokka_%s -c "prokka --force --compliant --metagenome --cpus 1 --kingdom Archaea --prefix %s --locustag %s --strain %s --outdir %s_prokka_wd %s.fna"' % (n, gnm_id, gnm_id, gnm_id, gnm_id, gnm_id)
    # prokka_cmd     = 'prokka --force --compliant --metagenome --cpus 1 --kingdom Archaea --prefix %s --locustag %s --strain %s --outdir %s_prokka_wd %s.fna' % (gnm_id, gnm_id, gnm_id, gnm_id, gnm_id)
    print(prokka_cmd)
    n += 1

