import os


def colorstrip_col(metadata_txt, interested_col, interested_colorstrip_col_txt, interested_colorstrip_col_txt_itol, color_code_txt):
    interested_colorstrip_col_txt_handle = open(interested_colorstrip_col_txt, 'w')
    col_index = dict()
    for each_gnm in open(metadata_txt):
        each_gnm_split = each_gnm.strip().split('\t')
        if each_gnm.startswith('Genome\t'):
            col_index = {key: i for i, key in enumerate(each_gnm_split)}
        else:
            gnm_id = each_gnm_split[col_index['Genome']]
            if gnm_id in gnm_id_set:
                interested_colorstrip_col_txt_handle.write(
                    '%s\t%s\n' % (gnm_id, each_gnm_split[col_index[interested_col]]))
    interested_colorstrip_col_txt_handle.close()

    if color_code_txt is None:
        treesak_cmd_interested_colorstrip_col = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -lt %s -o %s' % (
            interested_colorstrip_col_txt, interested_col, interested_colorstrip_col_txt_itol)
    else:
        treesak_cmd_interested_colorstrip_col = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt %s -o %s' % (
            interested_colorstrip_col_txt, color_code_txt, interested_col, interested_colorstrip_col_txt_itol)
    os.system(treesak_cmd_interested_colorstrip_col)


########################################################################################################################

metadata_update_date        = '20260423'

# file in
meta_data_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_%s.txt'           % metadata_update_date
color_code_sponge_txt       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_sponge.txt'
color_code_genome_txt       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_symbiont.txt'
color_code_habitat_txt      = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_habitat.txt'
color_code_dbscc_txt        = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_DBSCCs.txt'
color_code_host_cate_txt    = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_Host_Group.txt'
cols_to_include_in_label    = 'habitat_for_labelling,Habitat_Depth,Location'
cols_to_include_in_label    = 'habitat_for_labelling,Host_Species,Location'
fixed_taxon_label_list      = ['f__Nitrososphaeraceae', 'f__Nitrosocaldaceae', 'f__UBA213']
include_host_tax_in_label   = False
colorstrip_cols             = 'Contributor,Source'
force_create_op_dir         = True

# 2395
gnm_id_txt                  = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_r232_2383.txt'
itol_file_dir               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_%s_iTOL_2383'     % metadata_update_date

########################################################################################################################

# create op_dir
if os.path.isdir(itol_file_dir) is True:
    if force_create_op_dir is True:
        os.system('rm -r %s' % itol_file_dir)
    else:
        print('Output folder detected, program exited!')
        exit()
os.system('mkdir %s'     % itol_file_dir)
os.system('mkdir %s/tmp' % itol_file_dir)

gnm_genus_txt               = '%s/tmp/gnm_genus_Range.txt'          % itol_file_dir
gnm_family_txt              = '%s/tmp/gnm_family_Range.txt'         % itol_file_dir
gnm_label_txt               = '%s/tmp/gnm_Label.txt'                % itol_file_dir
gnm_label_txt_long          = '%s/tmp/gnm_Label_long.txt'           % itol_file_dir
gnm_to_host_s_txt           = '%s/tmp/gnm_host_0_s.txt'             % itol_file_dir
gnm_to_host_g_txt           = '%s/tmp/gnm_host_1_g.txt'             % itol_file_dir
gnm_to_host_f_txt           = '%s/tmp/gnm_host_2_f.txt'             % itol_file_dir
gnm_to_host_o_txt           = '%s/tmp/gnm_host_3_o.txt'             % itol_file_dir
gnm_to_host_sc_txt          = '%s/tmp/gnm_host_4_sc.txt'            % itol_file_dir
gnm_to_host_c_txt           = '%s/tmp/gnm_host_5_c.txt'             % itol_file_dir
gnm_completeness_txt        = '%s/tmp/gnm_completeness.txt'         % itol_file_dir
gnm_host_group_txt          = '%s/tmp/gnm_host_group.txt'           % itol_file_dir
gnm_size_txt                = '%s/tmp/gnm_size.txt'                 % itol_file_dir
gnm_gc_txt                  = '%s/tmp/gnm_gc.txt'                   % itol_file_dir
gnm_habitat_1_txt           = '%s/tmp/gnm_habitat_1.txt'            % itol_file_dir
gnm_habitat_2_txt           = '%s/tmp/gnm_habitat_2.txt'            % itol_file_dir
gnm_habitat_3_txt           = '%s/tmp/gnm_habitat_3.txt'            % itol_file_dir
gnm_habitat_4_txt           = '%s/tmp/gnm_habitat_4.txt'            % itol_file_dir
gnm_dbscc_txt               = '%s/tmp/gnm_DBSCC.txt'                % itol_file_dir
gnm_dbscc_genus_txt         = '%s/tmp/gnm_DBSCC_and_genus.txt'      % itol_file_dir
gnm_deepsea_txt             = '%s/tmp/gnm_deepsea_Binary.txt'       % itol_file_dir
gnm_deepsea_txt_for_strip   = '%s/tmp/gnm_deepsea.txt'              % itol_file_dir

