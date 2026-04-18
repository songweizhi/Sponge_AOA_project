import os

########################################################################################################################

wd = '/Users/songweizhi/Desktop/Sponge_r220/metadata'

# file in
gnm_id_txt                              = '%s/gnm_id_614.txt'                                           % wd
gnm_db_source_txt                       = '%s/genome_database_source.txt'                               % wd
gnm_size_txt                            = '%s/3_combined_genomes_50_5_630_size.txt'                     % wd
gnm_gc_txt                              = '%s/3_combined_genomes_50_5_630_gc.txt'                       % wd
gnm_host_txt                            = '%s/mag_host.txt'                                             % wd
gnm_taxon_txt                           = '%s/Nitrosopumilaceae_GTDB_r220_50_5_630.ar53.summary.tsv'    % wd
gnm_quality_txt                         = '%s/Nitrosopumilaceae_GTDB_r220_50_5_630_quality_report.tsv'  % wd
sponge_taxonomy_txt                     = '%s/Sponge_full_lineage_GTDB_format.txt'                      % wd
sponge_color_code_txt                   = '%s/sponge_color_code.txt'                                    % wd

# file out
meta_data_txt                           = '%s/metadata_614.txt'                                         % wd
itol_file_dir                           = wd

# ########################################################################################################################

# read in genome taxon
gnm_taxon_dict = dict()
for each_gnm in open(gnm_taxon_txt):
    if not each_gnm.startswith('user_genome\tclassification'):
        each_gnm_split  = each_gnm.strip().split('\t')
        gnm_id          = each_gnm_split[0]
        gnm_taxon       = each_gnm_split[1]
        gnm_taxon_dict[gnm_id] = gnm_taxon

# read in db genome metadata
gnm_cpl_dict = dict()
gnm_ctm_dict = dict()
for each_gnm in open(gnm_quality_txt):
    if not each_gnm.startswith('Name\tCompleteness\tContamination'):
        each_gnm_split       = each_gnm.strip().split('\t')
        gnm_id               = each_gnm_split[0]
        gnm_cpl              = each_gnm_split[1]
        gnm_ctm              = each_gnm_split[2]
        gnm_cpl_dict[gnm_id] = gnm_cpl
        gnm_ctm_dict[gnm_id] = gnm_ctm

