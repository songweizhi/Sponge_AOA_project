
meta_data_txt            = '/Users/songweizhi/Desktop/Sponge_r220/metadata/metadata_614.txt'
genus_stats_txt          = '/Users/songweizhi/Desktop/Sponge_r220/1_manuscript/Figures/Fig1_genus_stats.txt'
genus_stats_txt_symbiont = '/Users/songweizhi/Desktop/Sponge_r220/1_manuscript/Figures/Fig1_genus_stats_symbiont.txt'


genus_stats_dict = dict()
symbiont_stats_dict = dict()
col_index = {}
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id                  = each_gnm_split[col_index['Genome']]
        gnm_taxon               = each_gnm_split[col_index['Taxon']]
        gnm_genus               = gnm_taxon.split(';')[5]
        host_species            = each_gnm_split[col_index['Host']]
        host_taxon_str_split    = each_gnm_split[col_index['Host_taxon']].split(';')

        if gnm_genus not in genus_stats_dict:
            genus_stats_dict[gnm_genus] = 1
        else:
            genus_stats_dict[gnm_genus] += 1

        if host_species not in ['nonsponge', 'na', 'coral', 'Porites_lutea(coral)', 'Isopora_palifera(coral)']:
            if gnm_genus not in symbiont_stats_dict:
                symbiont_stats_dict[gnm_genus] = 1
            else:
                symbiont_stats_dict[gnm_genus] += 1

genus_stats_txt_handle = open(genus_stats_txt, 'w')
for each in genus_stats_dict:
    genus_stats_txt_handle.write('%s\t%s\n' % (each, genus_stats_dict[each]))
genus_stats_txt_handle.close()

genus_stats_txt_symbiont_handle = open(genus_stats_txt_symbiont, 'w')
for each in symbiont_stats_dict:
    genus_stats_txt_symbiont_handle.write('%s\t%s\n' % (each, symbiont_stats_dict[each]))
genus_stats_txt_symbiont_handle.close()

