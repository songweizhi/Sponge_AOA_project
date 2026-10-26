
########################################################################################################################

meta_data_txt = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'
gnm_id_txt    = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_r232_2383.txt'

########################################################################################################################

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

habitat_set= set()
habitat_dict_f = dict()
habitat_dict_Nitrosopumilaceae = dict()

life_style_dict_f = dict()
life_style_dict_Nitrosopumilaceae = dict()
host_species_set = set()
genus_to_host_species_dict = dict()
host_grp_dict = dict()
genus_set = set()
genus_stats_dict_all = dict()
genus_stats_dict_sym = dict()
col_index = dict()

d7_host_set = set()
d8_host_set = set()
gnm_contributor_set = set()
marine_num_before_symbiosis = 0
total_num_before_symbiosis = 0
marine_num_after_symbiosis = 0
total_num_after_symbiosis = 0
David_Ngugi = 0
Shan_Zhang = 0
Michelle_Allen = 0
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if  gnm_id in gnm_id_set:
            host_species         = each_gnm_split[col_index['Host_Species']]
            host_grp             = each_gnm_split[col_index['Host_Group']]
            host_taxon_str       = each_gnm_split[col_index['Host_Taxon']]
            host_taxon_str_split = host_taxon_str.split(';')
            gnm_size             = each_gnm_split[col_index['Size_Mbp_adjusted_by_cpl']]
            gc_content           = each_gnm_split[col_index['GC']]
            gnm_taxon            = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_taxon_r232       = each_gnm_split[col_index['GTDB_Taxon_r232']]
            gnm_habitat_1        = each_gnm_split[col_index['Habitat_1']]
            gnm_habitat_2        = each_gnm_split[col_index['Habitat_2']]
            gnm_habitat_3        = each_gnm_split[col_index['Habitat_3']]
            gnm_habitat_4        = each_gnm_split[col_index['Habitat_4']]
            gnm_dbscc            = each_gnm_split[col_index['DBSCC']]
            gnm_contributor      = each_gnm_split[col_index['Contributor']]
            gnm_cpl              = each_gnm_split[col_index['Completeness']]
            gnm_ctm              = each_gnm_split[col_index['Contamination']]