# read in genome database source
gnm_db_source_dict = dict()
for each_gnm in open(gnm_db_source_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    gnm_db_source_dict[each_gnm_split[0]] = each_gnm_split[1]

# read in sponge taxonomy
sponge_genus_to_taxonomy_dict = dict()
for each_line in open(sponge_taxonomy_txt):
    each_line_split = each_line.strip().split(';')
    sponge_g = each_line_split[5]
    for each_r in each_line_split:
        if each_r.startswith('g__'):
            sponge_g = each_r
    tax_str = each_line.split(sponge_g)[0] + sponge_g
    sponge_genus_to_taxonomy_dict[sponge_g] = tax_str

# get gnm_gc_dict
gnm_gc_dict = dict()
for each_gnm in open(gnm_gc_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    gnm_gc_dict[each_gnm_split[0]] = float(each_gnm_split[1])

# read in host information
gnm_host_dict = dict()
for each_gnm in open(gnm_host_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    gnm_id = each_gnm_split[0]
    gnm_host = each_gnm_split[1]
    gnm_host_dict[gnm_id] = gnm_host

# read in gnm_size_txt
gnm_size_dict = dict()
for each_gnm in open(gnm_size_txt):
    if not each_gnm.startswith('Genome\t'):
        each_gnm_split  = each_gnm.strip().split('\t')
        gnm_id          = each_gnm_split[0]
        gnm_size        = each_gnm_split[1]
        gnm_size_dict[gnm_id] = gnm_size

# write out metadata.txt
meta_data_txt_handle = open(meta_data_txt, 'w')
meta_data_txt_handle.write('Genome\tSource\tCompleteness\tContamination\tSize_bp\tSize_Mbp\tSize_Mbp_adjusted_by_cpl\tGC\tTaxon\tHost\tHost_taxon\n')
for each_gnm in open(gnm_id_txt):
    gnm_id = each_gnm.strip()
    gnm_db_source = gnm_db_source_dict.get(gnm_id, 'na')
    gnm_cpl = gnm_cpl_dict.get(gnm_id, 'na')
    gnm_ctm = gnm_ctm_dict.get(gnm_id, 'na')
    gnm_size = gnm_size_dict.get(gnm_id, 'na')
    gnm_size_mbp = float("{0:.2f}".format(float(gnm_size)/(1024*1024)))
    gnm_size_norm_by_cpl = float("{0:.2f}".format(gnm_size_mbp*100/float(gnm_cpl)))
    gnm_gc = gnm_gc_dict.get(gnm_id, 'na')
    gnm_taxon = gnm_taxon_dict.get(gnm_id, 'na')
    gnm_host = gnm_host_dict.get(gnm_id, 'na')

    # get host taxon
    host_taxon = 'na'
    if gnm_host not in ['sponge', 'nonsponge', 'coral', 'na']:
        host_genus = 'g__' + gnm_host.split('_')[0]
        if 'coral' in gnm_host:
            host_genus += '(coral)'
        host_taxon = sponge_genus_to_taxonomy_dict.get(host_genus, 'na')

    meta_data_txt_handle.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (gnm_id, gnm_db_source, gnm_cpl, gnm_ctm, gnm_size, gnm_size_mbp, gnm_size_norm_by_cpl, gnm_gc, gnm_taxon, gnm_host, host_taxon))
meta_data_txt_handle.close()


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# file in
gnms_to_ignore = {}

# file out
gnm_to_host_g_txt       = '%s/gnm_host_1_g.txt'        % itol_file_dir
gnm_to_host_f_txt       = '%s/gnm_host_2_f.txt'        % itol_file_dir
gnm_to_host_o_txt       = '%s/gnm_host_3_o.txt'        % itol_file_dir
gnm_to_host_sc_txt      = '%s/gnm_host_4_sc.txt'       % itol_file_dir
gnm_to_host_c_txt       = '%s/gnm_host_5_c.txt'        % itol_file_dir
gnm_to_host_g_txt_itol  = '%s/iTOL_gnm_host_1_g.txt'   % itol_file_dir
gnm_to_host_f_txt_itol  = '%s/iTOL_gnm_host_2_f.txt'   % itol_file_dir
gnm_to_host_o_txt_itol  = '%s/iTOL_gnm_host_3_o.txt'   % itol_file_dir
gnm_to_host_sc_txt_itol = '%s/iTOL_gnm_host_4_sc.txt'  % itol_file_dir
gnm_to_host_c_txt_itol  = '%s/iTOL_gnm_host_5_c.txt'   % itol_file_dir

gnm_to_host_g_txt_handle = open(gnm_to_host_g_txt, 'w')
gnm_to_host_f_txt_handle = open(gnm_to_host_f_txt, 'w')
gnm_to_host_o_txt_handle = open(gnm_to_host_o_txt, 'w')
gnm_to_host_sc_txt_handle = open(gnm_to_host_sc_txt, 'w')
gnm_to_host_c_txt_handle = open(gnm_to_host_c_txt, 'w')
col_index = {}
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]

        if gnm_id not in gnms_to_ignore:
            host_species         = each_gnm_split[col_index['Host']]
            host_taxon_str_split = each_gnm_split[col_index['Host_taxon']].split(';')
            print(host_species)
            # write out host taxon
            if host_species == 'sponge':
                gnm_to_host_g_txt_handle.write('%s\t%s\n'  % (gnm_id, 'sponge'))
                gnm_to_host_f_txt_handle.write('%s\t%s\n'  % (gnm_id, 'sponge'))
                gnm_to_host_o_txt_handle.write('%s\t%s\n'  % (gnm_id, 'sponge'))
                gnm_to_host_sc_txt_handle.write('%s\t%s\n' % (gnm_id, 'sponge'))
                gnm_to_host_c_txt_handle.write('%s\t%s\n'  % (gnm_id, 'sponge'))
            elif host_species == 'coral':
                gnm_to_host_g_txt_handle.write('%s\t%s\n'  % (gnm_id, 'coral'))
                gnm_to_host_f_txt_handle.write('%s\t%s\n'  % (gnm_id, 'coral'))
                gnm_to_host_o_txt_handle.write('%s\t%s\n'  % (gnm_id, 'coral'))
                gnm_to_host_sc_txt_handle.write('%s\t%s\n' % (gnm_id, 'coral'))
                gnm_to_host_c_txt_handle.write('%s\t%s\n'  % (gnm_id, 'coral'))
            elif host_species == 'nonsponge':
                gnm_to_host_g_txt_handle.write('%s\t%s\n'  % (gnm_id, 'nonsponge'))
                gnm_to_host_f_txt_handle.write('%s\t%s\n'  % (gnm_id, 'nonsponge'))
                gnm_to_host_o_txt_handle.write('%s\t%s\n'  % (gnm_id, 'nonsponge'))
                gnm_to_host_sc_txt_handle.write('%s\t%s\n' % (gnm_id, 'nonsponge'))
                gnm_to_host_c_txt_handle.write('%s\t%s\n'  % (gnm_id, 'nonsponge'))
            elif host_species == 'na':
                gnm_to_host_g_txt_handle.write('%s\t%s\n'  % (gnm_id, 'na'))
                gnm_to_host_f_txt_handle.write('%s\t%s\n'  % (gnm_id, 'na'))
                gnm_to_host_o_txt_handle.write('%s\t%s\n'  % (gnm_id, 'na'))
                gnm_to_host_sc_txt_handle.write('%s\t%s\n' % (gnm_id, 'na'))
                gnm_to_host_c_txt_handle.write('%s\t%s\n'  % (gnm_id, 'na'))
            else:
                for each_host_r in host_taxon_str_split:
                    if each_host_r.startswith('g__'):
                        gnm_to_host_g_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('f__'):
                        gnm_to_host_f_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('o__'):
                        gnm_to_host_o_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('sc__'):
                        gnm_to_host_sc_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('c__'):
                        gnm_to_host_c_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
gnm_to_host_g_txt_handle.close()
gnm_to_host_f_txt_handle.close()
gnm_to_host_o_txt_handle.close()
gnm_to_host_sc_txt_handle.close()
gnm_to_host_c_txt_handle.close()

biosak_cmd_host_g  = 'BioSAK iTOL -ColorStrip -lg %s -gc %s -lt Host_g -o %s'  % (gnm_to_host_g_txt,  sponge_color_code_txt, gnm_to_host_g_txt_itol)
biosak_cmd_host_f  = 'BioSAK iTOL -ColorStrip -lg %s -gc %s -lt Host_f -o %s'  % (gnm_to_host_f_txt,  sponge_color_code_txt, gnm_to_host_f_txt_itol)
biosak_cmd_host_o  = 'BioSAK iTOL -ColorStrip -lg %s -gc %s -lt Host_o -o %s'  % (gnm_to_host_o_txt,  sponge_color_code_txt, gnm_to_host_o_txt_itol)
biosak_cmd_host_sc = 'BioSAK iTOL -ColorStrip -lg %s -gc %s -lt Host_sc -o %s' % (gnm_to_host_sc_txt, sponge_color_code_txt, gnm_to_host_sc_txt_itol)
biosak_cmd_host_c  = 'BioSAK iTOL -ColorStrip -lg %s -gc %s -lt Host_c -o %s'  % (gnm_to_host_c_txt,  sponge_color_code_txt, gnm_to_host_c_txt_itol)

# os.system(biosak_cmd_host_g)
# os.system(biosak_cmd_host_f)
# os.system(biosak_cmd_host_o)
# os.system(biosak_cmd_host_sc)
# os.system(biosak_cmd_host_c)
