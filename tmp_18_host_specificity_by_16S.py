from Bio import SeqIO


########################################################################################################################

gnm_dbscc_txt       = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/DBSCC_genomes.txt'
gnm_metadata_txt    = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/metadata_614.txt'
otu_seq_file        = '/Users/songweizhi/Desktop/Sponge_r220/11_host_specificity_by_16S/Torsten_NC/S3_representative_OTUs_45982.fasta'
blast_op_txt        = '/Users/songweizhi/Desktop/Sponge_r220/11_host_specificity_by_16S/blastn_symbionts_16S_vs_S3_representative_OTUs_45982.txt'
otu_table           = '/Users/songweizhi/Desktop/Sponge_r220/11_host_specificity_by_16S/Torsten_NC/S4_OTU_table_pct.txt'
sample_metadata_txt = '/Users/songweizhi/Desktop/Sponge_r220/11_host_specificity_by_16S/Torsten_NC/10346_20230201-070642.txt'
iden_cutoff         = 99
aln_cov_cutoff      = 99
otu_table_min_count = 0
otu_table_min_pct   = 0.1

########################################################################################################################

gnm_dbscc_dict = dict()
for each_line in open(gnm_dbscc_txt):
    line_split = each_line.strip().split()
    gnm_dbscc_dict[line_split[0]] = line_split[1]

gnm_host_dict = dict()
col_index = dict()
for each_gnm in open(gnm_metadata_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        host_species = each_gnm_split[col_index['Host']]
        gnm_host_dict[gnm_id] = host_species

otu_len_dict = dict()
for each_seq in SeqIO.parse(otu_seq_file, 'fasta'):
    otu_len_dict[each_seq.id] = len(each_seq.seq)

query_gnm_to_subject_dict = dict()
for each_line in open(blast_op_txt):
    line_split = each_line.strip().split()
    query_id = line_split[0]
    query_gnm = query_id.split('_16S_')[0]
    subject_id = line_split[1]
    iden = float(line_split[2])
    aln_len = int(line_split[3])
    otu_len = otu_len_dict.get(line_split[1])
    aln_cov = aln_len*100/otu_len
    if (iden >= iden_cutoff) and (aln_cov >= aln_cov_cutoff):
        if query_gnm not in query_gnm_to_subject_dict:
            query_gnm_to_subject_dict[query_gnm] = set()
        query_gnm_to_subject_dict[query_gnm].add(subject_id)

otu_to_sample_dict_with_value = dict()
header_list = []
line_num_index = 0
for each_line in open(otu_table):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        header_list = line_split[1:]
    else:
        otu_id = line_split[0]
        count_list = line_split[1:]
        for (sample_id, otu_count) in zip(header_list, count_list):
            if float(otu_count) > 0:
                if otu_id not in otu_to_sample_dict_with_value:
                    otu_to_sample_dict_with_value[otu_id] = dict()
                otu_to_sample_dict_with_value[otu_id][sample_id] = float(otu_count)

sample_metadata_dict = dict()
col_index = dict()
line_num_index = 0
for each_line in open(sample_metadata_txt):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        col_index = {key: i for i, key in enumerate(line_split)}
    else:
        sample_id            = line_split[col_index['sample_name']]
        anonymized_name      = line_split[col_index['anonymized_name']]
        host_scientific_name = line_split[col_index['host_scientific_name']]
        env_material         = line_split[col_index['env_material']]
        if host_scientific_name == 'not applicable':
            sample_metadata_dict[anonymized_name] = env_material
        else:
            sample_metadata_dict[anonymized_name] = host_scientific_name

# get stats
query_to_sample_dod = dict()
for each_16s in sorted(list(query_gnm_to_subject_dict.keys())):
    gnm_dbscc = gnm_dbscc_dict.get(each_16s, 'nonDBSCC')
    gnm_host = gnm_host_dict.get(each_16s)
    query_to_sample_dod[each_16s] = dict()
    matched_otu_set = query_gnm_to_subject_dict.get(each_16s, set())

    for each_otu in matched_otu_set:
        otu_sample_dict = otu_to_sample_dict_with_value.get(each_otu, dict())
        #print('%s\t%s\t%s' % (each_16s, each_otu, otu_sample_dict))

        for otu_sample in sorted(list(otu_sample_dict.keys())):
            sample_id = '.'.join(otu_sample.split('.')[:-1])
            sample_type = sample_metadata_dict.get(sample_id)
            otu_abd = otu_sample_dict[otu_sample]
            if otu_abd >= otu_table_min_pct:
                print('%s\t%s\t%s\t%s\t%s' % (each_16s, gnm_host, gnm_dbscc, otu_abd, sample_type))
    print()


# report
# for each_query_gnm in query_to_sample_type_dict:
#     gnm_dbscc = gnm_dbscc_dict.get(each_query_gnm, 'nonDBSCC')
#     gnm_host = gnm_host_dict.get(each_query_gnm)
#     current_query_sample_type_set = query_to_sample_type_dict[each_query_gnm]
#     print('%s\t%s\t%s\t%s' % (each_query_gnm, gnm_dbscc, gnm_host, current_query_sample_type_set))

########################################################################################################################

# GB_GCA_021296165.1~JAGWAW010000084.1	GCA016126025_1_16S_1	99.702	336	1	0	23	358	1	336	3.35e-178	616

# GCA016126025_1 D5
# print("query_gnm_to_subject_dict['GCA016126025_1']")
# print(query_gnm_to_subject_dict['GCA016126025_1'])

########################################################################################################################

# GCA029948415_1 D2b

# print("GCA029948415_1_16S_1	Otu000655	99.000	100	1	0	461	560	1	100	2.77e-45	180")
# print("otu_to_sample_dict_with_value['Otu000655']")
# print(otu_to_sample_dict_with_value['Otu000655'])
# print(sample_metadata_dict['HBOI12.9.VIII.09.2.001'])
# print(sample_metadata_dict['AF10.6.15'])

# {'HBOI12.9.VIII.09.2.001.1020073': 0.009, 'AF10.6.15.1182288': 0.003}
# Geodia sp.
# Ircinia fasciculata (Jun 2010)

########################################################################################################################
