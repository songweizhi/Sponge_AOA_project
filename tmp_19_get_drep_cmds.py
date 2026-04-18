import os

########################################################################################################################

meta_data_txt = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20251107.txt'
gnm_id_txt    = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/gnm_id_1369.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])


grp_to_gnm_dict = dict()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if  gnm_id in gnm_id_set:
            host_species = each_gnm_split[col_index['Host_Species']]
            if host_species not in grp_to_gnm_dict:
                grp_to_gnm_dict[host_species] = set()
            grp_to_gnm_dict[host_species].add(gnm_id)

for grp in sorted(list(grp_to_gnm_dict.keys())):
    folder_name_no_space = grp.replace(' ', '_').replace('.', '')
    gnm_set = grp_to_gnm_dict[grp]
    sub_dir = '/Users/songweizhi/Desktop/drep_wd/%s/' % folder_name_no_space
    if os.path.isdir(sub_dir) is False:
        os.mkdir(sub_dir)
    for each_gnm in gnm_set:
        pass
        # print('cp /Users/songweizhi/Desktop/03_AOA_genomes_1369/%s.fna %s' % (each_gnm, sub_dir))
    if len(gnm_set) > 1:
        drep_cmd = 'BioSAK hpc3 -wt 23:59:59 -t 12 -q cpu -a boqianpy -conda drep -n drep95_%s -c "dRep dereplicate %s_dRep95_wd -g %s/*.fna -pa 0.9 -sa 0.95 --genomeInfo /scratch/PI/ocessongwz/Sponge_r226/03_AOA_genomes_1369_checkm2_quality_for_dRep.txt -comp 50 -p 12"' % (folder_name_no_space, folder_name_no_space, folder_name_no_space)
        #print(drep_cmd)
    else:
        cp_cmd = 'cp %s/%s.fna 0_dereplicated/' % (folder_name_no_space, list(gnm_set)[0])
        print(cp_cmd)



