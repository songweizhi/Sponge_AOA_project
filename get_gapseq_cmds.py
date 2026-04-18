
for each_gnm in open('/Users/songweizhi/Desktop/Sponge_r220/metadata/gnm_id_291.txt'):
    gnm_id = each_gnm.strip()
    gapseq_cmd = 'gapseq find -p all -t Archaea -b 100 -c 70 -m Archaea -l MetaCyc,KEGG -y /scratch/PI/ocessongwz/Sponge_r220/3_combined_genomes_50_5_dRep97_291/%s.fna > %s_stdout.txt' % (gnm_id, gnm_id)
    print(gapseq_cmd)