gnm_genus_colorclade_itol   = '%s/iTOL_gnm_genus_ColorClade.txt'    % itol_file_dir
gnm_genus_colorlabel_itol   = '%s/iTOL_gnm_genus_ColorLabel.txt'    % itol_file_dir
gnm_genus_txt_itol          = '%s/iTOL_gnm_genus_Range.txt'         % itol_file_dir
gnm_family_txt_itol         = '%s/iTOL_gnm_family_Range.txt'        % itol_file_dir
gnm_label_txt_itol          = '%s/iTOL_gnm_Label.txt'               % itol_file_dir
gnm_label_txt_itol_long     = '%s/iTOL_gnm_Label_long.txt'          % itol_file_dir
gnm_to_host_s_txt_itol      = '%s/iTOL_gnm_host_0_s.txt'            % itol_file_dir
gnm_to_host_g_txt_itol      = '%s/iTOL_gnm_host_1_g.txt'            % itol_file_dir
gnm_to_host_f_txt_itol      = '%s/iTOL_gnm_host_2_f.txt'            % itol_file_dir
gnm_to_host_o_txt_itol      = '%s/iTOL_gnm_host_3_o.txt'            % itol_file_dir
gnm_to_host_sc_txt_itol     = '%s/iTOL_gnm_host_4_sc.txt'           % itol_file_dir
gnm_to_host_c_txt_itol      = '%s/iTOL_gnm_host_5_c.txt'            % itol_file_dir
gnm_completeness_txt_itol   = '%s/iTOL_gnm_completeness.txt'        % itol_file_dir
gnm_host_group_txt_itol     = '%s/iTOL_gnm_host_group.txt'          % itol_file_dir
gnm_size_txt_itol           = '%s/iTOL_genome_size.txt'             % itol_file_dir
gnm_gc_txt_itol             = '%s/iTOL_GC_content.txt'              % itol_file_dir
gnm_habitat_1_txt_itol      = '%s/iTOL_habitat_1.txt'               % itol_file_dir
gnm_habitat_2_txt_itol      = '%s/iTOL_habitat_2.txt'               % itol_file_dir
gnm_habitat_3_txt_itol      = '%s/iTOL_habitat_3.txt'               % itol_file_dir
gnm_habitat_4_txt_itol      = '%s/iTOL_habitat_4.txt'               % itol_file_dir
gnm_dbscc_txt_itol          = '%s/iTOL_DBSCC.txt'                   % itol_file_dir
gnm_deepsea_txt_itol        = '%s/iTOL_Deepsea_Binary.txt'          % itol_file_dir
gnm_deepsea_txt_itol_strip  = '%s/iTOL_Deepsea.txt'                 % itol_file_dir

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])

############################################ colorstrip interested columns #############################################

colorstrip_col_list = colorstrip_cols.split(',')

for interested_col in colorstrip_col_list:
    interested_col_txt              = '%s/tmp/%s.txt'  % (itol_file_dir, interested_col)
    interested_col_txt_itol         = '%s/iTOL_%s.txt' % (itol_file_dir, interested_col)
    interested_col_color_code_txt   = None
    colorstrip_col(meta_data_txt, interested_col, interested_col_txt, interested_col_txt_itol, interested_col_color_code_txt)

