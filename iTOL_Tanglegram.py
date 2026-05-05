import os
from ete3 import Tree


def tanglegram(symbiont_meta_data_txt, host_tree_file, color_code_symbiont_txt, color_code_host_txt, leaf_label_rank_str, color_link_by_host, color_link_by_symbiont, color_link_by_host_rank, connection_host_tax, min_symbiont_per_host, connect_sym_info_col, connect_sym_interested_grp, op_dir):

    ############################################### define output file name ###############################################

    leaf_rank_str = 'p,c,sc,o,f,g'

    if connect_sym_interested_grp is not None:
        connect_sym_interested_grp_renamed = connect_sym_interested_grp.replace(',', '_')

    # define the name of output iTOL file
    suffix_str = ''
    if (connect_sym_interested_grp is not None) and (connection_host_tax is None):
        suffix_str = connect_sym_interested_grp_renamed
    elif (connect_sym_interested_grp is None) and (connection_host_tax is not None):
        suffix_str = connection_host_tax
    elif (connect_sym_interested_grp is not None) and (connection_host_tax is not None):
        suffix_str = '%s__%s' % (connect_sym_interested_grp_renamed, connection_host_tax)

    if suffix_str == '':
        itol_tanglegram_txt = '%s/iTOL_Tanglegram_min%s_All.txt'    % (op_dir, min_symbiont_per_host)
    else:
        itol_tanglegram_txt = '%s/iTOL_Tanglegram_min%s_%s.txt'     % (op_dir, min_symbiont_per_host, suffix_str)

    label_txt               = '%s/label.txt'                        % op_dir
    label_txt_itol          = '%s/iTOL_label.txt'                   % op_dir

    ########################################################################################################################

    # tanglegram tree position
    tree_pan_h                  = 3000
    tree_pan_v                  = 150

    # tanglegram tree scaling
    tree_scale_h                = 1
    tree_scale_v                = 8

    # tanglegram tree label
    show_leaf_label             = 1
    leaf_label_size_factor      = 6
    leaf_label_shift            = 0
    leaf_label_align            = 'left'

    # linkages
    max_link_line_width         = 8
    connection_margin_left      = 25
    connection_margin_right     = 3

    # colorstrip
    show_column_labels          = 0
    show_strips                 = 1
    strip_width                 = 150
    strip_spacing               = 10
    show_strip_labels           = 0
    strip_label_position        = 'center'
    strip_label_size_factor     = 1
    strip_label_rotation        = 0

    ########################################################################################################################

    if connect_sym_info_col in ['GTDB_Taxon_r232']:
        connect_sym_info_col_is_tax = True
    if connect_sym_info_col in ['DBSCC']:
        connect_sym_info_col_is_tax = False

    if connection_host_tax is not None:
        connection_host_tax_list        = connection_host_tax.split(',')
    leaf_rank_list                      = leaf_rank_str.split(',')
    leaf_label_rank_list                = leaf_label_rank_str.split(',')

    rename_tree_leaves = False
    if leaf_label_rank_str is not None:
        rename_tree_leaves = True

    symbiont_color_code_dict = dict()
    if os.path.isfile(color_code_symbiont_txt):
        for each_line in open(color_code_symbiont_txt):
            each_line_split = each_line.strip().split()
            symbiont_color_code_dict[each_line_split[0]] = each_line_split[1]

    host_color_code_dict = dict()
    if os.path.isfile(color_code_host_txt):
        for each_line in open(color_code_host_txt):
            each_line_split = each_line.strip().split()
            host_color_code_dict[each_line_split[0]] = each_line_split[1]

    ##########################################

    gnm_tax_dict = dict()
    host_taxon_dict = dict()
    association_dict = dict()
    host_taxon_grp_dict = dict()
    color_connection_leaf_grp_dict = dict()
    association_dict_host_to_symbiont = dict()
    col_index = dict()
    for each_gnm in open(symbiont_meta_data_txt):
        each_gnm_split = each_gnm.strip().split('\t')
        if each_gnm.startswith('Genome\t'):
            col_index = {key: i for i, key in enumerate(each_gnm_split)}
        else:
            gnm_id                  = each_gnm_split[col_index['Genome']]
            connection_info_col_str = each_gnm_split[col_index[connect_sym_info_col]]
            gnm_tax                 = each_gnm_split[col_index['GTDB_Taxon_r232']]
            host_taxon_str          = each_gnm_split[col_index['Host_Taxon']]
            host_taxon_str_split    = host_taxon_str.split(';')
            host_taxon_dict[gnm_id] = host_taxon_str

            #################### symbiont part ####################

            interested_symbiont_for_connection = False
            if connect_sym_info_col_is_tax is False:
                if connect_sym_interested_grp is None:
                    interested_symbiont_for_connection = True
                else:
                    if connection_info_col_str in connect_sym_interested_grp.split(','):
                        interested_symbiont_for_connection = True
            else:
                # treat as tax str, code to be added
                gnm_tax_split = connection_info_col_str.split(';')
                for each_sr in gnm_tax_split:
                    if connect_sym_interested_grp is None:
                        interested_symbiont_for_connection = True
                    else:
                        if each_sr in connect_sym_interested_grp.split(','):
                            interested_symbiont_for_connection = True

            ###################### host part ######################

            interested_host_for_connection = False
            if connection_host_tax is None:
                interested_host_for_connection = True
            else:
                for each_hr in host_taxon_str_split:
                    if each_hr in connection_host_tax_list:
                        interested_host_for_connection = True

            ######### add to dict if both parties belong to the interested groups #########

            if gnm_id.startswith('JL'):
                jl_sample_id = gnm_id.split('_bin')[0]
                if (interested_symbiont_for_connection is True) and (interested_host_for_connection is True):
                    association_dict[gnm_id] = jl_sample_id

                    if jl_sample_id not in association_dict_host_to_symbiont:
                        association_dict_host_to_symbiont[jl_sample_id] = set()
                    association_dict_host_to_symbiont[jl_sample_id].add(gnm_id)

            host_g  = 'g__'
            host_f  = 'f__'
            host_o  = 'o__'
            host_sc = 'sc__'
            host_c  = 'c__'
            for each_hr in host_taxon_str_split:
                if each_hr.startswith('g__'):
                    host_g = each_hr
                if each_hr.startswith('f__'):
                    host_f = each_hr
                if each_hr.startswith('o__'):
                    host_o = each_hr
                if each_hr.startswith('sc__'):
                    host_sc = each_hr
                if each_hr.startswith('c__'):
                    host_c = each_hr

            if (host_g != 'g__') and (host_o != 'o__'):
                host_taxon_grp_dict[host_g] = host_o

            if host_g != 'g__':
                if (interested_symbiont_for_connection is True) and (interested_host_for_connection is True):
                    association_dict[gnm_id] = host_g
                    if host_g not in association_dict_host_to_symbiont:
                        association_dict_host_to_symbiont[host_g] = set()
                    association_dict_host_to_symbiont[host_g].add(gnm_id)

            gnm_g = 'g__'
            for each_r in gnm_tax.split(';'):
                if each_r.startswith('g__'):
                    gnm_g = each_r
            gnm_tax_dict[gnm_id] = gnm_g

            # write out color_connection_leaf_grp_txt
            g_to_use = ''
            if color_link_by_host_rank == 'f':
                g_to_use = host_f
            elif color_link_by_host_rank == 'o':
                g_to_use = host_o
            elif color_link_by_host_rank == 'sc':
                g_to_use = host_sc
            elif color_link_by_host_rank == 'c':
                g_to_use = host_c

            if gnm_id.startswith('JL'):
                jl_sample_id = gnm_id.split('_bin')[0]
                color_connection_leaf_grp_dict[jl_sample_id] = g_to_use
            if host_g != 'g__':
                color_connection_leaf_grp_dict[host_g] = g_to_use

            ################################################################################################################

    host_to_ignore = set()
    for each_host in association_dict_host_to_symbiont:
        if len(association_dict_host_to_symbiont[each_host]) < min_symbiont_per_host:
            host_to_ignore.add(each_host)

    association_dict_filtered = dict()
    for each_association in association_dict:
        if association_dict[each_association] not in host_to_ignore:
            association_dict_filtered[each_association] = association_dict[each_association]

    # get tax_max_len_by_rank_dict
    tax_max_len_by_rank_dict = dict()
    for each_id in host_taxon_dict:
        id_taxon_split = host_taxon_dict[each_id].split(';')
        if len(id_taxon_split) > 1:
            for each_r in id_taxon_split:
                rank_alphabet = each_r.split('__')[0]
                if rank_alphabet not in tax_max_len_by_rank_dict:
                    tax_max_len_by_rank_dict[rank_alphabet] = 0
                if len(each_r) > tax_max_len_by_rank_dict[rank_alphabet]:
                    tax_max_len_by_rank_dict[rank_alphabet] = len(each_r)

    # get leaf rename dict
    rename_leaf_dict = dict()
    for each_id in host_taxon_dict:
        id_taxon = host_taxon_dict[each_id]
        id_taxon_split = id_taxon.split(';')
        if len(id_taxon_split) > 1:
            needed_key_list = []
            needed_rank_list = []
            for each_r in id_taxon_split:
                rank_alphabet = each_r.split('__')[0]
                if rank_alphabet in leaf_label_rank_list:
                    needed_rank_list.append(each_r)
                if rank_alphabet in leaf_rank_list:
                    needed_key_list.append(each_r)

            if each_id.startswith('JL'):
                jl_sample = each_id.split('_bin')[0]
                needed_key_list.append(jl_sample)

            for needed_key in needed_key_list:
                current_needed_rank_list = []
                ignore_the_rest = False
                for each_needed_rank in needed_rank_list:
                    if ignore_the_rest is False:
                        if each_needed_rank != needed_key:
                            current_needed_rank_list.append(each_needed_rank)
                        else:
                            ignore_the_rest = True

                current_needed_rank_list_equal_len = [('%s%s' % (i, '_' * (tax_max_len_by_rank_dict[i.split('__')[0]] - len(i)))) for i in current_needed_rank_list]
                rename_leaf_dict[needed_key] = '%s__%s' % (';'.join(current_needed_rank_list_equal_len), needed_key)
            needed_rank_list_equal_len = [('%s%s' % (i, '_' * (tax_max_len_by_rank_dict[i.split('__')[0]] - len(i)))) for i in needed_rank_list]
            rename_leaf_dict[each_id] = '%s__%s' % (';'.join(needed_rank_list_equal_len), each_id)

    label_txt_handle = open(label_txt, 'w')
    for i in rename_leaf_dict:
        label_txt_handle.write('%s\t%s\n' % (i, rename_leaf_dict[i]))
    label_txt_handle.close()

    biosak_cmd_genus_label = 'TreeSAK iTOL -Labels -ll %s -o %s' % (label_txt, label_txt_itol)
    os.system(biosak_cmd_genus_label)
    os.system('rm %s' % label_txt)

    tanglegram_tree_str = ''
    if rename_tree_leaves is False:
        with open(host_tree_file, 'r') as f:
            tanglegram_tree_str = f.readline()
    else:
        # rename tree leaves
        t = Tree(host_tree_file, format=0)
        for leaf in t:
            leaf_name_new = rename_leaf_dict.get(leaf.name, leaf.name)
            leaf.name = leaf_name_new
        tanglegram_tree_str = t.write(format=9)

    itol_tanglegram_txt_handle = open(itol_tanglegram_txt, 'w')
    itol_tanglegram_txt_handle.write('DATASET_TANGLEGRAM\nSEPARATOR TAB\n\n')
    if suffix_str == '':
        itol_tanglegram_txt_handle.write('DATASET_LABEL\tTanglegram_All\nCOLOR\t#00ff00\n\n')
    else:
        itol_tanglegram_txt_handle.write('DATASET_LABEL\tTanglegram_%s\nCOLOR\t#00ff00\n\n' % suffix_str)

    itol_tanglegram_txt_handle.write('TANGLEGRAM_TREE\n%s\nEND_TANGLEGRAM_TREE\n\n'     % tanglegram_tree_str)
    itol_tanglegram_txt_handle.write('\n')

    #  Attributes for connection lines
    itol_tanglegram_txt_handle.write('# Connection lines\n')
    itol_tanglegram_txt_handle.write('CONNECTION_CURVE\t0\n')
    itol_tanglegram_txt_handle.write('MAXIMUM_LINE_WIDTH\t%s\n'                                     % max_link_line_width)
    itol_tanglegram_txt_handle.write('CONNECTION_MARGIN_LEFT\t%s\nCONNECTION_MARGIN_RIGHT\t%s\n'    % (connection_margin_left, connection_margin_right))
    itol_tanglegram_txt_handle.write('\n')

    # Position of the tanglegram tree
    itol_tanglegram_txt_handle.write('# Move the tanglegram tree horizontally and/or vertically\n')
    itol_tanglegram_txt_handle.write('TREE_PAN_H\t%s\nTREE_PAN_V\t%s\n'     % (tree_pan_h, tree_pan_v))
    itol_tanglegram_txt_handle.write('\n')

    # Scaling of the tanglegram tree
    itol_tanglegram_txt_handle.write('# Tanglegram tree scaling factors, horizontal and vertical\n')
    itol_tanglegram_txt_handle.write('TREE_SCALE_H\t%s\nTREE_SCALE_V\t%s\n' % (tree_scale_h, tree_scale_v))
    itol_tanglegram_txt_handle.write('\n')

    # Tanglegram tree leaf labels
    itol_tanglegram_txt_handle.write('# Tanglegram tree label\n')
    itol_tanglegram_txt_handle.write('SHOW_LABELS\t%s\nSIZE_FACTOR\t%s\nLABEL_SHIFT\t%s\nLABEL_ALIGN\t%s\n' % (show_leaf_label, leaf_label_size_factor, leaf_label_shift, leaf_label_align))
    itol_tanglegram_txt_handle.write('\n')

    # Specify attributes for colorstrip
    itol_tanglegram_txt_handle.write('# Attributes for colorstrip\n')
    itol_tanglegram_txt_handle.write('COLUMN_LABELS\tlabel_for_column_index_1\tlabel_for_column_index_2\tlabel_for_column_index_3\n')
    itol_tanglegram_txt_handle.write('SHOW_COLUMN_LABELS\t%s\n'         % show_column_labels)
    itol_tanglegram_txt_handle.write('SHOW_STRIPS\t%s\n'                % show_strips)
    itol_tanglegram_txt_handle.write('STRIP_WIDTH\t%s\n'                % strip_width)
    itol_tanglegram_txt_handle.write('STRIP_SPACING\t%s\n'              % strip_spacing)
    itol_tanglegram_txt_handle.write('SHOW_STRIP_LABELS\t%s\n'          % show_strip_labels)
    itol_tanglegram_txt_handle.write('STRIP_LABEL_POSITION\t%s\n'       % strip_label_position)
    itol_tanglegram_txt_handle.write('STRIP_LABEL_SIZE_FACTOR\t%s\n'    % strip_label_size_factor)
    itol_tanglegram_txt_handle.write('STRIP_LABEL_ROTATION\t%s\n'       % strip_label_rotation)
    itol_tanglegram_txt_handle.write('\n')

    ########## DATA section ##########

    itol_tanglegram_txt_handle.write('DATA\n')
    itol_tanglegram_txt_handle.write('#connect\tMAIN_TREE_NODE_ID\tTANGLEGRAM_TREE_NODE_ID\tWIDTH\tCOLOR\tSTYLE\tLABEL\n')
    itol_tanglegram_txt_handle.write('#colorstrip\tCOLUMN_INDEX\tTANGLEGRAM_TREE_NODE_ID\tCOLOR LABEL\n')
    itol_tanglegram_txt_handle.write('#style\tTANGLEGRAM_TREE_NODE_ID\tTYPE\tWHAT\tCOLOR\tWIDTH_OR_SIZE_FACTOR\tSTYLE\tBACKGROUND_COLOR\n')
    itol_tanglegram_txt_handle.write('#symbol\tTANGLEGRAM_TREE_NODE_ID\tSYMBOL\tSIZE\tCOLOR\tFILL\tPOSITION\tLABEL\n')
    itol_tanglegram_txt_handle.write('\n')

    ########## connection section ##########

    # connect\tMAIN_TREE_NODE_ID\tTANGLEGRAM_TREE_NODE_ID\tWIDTH\tCOLOR\tSTYLE\tLABEL
    itol_tanglegram_txt_handle.write('# Data for the connect section\n')
    for each_leaf in association_dict_filtered:
        leaf_host           = association_dict_filtered[each_leaf]
        leaf_host_renamed   = rename_leaf_dict.get(leaf_host, leaf_host)
        leaf_host_renamed   = leaf_host_renamed.replace(';', '_')
        leaf_l_grp          = color_connection_leaf_grp_dict.get(leaf_host, '')
        color_by_host       = host_color_code_dict.get(leaf_l_grp, 'black')
        symbiont_tax        = gnm_tax_dict.get(each_leaf, 'g__')
        color_by_symbiont   = symbiont_color_code_dict.get(symbiont_tax, 'black')

        # link color
        link_color_to_use = 'black'
        if color_link_by_symbiont is True:
            link_color_to_use = color_by_symbiont
        elif color_link_by_host is True:
            link_color_to_use = color_by_host
        itol_tanglegram_txt_handle.write('connect\t%s\t%s\t3\t%s\tnormal\ttest\n' % (each_leaf, leaf_host_renamed, link_color_to_use))
    itol_tanglegram_txt_handle.write('\n')

    ########## colorstrip section ##########

    # colorstrip\tCOLUMN_INDEX\tTANGLEGRAM_TREE_NODE_ID\tCOLOR LABEL
    itol_tanglegram_txt_handle.write('# Data for the colorstrip section\n')
    for each_leaf in color_connection_leaf_grp_dict:
        leaf_renamed      = rename_leaf_dict.get(each_leaf, each_leaf)
        leaf_renamed = leaf_renamed.replace(';', '_')
        leaf_grp_str = color_connection_leaf_grp_dict[each_leaf]
        leaf_grp_str_split = leaf_grp_str.split(';')
        col_index = 1
        for each_g in leaf_grp_str_split:
            g_color = host_color_code_dict.get(each_g, '#F8F9F9')
            str_to_write = 'colorstrip\t%s\t%s\t%s\t%s' % (col_index, leaf_renamed, g_color, each_g)
            itol_tanglegram_txt_handle.write(str_to_write + '\n')
            col_index += 1
    itol_tanglegram_txt_handle.close()


