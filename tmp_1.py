
meta_data_txt                       = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/metadata_614.txt'
gnm_id_406_txt                      = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/gnm_id_406.txt'
DBSCC_genomes_txt                   = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/DBSCC_genomes.txt'

enrichment_analysis_grouping_txt    = '/Users/songweizhi/Desktop/dRep99_406_grouping_DBSCC_vs_freeliving.txt'


DBSCC_dict = dict()
for gnm in open(DBSCC_genomes_txt):
    gnm_split = gnm.strip().split('\t')
    DBSCC_dict[gnm_split[0]] = gnm_split[1]

gnm_id_406_set =set()
for line in open(gnm_id_406_txt):
    gnm_id_406_set.add(line.strip())


enrichment_analysis_grouping_txt_handle = open(enrichment_analysis_grouping_txt, 'w')
n = 0
col_index = dict()
nonDBSCC_symbiont_set = set()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_406_set:
            host_species         = each_gnm_split[col_index['Host']]
            host_type            = each_gnm_split[col_index['Host_type']]
            host_taxon_str_split = each_gnm_split[col_index['Host_taxon']].split(';')
            if gnm_id in DBSCC_dict:
                enrichment_analysis_grouping_txt_handle.write('%s\t%s\n' % (gnm_id, 'DBSCC'))
            else:
                if host_type == 'nonsponge':
                    enrichment_analysis_grouping_txt_handle.write('%s\t%s\n' % (gnm_id, 'freeliving'))
                else:
                    print('%s\t%s\tignored, nonDBSCC symbiont' % (gnm_id, host_type))
            n += 1
enrichment_analysis_grouping_txt_handle.close()