########################################################################################################################

# write out
gnm_genus_txt_handle                = open(gnm_genus_txt, 'w')
gnm_family_txt_handle               = open(gnm_family_txt, 'w')
gnm_to_host_s_txt_handle            = open(gnm_to_host_s_txt, 'w')
gnm_to_host_g_txt_handle            = open(gnm_to_host_g_txt, 'w')
gnm_to_host_f_txt_handle            = open(gnm_to_host_f_txt, 'w')
gnm_to_host_o_txt_handle            = open(gnm_to_host_o_txt, 'w')
gnm_to_host_sc_txt_handle           = open(gnm_to_host_sc_txt, 'w')
gnm_to_host_c_txt_handle            = open(gnm_to_host_c_txt, 'w')
gnm_completeness_txt_handle         = open(gnm_completeness_txt, 'w')
gnm_host_group_txt_handle           = open(gnm_host_group_txt, 'w')
gnm_size_txt_handle                 = open(gnm_size_txt, 'w')
gnm_gc_txt_handle                   = open(gnm_gc_txt, 'w')
gnm_habitat_1_txt_handle            = open(gnm_habitat_1_txt, 'w')
gnm_habitat_2_txt_handle            = open(gnm_habitat_2_txt, 'w')
gnm_habitat_3_txt_handle            = open(gnm_habitat_3_txt, 'w')
gnm_habitat_4_txt_handle            = open(gnm_habitat_4_txt, 'w')
gnm_dbscc_txt_handle                = open(gnm_dbscc_txt, 'w')
gnm_dbscc_genus_txt_handle          = open(gnm_dbscc_genus_txt, 'w')
gnm_deepsea_txt_handle              = open(gnm_deepsea_txt, 'w')
gnm_deepsea_txt_for_strip_handle    = open(gnm_deepsea_txt_for_strip, 'w')
gnm_to_genus_dict                   = dict()
gnm_to_family_dict                  = dict()
gnm_to_host_taxa_dict               = dict()
max_genus_len = 0
max_family_len = 0
max_gnm_name_len = 0
col_index = dict()
cols_to_include_in_label_dict = dict()
cols_to_include_in_label_max_len_dict = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            host_species            = each_gnm_split[col_index['Host_Species']]
            host_group              = each_gnm_split[col_index['Host_Group']]
            host_taxon_str_split    = each_gnm_split[col_index['Host_Taxon']].split(';')
            gnm_size                = each_gnm_split[col_index['Size_Mbp_adjusted_by_cpl']]
            gnm_dbscc               = each_gnm_split[col_index['DBSCC']]
            gnm_deepsea             = each_gnm_split[col_index['Deepsea_2']]
            gnm_taxon               = each_gnm_split[col_index['GTDB_Taxon_r232']]
            gnm_completeness        = each_gnm_split[col_index['Completeness']]
            gnm_gc                  = each_gnm_split[col_index['GC']]

            if gnm_deepsea in ['Deep-sea', 'deep-sea']:
                gnm_deepsea_txt_handle.write(gnm_id + '\n')
                gnm_deepsea_txt_for_strip_handle.write('%s\tDeep-sea\n' % gnm_id)

            if cols_to_include_in_label != '':
                cols_to_include_in_label_value_list = []
                for each_col in cols_to_include_in_label.split(','):
                    each_col_value = each_gnm_split[col_index[each_col]]
                    if '"' in each_col_value:
                        each_col_value = each_col_value.replace('"', '')

                    if each_col not in cols_to_include_in_label_max_len_dict:
                        cols_to_include_in_label_max_len_dict[each_col] = 0
                    if len(each_col_value) > cols_to_include_in_label_max_len_dict[each_col]:
                        cols_to_include_in_label_max_len_dict[each_col] = len(each_col_value)

                    cols_to_include_in_label_value_list.append(each_col_value)
                cols_to_include_in_label_dict[gnm_id] = cols_to_include_in_label_value_list

            gnm_to_host_taxa_dict[gnm_id] = host_taxon_str_split
            if len(gnm_id) > max_gnm_name_len:
                max_gnm_name_len = len(gnm_id)

            gnm_host_group_txt_handle.write('%s\t%s\n' % (gnm_id, host_group))

            # write out genome taxon
            gnm_taxon_split = gnm_taxon.split(';')
            gnm_family = gnm_taxon_split[4]
            gnm_genus  = gnm_taxon_split[5]
            gnm_to_family_dict[gnm_id] = gnm_family
            gnm_family_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_family))

            if len(gnm_family) > max_family_len:
                max_family_len = len(gnm_family)

            tax_str_to_use = ''
            for fixed_taxon_label in fixed_taxon_label_list:
                if ('%s;'% fixed_taxon_label) in gnm_taxon:
                    tax_str_to_use = fixed_taxon_label

            if tax_str_to_use != '':
                gnm_genus_txt_handle.write('%s\t%s\n' % (gnm_id, tax_str_to_use))
                gnm_to_genus_dict[gnm_id] = tax_str_to_use
                if len(tax_str_to_use) > max_genus_len:
                    max_genus_len = len(tax_str_to_use)
            else:
                gnm_genus_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_genus))
                gnm_to_genus_dict[gnm_id] = gnm_genus
                if len(gnm_genus) > max_genus_len:
                    max_genus_len = len(gnm_genus)

            # write out DBSCC
            if gnm_dbscc != 'na':
                gnm_dbscc_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_dbscc))
                gnm_dbscc_genus_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_dbscc))
            else:
                gnm_dbscc_genus_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_genus))

            # write out size, completeness
            gnm_completeness_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_completeness))
            gnm_size_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_size))
            gnm_gc_txt_handle.write('%s\t%s\n' % (gnm_id, (float(gnm_gc)-25)))
            gnm_habitat_1_txt_handle.write('%s\t%s\n' % (gnm_id, each_gnm_split[col_index['Habitat_1']]))
            gnm_habitat_2_txt_handle.write('%s\t%s\n' % (gnm_id, each_gnm_split[col_index['Habitat_2']]))
            gnm_habitat_3_txt_handle.write('%s\t%s\n' % (gnm_id, each_gnm_split[col_index['Habitat_3']]))
            gnm_habitat_4_txt_handle.write('%s\t%s\n' % (gnm_id, each_gnm_split[col_index['Habitat_4']]))

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
                    if each_host_r.startswith('s__'):
                        gnm_to_host_s_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('g__'):
                        gnm_to_host_g_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('f__'):
                        gnm_to_host_f_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('o__'):
                        gnm_to_host_o_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('sc__'):
                        gnm_to_host_sc_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
                    elif each_host_r.startswith('c__'):
                        gnm_to_host_c_txt_handle.write('%s\t%s\n' % (gnm_id, each_host_r))
