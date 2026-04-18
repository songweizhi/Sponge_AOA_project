
########################################################################################################################

# file in
gnm_size_txt                = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/5_combined_genomes_407_size.txt'
gnm_quality_txt             = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/5_combined_genomes_407_quality.txt'
gnm_taxon_txt               = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/5_combined_genomes_407.ar53.summary.tsv'
meta_table_old              = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/2_metadata/0_metadata_final.txt'
drep97_representatives_txt  = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/5_combined_genomes_dRep97_wd/dereplicated_genomes.txt'

# file out
meta_table_new              = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/5_combined_genomes_407_metadata.txt'

########################################################################################################################

drep97_representative_gnm_set = set()
for each_line in open(drep97_representatives_txt):
    drep97_representative_gnm_set.add(each_line.strip())

gnm_cpl_dict = dict()
gnm_ctm_dict = dict()
gnm_hete_dict = dict()
for each_line in open(gnm_quality_txt):
    each_line_split = each_line.strip().split('\t')
    if not each_line.startswith('Genome\t'):
        gnm_cpl_dict[each_line_split[0]]  = each_line_split[1]
        gnm_ctm_dict[each_line_split[0]]  = each_line_split[2]
        gnm_hete_dict[each_line_split[0]] = each_line_split[3]

gnm_taxon_dict = dict()
for each_gnm in open(gnm_taxon_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    gnm_taxon_dict[each_gnm_split[0]] = each_gnm_split[1]

gnm_size_dict = dict()
for each_gnm in open(gnm_size_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    gnm_size_dict[each_gnm_split[0]] = each_gnm_split[1]

col_index = dict()
mag_host_dict = dict()
mag_alias_dict = dict()
mag_source_dict = dict()
mag_biosample_dict = dict()
mag_host_taxon_dict = dict()
for each_line in open(meta_table_old):
    each_line_split = each_line.strip().split('\t')
    if each_line.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_line_split)}
    else:
        gnm_id = each_line_split[col_index['Genome']]
        gnm_id = gnm_id.replace('GCA_', 'GCA').replace('GCF_', 'GCF')
        gnm_id = gnm_id.replace('.1', '_1').replace('.2', '_2')
        mag_host_dict[gnm_id]       = each_line_split[col_index['Host']]
        mag_alias_dict[gnm_id]      = each_line_split[col_index['Alias']]
        mag_source_dict[gnm_id]     = each_line_split[col_index['Source']]
        mag_biosample_dict[gnm_id]  = each_line_split[col_index['Biosample']]
        mag_host_taxon_dict[gnm_id] = each_line_split[col_index['Host_taxon']]

# write out table
sponge_mag_num = 0
meta_table_new_handle = open(meta_table_new, 'w')
meta_table_new_handle.write('Genome\tAlias\tSource\tBiosample\tSize\tCompleteness\tContamination\tHeterogeneity\tdRep97_representative\tTaxon\tLifestyle\tHost\tHost_taxon\n')
for each_gnm in sorted(list(gnm_cpl_dict.keys())):

    gnm_host       = mag_host_dict.get(each_gnm, 'na')
    gnm_alias      = mag_alias_dict.get(each_gnm, 'na')
    gnm_source     = mag_source_dict.get(each_gnm, 'na')
    gnm_cpl        = gnm_cpl_dict.get(each_gnm, 'na')
    gnm_ctm        = gnm_ctm_dict.get(each_gnm, 'na')
    gnm_hete       = gnm_hete_dict.get(each_gnm, 'na')
    gnm_taxon      = gnm_taxon_dict.get(each_gnm, 'na')
    gnm_size       = gnm_size_dict.get(each_gnm, 'na')
    gnm_biosample  = mag_biosample_dict.get(each_gnm, 'na')
    gnm_host_taxon = mag_host_taxon_dict.get(each_gnm, 'na')

    drep97_representative_gnm = '0'
    if each_gnm in drep97_representative_gnm_set:
        drep97_representative_gnm = '1'

    gnm_lifestyle = 'na'
    if gnm_host == 'nonsponge':
        gnm_lifestyle = 'nonsponge'
    elif gnm_host == 'na':
        gnm_lifestyle = 'na'
    elif gnm_host == 'sponge':
        gnm_lifestyle = 'sponge'
    else:
        gnm_lifestyle = 'sponge'

    str_to_write = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (each_gnm,
                                                                gnm_alias,
                                                                gnm_source,
                                                                gnm_biosample,
                                                                gnm_size,
                                                                gnm_cpl,
                                                                gnm_ctm,
                                                                gnm_hete,
                                                                drep97_representative_gnm,
                                                                gnm_taxon,
                                                                gnm_lifestyle,
                                                                gnm_host,
                                                                gnm_host_taxon)

    meta_table_new_handle.write(str_to_write + '\n')
meta_table_new_handle.close()

