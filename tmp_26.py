
# file in
meta_data_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'


col_index = dict()
cols_to_include_in_label_dict = dict()
cols_to_include_in_label_max_len_dict = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        host_species            = each_gnm_split[col_index['Host_Species']]
        host_group              = each_gnm_split[col_index['Host_Group']]
        host_taxon_str_split    = each_gnm_split[col_index['Host_Taxon']].split(';')
        gnm_size                = each_gnm_split[col_index['Size_Mbp_adjusted_by_cpl']]
        gnm_dbscc               = each_gnm_split[col_index['DBSCC']]
        gnm_deepsea             = each_gnm_split[col_index['Deepsea_2']]
        gnm_taxon               = each_gnm_split[col_index['GTDB_Taxon_r232']]
        gnm_completeness        = each_gnm_split[col_index['Completeness']]
        gnm_gc                  = each_gnm_split[col_index['GC']]

        if 'f__Nitrosopumilaceae' in gnm_taxon:
            print(gnm_taxon)