gnm_genus_txt_handle.close()
gnm_family_txt_handle.close()
gnm_to_host_s_txt_handle.close()
gnm_to_host_g_txt_handle.close()
gnm_to_host_f_txt_handle.close()
gnm_to_host_o_txt_handle.close()
gnm_to_host_sc_txt_handle.close()
gnm_to_host_c_txt_handle.close()
gnm_completeness_txt_handle.close()
gnm_host_group_txt_handle.close()
gnm_size_txt_handle.close()
gnm_gc_txt_handle.close()
gnm_habitat_1_txt_handle.close()
gnm_habitat_2_txt_handle.close()
gnm_habitat_3_txt_handle.close()
gnm_habitat_4_txt_handle.close()
gnm_dbscc_txt_handle.close()
gnm_dbscc_genus_txt_handle.close()
gnm_deepsea_txt_handle.close()
gnm_deepsea_txt_for_strip_handle.close()

gnm_to_host_p_dict = dict()
gnm_to_host_c_dict = dict()
gnm_to_host_sc_dict = dict()
gnm_to_host_o_dict = dict()
gnm_to_host_f_dict = dict()
gnm_to_host_g_dict = dict()
gnm_to_host_s_dict = dict()
max_taxon_name_len_dict = dict()
for each_g in gnm_to_host_taxa_dict:
    host_tax_list = gnm_to_host_taxa_dict[each_g]
    if len(host_tax_list) > 1:
        for each_r in host_tax_list:
            if each_r.startswith('p__'):
                name_len = len(each_r)
                if 'p' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['p'] = name_len
                if name_len > max_taxon_name_len_dict['p']:
                    max_taxon_name_len_dict['p'] = name_len
                if each_r != 'p__':
                    gnm_to_host_p_dict[each_g] = each_r
            elif each_r.startswith('c__'):
                name_len = len(each_r)
                if 'c' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['c'] = name_len
                if name_len > max_taxon_name_len_dict['c']:
                    max_taxon_name_len_dict['c'] = name_len
                if each_r != 'c__':
                    gnm_to_host_c_dict[each_g] = each_r
            elif each_r.startswith('sc__'):
                name_len = len(each_r)
                if 'sc' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['sc'] = name_len
                if name_len > max_taxon_name_len_dict['sc']:
                    max_taxon_name_len_dict['sc'] = name_len
                if each_r != 'sc__':
                    gnm_to_host_sc_dict[each_g] = each_r
            elif each_r.startswith('o__'):
                name_len = len(each_r)
                if 'o' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['o'] = name_len
                if name_len > max_taxon_name_len_dict['o']:
                    max_taxon_name_len_dict['o'] = name_len
                if each_r != 'o__':
                    gnm_to_host_o_dict[each_g] = each_r
            elif each_r.startswith('f__'):
                name_len = len(each_r)
                if 'f' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['f'] = name_len
                if name_len > max_taxon_name_len_dict['f']:
                    max_taxon_name_len_dict['f'] = name_len
                if each_r != 'f__':
                    gnm_to_host_f_dict[each_g] = each_r
            elif each_r.startswith('g__'):
                name_len = len(each_r)
                if 'g' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['g'] = name_len
                if name_len > max_taxon_name_len_dict['g']:
                    max_taxon_name_len_dict['g'] = name_len
                if each_r != 'g__':
                    gnm_to_host_g_dict[each_g] = each_r
            elif each_r.startswith('s__'):
                name_len = len(each_r)
                if 's' not in max_taxon_name_len_dict:
                    max_taxon_name_len_dict['s'] = name_len
                if name_len > max_taxon_name_len_dict['s']:
                    max_taxon_name_len_dict['s'] = name_len
                if each_r != 's__':
                    gnm_to_host_s_dict[each_g] = each_r

