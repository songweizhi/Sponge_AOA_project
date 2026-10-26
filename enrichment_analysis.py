import os

# needed files
wd                      = '/Users/songweizhi/Desktop/Sponge_r226/11_Functional_enrichment_analysis'
distinct_AOA_groups_txt = '/Users/songweizhi/Desktop/Sponge_r226/11_Functional_enrichment_analysis/distinct_AOA_groups.txt'
meta_data_txt           = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260423.txt'


grp_to_gnm_dict = dict()
interested_gnm_set = set()
for each_line in open(distinct_AOA_groups_txt):
    each_line_split = each_line.strip().split('\t')
    gnm_id = each_line_split[0]
    grp_id = each_line_split[1]
    interested_gnm_set.add(gnm_id)
    if grp_id not in grp_to_gnm_dict:
        grp_to_gnm_dict[grp_id] = set()
    grp_to_gnm_dict[grp_id].add(gnm_id)

all_symbioint_set = set()
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id                  = each_gnm_split[col_index['Genome']]
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
            if host_group in ['Sponge']:
                all_symbioint_set.add(gnm_id)

for each_grp in grp_to_gnm_dict:
    grp_member = grp_to_gnm_dict[each_grp]
    op_txt = '%s/%s.txt' % (wd, each_grp)
    op_txt_handle = open(op_txt, 'w')
    for each_gnm in grp_member:
        op_txt_handle.write('%s\t%s\n'% (each_gnm, each_grp))
    for each_sym in all_symbioint_set:
        if each_sym not in grp_member:
            op_txt_handle.write('%s\t%s\n' % (each_sym, 'The_rest_symbionts'))
    op_txt_handle.close()

    enrich_cmd_cog  = 'BioSAK enrich -bc -f -i annotation_arCOG -x txt -g %s.txt -p %s_arCOG -o functional_enrichment_%s_arCOG' % (each_grp, each_grp, each_grp)
    enrich_cmd_kegg = 'BioSAK enrich -bc -f -i annotation_KEGG  -x txt -g %s.txt -p %s_KEGG  -o functional_enrichment_%s_KEGG'  % (each_grp, each_grp, each_grp)
    print(enrich_cmd_cog)
    print(enrich_cmd_kegg)