########################################################################################################################

metadata_update_date                = '20260423'

# file in
meta_data_txt                       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_%s.txt'           % metadata_update_date
tree_file                           = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_COI_iden95_g_representatives_JL_wd_WoRMS/Sponge_phylogeny_Maria_topo_genus_level_18S_COI.tree'
color_code_genome_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_symbiont.txt'
color_code_sponge_txt               = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/color_code_sponge.txt'
leaf_label_rank_str                 = 'c,sc,o,f'        # or None
color_link_by_host                  = True              # True or False
color_link_by_host_rank             = 'o'
color_link_by_symbiont              = False             # True or False
min_symbiont_per_host               = 0
force_create_op_dir                 = True

# plot links by symbioint DBSCC
connect_sym_info_col                = 'DBSCC'       # GTDB_Taxon_r232 or DBSCC
connect_sym_interested_dbscc_list   = [None, 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11a', 'D11b', 'D11c', 'D11d', 'D11a,D11b,D11c,D11d']

# plot links by symbioint taxa
connect_sym_info_col                = 'GTDB_Taxon_r232'       # GTDB_Taxon_r232 or DBSCC
connect_sym_interested_taxon_list   = ['g__Nitrosopumilus']

# plot links by host group
connection_host_tax_list            = [None, 'c__Hexactinellida', 'o__Dictyoceratida', 'o__Homosclerophorida', 'o__Lyssacinosida', 'o__Tetractinellida', 'o__Verongiida', 'f__Ianthellidae', 'g__Agelas', 'g__Coscinoderma', 'g__Stylissa']

# file out
op_dir                              = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_%s_iTOL_Tanglegram'     % metadata_update_date

########################################################################################################################

# create op_dir
if os.path.isdir(op_dir) is True:
    if force_create_op_dir is True:
        os.system('rm -r %s' % op_dir)
    else:
        print('Output folder detected, program exited!')
        exit()
os.system('mkdir %s' % op_dir)


for connect_sym_interested_dbscc in connect_sym_interested_dbscc_list:
    print('Processing %s' % connect_sym_interested_dbscc)
    tanglegram(meta_data_txt, tree_file, color_code_genome_txt, color_code_sponge_txt, leaf_label_rank_str, color_link_by_host, color_link_by_symbiont, color_link_by_host_rank, None, min_symbiont_per_host, 'DBSCC', connect_sym_interested_dbscc, op_dir)

for connect_sym_interested_taxon in connect_sym_interested_taxon_list:
    print('Processing %s' % connect_sym_interested_taxon)
    tanglegram(meta_data_txt, tree_file, color_code_genome_txt, color_code_sponge_txt, leaf_label_rank_str, color_link_by_host, color_link_by_symbiont, color_link_by_host_rank, None, min_symbiont_per_host, 'GTDB_Taxon_r232', connect_sym_interested_taxon, op_dir)

for connection_host_tax in connection_host_tax_list:
    print('Processing %s' % connection_host_tax)
    tanglegram(meta_data_txt, tree_file, color_code_genome_txt, color_code_sponge_txt, leaf_label_rank_str, color_link_by_host, color_link_by_symbiont, color_link_by_host_rank, connection_host_tax, min_symbiont_per_host, connect_sym_info_col, None, op_dir)