cols_to_include_in_label_max_len_list = []
if cols_to_include_in_label != '':
    cols_to_include_in_label_max_len_list = [cols_to_include_in_label_max_len_dict[i] for i in cols_to_include_in_label.split(',')]

# write out gnm_label_txt
gnm_label_txt_handle = open(gnm_label_txt, 'w')
for interested_gnm in gnm_to_genus_dict:
    current_genus = gnm_to_genus_dict[interested_gnm]
    current_genus = current_genus + '_' * (max_genus_len - len(current_genus))
    interested_gnm_to_write = interested_gnm + '_' * (max_gnm_name_len - len(interested_gnm))
    str_to_write = '%s\t%s___%s' % (interested_gnm, current_genus, interested_gnm)
    gnm_label_txt_handle.write(str_to_write + '\n')
gnm_label_txt_handle.close()

# write out the long label
gnm_label_txt_long_handle = open(gnm_label_txt_long, 'w')
for interested_gnm in gnm_to_genus_dict:
    current_genus = gnm_to_genus_dict[interested_gnm]
    current_genus = current_genus + '_' * (max_genus_len - len(current_genus))
    interested_gnm_to_write = interested_gnm + '_' * (max_gnm_name_len - len(interested_gnm))
    str_to_write = '%s\t%s___%s' % (interested_gnm, current_genus, interested_gnm)
    str_to_write_same_len = '%s\t%s___%s' % (interested_gnm, current_genus, interested_gnm_to_write)
    if include_host_tax_in_label is True:
        host_p  = gnm_to_host_p_dict.get(interested_gnm, '')
        host_c  = gnm_to_host_c_dict.get(interested_gnm, '')
        host_sc = gnm_to_host_sc_dict.get(interested_gnm, '')
        host_o  = gnm_to_host_o_dict.get(interested_gnm, '')
        host_f  = gnm_to_host_f_dict.get(interested_gnm, '')
        host_g  = gnm_to_host_g_dict.get(interested_gnm, '')
        host_s  = gnm_to_host_s_dict.get(interested_gnm, '')
        host_p  = host_p  + '_' * (max_taxon_name_len_dict['p']  - len(host_p))
        host_c  = host_c  + '_' * (max_taxon_name_len_dict['c']  - len(host_c))
        host_sc = host_sc + '_' * (max_taxon_name_len_dict['sc'] - len(host_sc))
        host_o  = host_o  + '_' * (max_taxon_name_len_dict['o']  - len(host_o))
        host_f  = host_f  + '_' * (max_taxon_name_len_dict['f']  - len(host_f))
        host_g  = host_g  + '_' * (max_taxon_name_len_dict['g']  - len(host_g))
        host_s  = host_s  + '_' * (max_taxon_name_len_dict['s']  - len(host_s))
        str_to_write          = '%s__;%s;%s;%s;%s;%s;%s' % (str_to_write,          host_c, host_sc, host_o, host_f, host_g, host_s)
        str_to_write_same_len = '%s__;%s;%s;%s;%s;%s;%s' % (str_to_write_same_len, host_c, host_sc, host_o, host_f, host_g, host_s)

    if cols_to_include_in_label != '':
        same_len_label_list = []
        for (col_value, col_value_max_len) in zip(cols_to_include_in_label_dict[interested_gnm],cols_to_include_in_label_max_len_list):
            col_value  = col_value  + '_' * (col_value_max_len  - len(col_value))
            same_len_label_list.append(col_value)
        same_len_label_str = '__'.join(same_len_label_list)
        str_to_write = '%s__%s' % (str_to_write, same_len_label_str)
        str_to_write_same_len = '%s__%s' % (str_to_write_same_len, same_len_label_str)
    gnm_label_txt_long_handle.write(str_to_write_same_len + '\n')
