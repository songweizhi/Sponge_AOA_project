import os

########################################################################################################################

# file in
mag_host_txt            = '/Users/songweizhi/Desktop/Sponge_r220/metadata/mag_host.txt'
color_code_txt_sponge   = '/Users/songweizhi/Desktop/Sponge_r220/metadata/sponge_taxon_color_code.txt'

# file out
host_g_txt              = '/Users/songweizhi/Desktop/Sponge_r220/metadata/mag_host_genus.txt'
host_g_txt_itol         = '/Users/songweizhi/Desktop/Sponge_r220/metadata/iTOL_host_genus.txt'

########################################################################################################################

# write out
host_g_txt_handle = open(host_g_txt, 'w')
line_index = 0
col_index = dict()
gnm_to_genus_dict = dict()
max_genus_len = 0
for each_line in open(mag_host_txt):
    each_line_split = each_line.strip().split('\t')
    gnm_id          = each_line_split[0]
    host_species    = each_line_split[1]
    if host_species in ['sponge', 'nonsponge', 'na']:
        host_genus = host_species
    else:
        host_genus = 'g__%s' % host_species.split('_')[0]
    host_g_txt_handle.write('%s\t%s\n' % (gnm_id, host_genus))
host_g_txt_handle.close()

os.system('BioSAK iTOL -ColorStrip -lg %s -o %s -gc %s -lt Sponge_Genus'    % (host_g_txt, host_g_txt_itol, color_code_txt_sponge))


########################################################################################################################
########################################################################################################################
########################################################################################################################


import os

########################################################################################################################

# file in
mag_taxon_txt               = '/Users/songweizhi/Desktop/Sponge_r220/metadata/Nitrosopumilaceae_GTDB_r220_50_5_630.ar53.summary.tsv'
color_code_genus_txt        = '/Users/songweizhi/Desktop/Sponge_r220/metadata/genome_taxon_color_code.txt'

# file out
gnm_full_tax_txt            = '/Users/songweizhi/Desktop/Sponge_r220/metadata/for_iTOL_MAG_taxon.txt'
gnm_full_tax_txt_itol       = '/Users/songweizhi/Desktop/Sponge_r220/metadata/iTOL_MAG_rename_label.txt'
gnm_genus_txt               = '/Users/songweizhi/Desktop/Sponge_r220/metadata/for_iTOL_genus.txt'
gnm_genus_txt_itol          = '/Users/songweizhi/Desktop/Sponge_r220/metadata/iTOL_MAG_genus.txt'

########################################################################################################################

# write out
gnm_genus_txt_handle = open(gnm_genus_txt, 'w')
line_index = 0
col_index = dict()
gnm_to_genus_dict = dict()
max_genus_len = 0
for each_line in open(mag_taxon_txt):
    each_line_split = each_line.strip().split('\t')
    if line_index == 0:
        col_index = {key: i for i, key in enumerate(each_line_split)}
        line_index += 1
    else:
        gnm_id = each_line_split[col_index['user_genome']]
        gnm_taxon = each_line_split[col_index['classification']]
        gnm_taxon_split = gnm_taxon.split(';')
        gnm_genus = gnm_taxon_split[5]
        gnm_genus_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_genus))
        gnm_to_genus_dict[gnm_id] = gnm_genus
        if len(gnm_genus) > max_genus_len:
            max_genus_len = len(gnm_genus)
gnm_genus_txt_handle.close()


gnm_full_tax_txt_handle = open(gnm_full_tax_txt, 'w')
for each_gnm in gnm_to_genus_dict:
    gnm_genus = gnm_to_genus_dict[each_gnm]
    gnm_genus = gnm_genus + '_'*(max_genus_len-len(gnm_genus))
    gnm_full_tax_txt_handle.write('%s\t%s___%s\n' % (each_gnm, gnm_genus, each_gnm))
gnm_full_tax_txt_handle.close()

# get iTOL files
os.system('BioSAK iTOL -ColorRange -lg %s -o %s -gc %s -lt Genus'           % (gnm_genus_txt, gnm_genus_txt_itol, color_code_genus_txt))
os.system('BioSAK iTOL -Labels -ll %s -o %s'                                % (gnm_full_tax_txt, gnm_full_tax_txt_itol))