gnm_label_txt_long_handle.close()

# run BioSAK
biosak_cmd_genus_range          = 'TreeSAK iTOL -ColorRange -lg %s -o %s -gc %s -lt Genus'                                                      % (gnm_genus_txt, gnm_genus_txt_itol, color_code_genome_txt)
biosak_cmd_family_range         = 'TreeSAK iTOL -ColorRange -lg %s -o %s -gc %s -lt Family'                                                     % (gnm_family_txt, gnm_family_txt_itol, color_code_genome_txt)
biosak_cmd_genus_label          = 'TreeSAK iTOL -Labels -ll %s -o %s'                                                                           % (gnm_label_txt, gnm_label_txt_itol)
biosak_cmd_genus_label_long     = 'TreeSAK iTOL -Labels -ll %s -o %s'                                                                           % (gnm_label_txt_long, gnm_label_txt_itol_long)
biosak_cmd_deepsea_strip        = 'TreeSAK iTOL -ColorStrip -strip_width 100 -hide_legend -lg %s -gc %s -lt "Deep-sea" -o %s'                   % (gnm_deepsea_txt_for_strip,  color_code_habitat_txt, gnm_deepsea_txt_itol_strip)
biosak_cmd_host_s               = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt "Host Species" -o %s'   % (gnm_to_host_s_txt,  color_code_sponge_txt, gnm_to_host_s_txt_itol)
biosak_cmd_host_g               = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt "Host genus" -o %s'     % (gnm_to_host_g_txt,  color_code_sponge_txt, gnm_to_host_g_txt_itol)
biosak_cmd_host_f               = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt "Host family" -o %s'    % (gnm_to_host_f_txt,  color_code_sponge_txt, gnm_to_host_f_txt_itol)
biosak_cmd_host_o               = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt "Host order" -o %s'     % (gnm_to_host_o_txt,  color_code_sponge_txt, gnm_to_host_o_txt_itol)
biosak_cmd_host_sc              = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt "Host subclass" -o %s'  % (gnm_to_host_sc_txt, color_code_sponge_txt, gnm_to_host_sc_txt_itol)
biosak_cmd_host_c               = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt "Host class" -o %s'     % (gnm_to_host_c_txt,  color_code_sponge_txt, gnm_to_host_c_txt_itol)
biosak_cmd_host_group           = 'TreeSAK iTOL -ColorStrip -strip_width 150 -lg %s -gc %s -lt "HostGroup" -o %s'                               % (gnm_host_group_txt,  color_code_host_cate_txt, gnm_host_group_txt_itol)
biosak_cmd_habitat_1            = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt habitat_1 -o %s'        % (gnm_habitat_1_txt,  color_code_habitat_txt, gnm_habitat_1_txt_itol)
biosak_cmd_habitat_2            = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt habitat_2 -o %s'        % (gnm_habitat_2_txt,  color_code_habitat_txt, gnm_habitat_2_txt_itol)
biosak_cmd_habitat_3            = 'TreeSAK iTOL -ColorStrip -strip_width 300 -hide_legend -show_label -lg %s -gc %s -lt habitat_3 -o %s'        % (gnm_habitat_3_txt,  color_code_habitat_txt, gnm_habitat_3_txt_itol)
biosak_cmd_habitat_4            = 'TreeSAK iTOL -ColorStrip -strip_width 300 -show_label -lg %s -gc %s -lt habitat_4 -o %s'                     % (gnm_habitat_4_txt,  color_code_habitat_txt, gnm_habitat_4_txt_itol)
biosak_cmd_dbscc                = 'TreeSAK iTOL -ColorStrip -show_label -hide_legend -lg %s -gc %s -lt DBSCC -o %s'                             % (gnm_dbscc_txt,  color_code_dbscc_txt, gnm_dbscc_txt_itol)
biosak_cmd_cpl                  = 'TreeSAK iTOL -SimpleBar -lv %s -scale 0-25-50-75-100 -lt Completeness -o %s'                                 % (gnm_completeness_txt, gnm_completeness_txt_itol)
biosak_cmd_size                 = 'TreeSAK iTOL -SimpleBar -lv %s -lt Genome_size -scale 0-1-2-3 -o %s'                                         % (gnm_size_txt, gnm_size_txt_itol)
biosak_cmd_gc                   = 'TreeSAK iTOL -SimpleBar -lv %s -lt GC_content -scale 25-50-75 -o %s'                                   % (gnm_gc_txt, gnm_gc_txt_itol)
biosak_cmd_deepsea              = 'TreeSAK iTOL -BinaryID -id %s -lt Deep-sea -BinaryColor "#2B7FFF" -o %s'                                     % (gnm_deepsea_txt, gnm_deepsea_txt_itol)
biosak_cmd_genus_color_clade    = 'TreeSAK iTOL -ColorClade -lg %s -gc %s -o %s'                                                                % (gnm_genus_txt, color_code_genome_txt, gnm_genus_colorclade_itol)
biosak_cmd_genus_color_label    = 'TreeSAK iTOL -ColorLabel -lg %s -gc %s -o %s'                                                                % (gnm_genus_txt, color_code_genome_txt, gnm_genus_colorlabel_itol)

os.system(biosak_cmd_host_group)
os.system(biosak_cmd_genus_label)
os.system(biosak_cmd_genus_label_long)
os.system(biosak_cmd_deepsea_strip)
os.system(biosak_cmd_dbscc)
os.system(biosak_cmd_genus_color_clade)
os.system(biosak_cmd_genus_color_label)
os.system(biosak_cmd_habitat_1)
os.system(biosak_cmd_habitat_2)
os.system(biosak_cmd_habitat_3)
os.system(biosak_cmd_habitat_4)
os.system(biosak_cmd_genus_range)
os.system(biosak_cmd_family_range)
os.system(biosak_cmd_host_s)
os.system(biosak_cmd_host_g)
os.system(biosak_cmd_host_f)
os.system(biosak_cmd_host_o)
os.system(biosak_cmd_host_sc)
os.system(biosak_cmd_host_c)
os.system(biosak_cmd_size)
os.system(biosak_cmd_gc)
os.system(biosak_cmd_cpl)
