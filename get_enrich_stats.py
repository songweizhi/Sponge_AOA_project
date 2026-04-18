
########################################################################################################################

# file in
enriched_in_dbscc_txt    = '/Users/songweizhi/Desktop/Sponge_r220/5_enrichment_analysis/functions_enriched_in_DBSC.txt'
enriched_in_symbiont_txt = '/Users/songweizhi/Desktop/Sponge_r220/5_enrichment_analysis/functions_enriched_in_symbiont.txt'
cog_des_txt              = '/Users/songweizhi/DB/arCOG18/arCOGdef.tab'
pwd_fun_20_tab           = '/Users/songweizhi/DB/arCOG18/fun-20.tab'
KEGG_DB_ko               = '/Users/songweizhi/DB/KEGG_2024_03_04/ko00001.keg'

# file out
table_out_arcog          = '/Users/songweizhi/Desktop/Sponge_r220/5_enrichment_analysis/arCOG_cate_stats.txt'
table_out_kegg_a         = '/Users/songweizhi/Desktop/Sponge_r220/5_enrichment_analysis/KEGG_A_stats.txt'
table_out_kegg_b         = '/Users/songweizhi/Desktop/Sponge_r220/5_enrichment_analysis/KEGG_B_stats.txt'
table_out_kegg_c         = '/Users/songweizhi/Desktop/Sponge_r220/5_enrichment_analysis/KEGG_C_stats.txt'

########################################################################################################################

# get cog_id_to_category_dict and cog_id_to_description_dict (arCOGdef.tab)
cog_category_set = set()
cog_id_to_category_dict = dict()
cog_id_to_description_dict = dict()
for each_cog in open(cog_des_txt, encoding="ISO-8859-1"):
    each_cog_split = each_cog.strip().split('\t')
    cog_id = each_cog_split[0]
    cog_cate_str = each_cog_split[1]
    cog_cate_split = [i for i in cog_cate_str]
    cog_desc = each_cog_split[3]
    cog_id_to_description_dict[cog_id] = cog_desc
    cog_id_to_category_dict[cog_id] = cog_cate_split
    for each_cate in cog_cate_split:
        cog_category_set.add(each_cate)

# get cog_category_to_description_dict (fun-20.tab)
cog_category_to_description_dict = {}
for cog_category in open(pwd_fun_20_tab):
    cog_category_split = cog_category.strip().split('\t')
    cog_category_to_description_dict[cog_category_split[0]] = cog_category_split[2]

# read in ko00001.keg
As_description_dict = {}
Bs_description_dict = {}
Cs_description_dict = {}
Ds_description_dict = {}
D2ABCD_dict = {}
current_A = ''
current_B = ''
current_C = ''
for each_line in open(KEGG_DB_ko):
    if each_line[0] in ['A', 'B', 'C', 'D']:
        each_line_split = each_line.strip().split(' ')

        if each_line[0] == 'A':
            current_A_id = each_line_split[0]
            current_A_description = ' '.join(each_line_split[1:])
            current_A = current_A_id
            As_description_dict[current_A_id] = current_A_description

        elif each_line[0] == 'B':
            if len(each_line_split) > 1:
                current_B_id = each_line_split[2]
                current_B_description = ' '.join(each_line_split[3:])
                current_B = current_B_id
                Bs_description_dict[current_B_id] = current_B_description

        elif each_line[0] == 'C':
            current_C_id = each_line_split[4]
            current_C_description = ' '.join(each_line_split[5:])
            current_C = current_C_id
            Cs_description_dict[current_C_id] = current_C_description

        elif each_line[0] == 'D':
            current_D_id = each_line_split[6]
            current_D_description = ' '.join(each_line_split[7:])
            Ds_description_dict[current_D_id] = current_D_description
            ABCD_value = 'A_%s|B_%s|C_%s|D_%s' % (current_A, current_B, current_C, current_D_id)
            if current_D_id not in D2ABCD_dict:
                D2ABCD_dict[current_D_id] = [ABCD_value]
            elif (current_D_id in D2ABCD_dict) and (ABCD_value not in D2ABCD_dict[current_D_id]):
                D2ABCD_dict[current_D_id].append(ABCD_value)

########################################################################################################################

fun_desc_dict = dict()
enriched_in_dbscc_fun_set = set()
for each in open(enriched_in_dbscc_txt):
    if not each.startswith('ID'):
        each_split = each.strip().split('\t')
        fun_id = each_split[0]
        fun_desc = each_split[5]
        enriched_in_dbscc_fun_set.add(fun_id)
        fun_desc_dict[fun_id] = fun_desc

enriched_in_symbiont_fun_set = set()
for each in open(enriched_in_symbiont_txt):
    if not each.startswith('ID'):
        each_split = each.strip().split('\t')
        fun_id = each_split[0]
        fun_desc = each_split[5]
        enriched_in_symbiont_fun_set.add(fun_id)
        fun_desc_dict[fun_id] = fun_desc

######################################################## stats 1 #######################################################

# shared_fun_set = set(enriched_in_dbsc_fun_set).intersection(enriched_in_symbiont_fun_set)
#
# for each in sorted(list(enriched_in_dbsc_fun_set)):
#     if each not in shared_fun_set:
#         print('DBSCC\t%s\t%s' % (each, fun_desc_dict[each]))
#
# for each in sorted(list(enriched_in_symbiont_fun_set)):
#     if each not in shared_fun_set:
#         print('Symbiont\t%s\t%s' % (each, fun_desc_dict[each]))
#
# for each in sorted(list(shared_fun_set)):
#     print('Shared\t%s\t%s' % (each, fun_desc_dict[each]))

######################################################## stats 2 #######################################################

all_enriched_arcog_cate_set = set()
all_enriched_kegg_a_set = set()
all_enriched_kegg_b_set = set()
all_enriched_kegg_c_set = set()

########## symbiont ##########

total_arcog_cate_num_symbiont = 0
symbiont_arcog_cate_stats_dict = dict()
kegg_a_dict_symbiont = dict()
kegg_b_dict_symbiont = dict()
kegg_c_dict_symbiont = dict()
total_num_a_symbiont = 0
total_num_b_symbiont = 0
total_num_c_symbiont = 0
for each_fun in enriched_in_symbiont_fun_set:
    if 'arCOG' in each_fun:
        fun_cate_list = cog_id_to_category_dict.get(each_fun, [])
        for each_cate in fun_cate_list:
            if each_cate not in symbiont_arcog_cate_stats_dict:
                symbiont_arcog_cate_stats_dict[each_cate] = 1
            else:
                symbiont_arcog_cate_stats_dict[each_cate] += 1
            all_enriched_arcog_cate_set.add(each_cate)
            total_arcog_cate_num_symbiont += 1
    else:
        ko_abcd_list = D2ABCD_dict[each_fun]
        a_set = set()
        b_set = set()
        c_set = set()
        for each_abcd in ko_abcd_list:
            each_abcd_split = each_abcd.split('|')
            id_a = each_abcd_split[0][2:]
            id_b = each_abcd_split[1][2:]
            id_c = each_abcd_split[2][2:]
            a_set.add(id_a)
            b_set.add(id_b)
            c_set.add(id_c)

        for each_a in a_set:
            total_num_a_symbiont += 1
            all_enriched_kegg_a_set.add(each_a)
            if each_a not in kegg_a_dict_symbiont:
                kegg_a_dict_symbiont[each_a] = 1
            else:
                kegg_a_dict_symbiont[each_a] += 1

        for each_b in b_set:
            total_num_b_symbiont += 1
            all_enriched_kegg_b_set.add(each_b)
            if each_b not in kegg_b_dict_symbiont:
                kegg_b_dict_symbiont[each_b] = 1
            else:
                kegg_b_dict_symbiont[each_b] += 1

        for each_c in c_set:
            total_num_c_symbiont += 1
            all_enriched_kegg_c_set.add(each_c)
            if each_c not in kegg_c_dict_symbiont:
                kegg_c_dict_symbiont[each_c] = 1
            else:
                kegg_c_dict_symbiont[each_c] += 1

########## DBSCC ##########

total_arcog_cate_num_dbscc = 0
dbscc_arcog_cate_stats_dict = dict()
kegg_a_dict_dbscc = dict()
kegg_b_dict_dbscc = dict()
kegg_c_dict_dbscc = dict()
total_num_a_dbscc = 0
total_num_b_dbscc = 0
total_num_c_dbscc = 0
for each_fun in enriched_in_dbscc_fun_set:
    if 'arCOG' in each_fun:
        fun_cate_list = cog_id_to_category_dict.get(each_fun, [])
        for each_cate in fun_cate_list:
            if each_cate not in dbscc_arcog_cate_stats_dict:
                dbscc_arcog_cate_stats_dict[each_cate] = 1
            else:
                dbscc_arcog_cate_stats_dict[each_cate] += 1
            all_enriched_arcog_cate_set.add(each_cate)
            total_arcog_cate_num_dbscc += 1
    else:
        ko_abcd_list = D2ABCD_dict[each_fun]
        a_set = set()
        b_set = set()
        c_set = set()
        for each_abcd in ko_abcd_list:
            each_abcd_split = each_abcd.split('|')
            id_a = each_abcd_split[0][2:]
            id_b = each_abcd_split[1][2:]
            id_c = each_abcd_split[2][2:]
            a_set.add(id_a)
            b_set.add(id_b)
            c_set.add(id_c)

        for each_a in a_set:
            total_num_a_dbscc += 1
            all_enriched_kegg_a_set.add(each_a)
            if each_a not in kegg_a_dict_dbscc:
                kegg_a_dict_dbscc[each_a] = 1
            else:
                kegg_a_dict_dbscc[each_a] += 1

        for each_b in b_set:
            total_num_b_dbscc += 1
            all_enriched_kegg_b_set.add(each_b)
            if each_b not in kegg_b_dict_dbscc:
                kegg_b_dict_dbscc[each_b] = 1
            else:
                kegg_b_dict_dbscc[each_b] += 1

        for each_c in c_set:
            total_num_c_dbscc += 1
            all_enriched_kegg_c_set.add(each_c)
            if each_c not in kegg_c_dict_dbscc:
                kegg_c_dict_dbscc[each_c] = 1
            else:
                kegg_c_dict_dbscc[each_c] += 1

########## report arcog ##########

table_out_arcog_handle = open(table_out_arcog, 'w')
table_out_arcog_handle.write('Category\tSymbiont\tDBSCC\tDescription\n')
for arcog_cate in all_enriched_arcog_cate_set:
    arcog_cate_desc         = cog_category_to_description_dict.get(arcog_cate, 'na')
    arcog_cate_num_symbiont = symbiont_arcog_cate_stats_dict.get(arcog_cate, 0)
    arcog_cate_num_dbscc    = dbscc_arcog_cate_stats_dict.get(arcog_cate, 0)
    arcog_cate_pct_symbiont = arcog_cate_num_symbiont*100/total_arcog_cate_num_symbiont
    arcog_cate_pct_dbscc    = arcog_cate_num_dbscc*100/total_arcog_cate_num_dbscc
    arcog_cate_pct_symbiont = float("{0:.2f}".format(arcog_cate_pct_symbiont))
    arcog_cate_pct_dbscc    = float("{0:.2f}".format(arcog_cate_pct_dbscc))
    table_out_arcog_handle.write('%s\t%s\t%s\t%s\n' % (arcog_cate, arcog_cate_pct_symbiont, arcog_cate_pct_dbscc, arcog_cate_desc))
table_out_arcog_handle.close()

########## report kegg ##########

table_out_kegg_a_handle = open(table_out_kegg_a, 'w')
table_out_kegg_a_handle.write('KEGG(A)\tSymbiont\tDBSCC\tDescription\n')
for each_a in all_enriched_kegg_a_set:
    a_desc          = As_description_dict[each_a]
    a_num_symbiont  = kegg_a_dict_symbiont.get(each_a, 0)
    a_num_dbscc     = kegg_a_dict_dbscc.get(each_a, 0)
    a_pct_symbiont  = a_num_symbiont*100/total_num_a_symbiont
    a_pct_dbscc     = a_num_dbscc*100/total_num_a_dbscc
    a_pct_symbiont  = float("{0:.2f}".format(a_pct_symbiont))
    a_pct_dbscc     = float("{0:.2f}".format(a_pct_dbscc))
    table_out_kegg_a_handle.write('%s\t%s\t%s\t%s\n' % (each_a, a_pct_symbiont, a_pct_dbscc, a_desc))
table_out_kegg_a_handle.close()


table_out_kegg_b_handle = open(table_out_kegg_b, 'w')
table_out_kegg_b_handle.write('KEGG(B)\tSymbiont\tDBSCC\tDescription\n')
for each_b in all_enriched_kegg_b_set:
    b_desc = Bs_description_dict[each_b]
    b_num_symbiont = kegg_b_dict_symbiont.get(each_b, 0)
    b_num_dbscc    = kegg_b_dict_dbscc.get(each_b, 0)
    b_pct_symbiont = b_num_symbiont*100/total_num_b_symbiont
    b_pct_dbscc    = b_num_dbscc*100/total_num_b_dbscc
    b_pct_symbiont = float("{0:.2f}".format(b_pct_symbiont))
    b_pct_dbscc    = float("{0:.2f}".format(b_pct_dbscc))
    table_out_kegg_b_handle.write('%s\t%s\t%s\t%s\n' % (each_b, b_pct_symbiont, b_pct_dbscc, b_desc))
table_out_kegg_b_handle.close()


table_out_kegg_c_handle = open(table_out_kegg_c, 'w')
table_out_kegg_c_handle.write('KEGG(C)\tSymbiont\tDBSCC\tDescription\n')
for each_c in all_enriched_kegg_c_set:
    c_desc = Cs_description_dict[each_c]
    c_num_symbiont = kegg_c_dict_symbiont.get(each_c, 0)
    c_num_dbscc    = kegg_c_dict_dbscc.get(each_c, 0)
    c_pct_symbiont = c_num_symbiont*100/total_num_c_symbiont
    c_pct_dbscc    = c_num_dbscc*100/total_num_c_dbscc
    c_pct_symbiont = float("{0:.2f}".format(c_pct_symbiont))
    c_pct_dbscc    = float("{0:.2f}".format(c_pct_dbscc))
    table_out_kegg_c_handle.write('%s\t%s\t%s\t%s\n' % (each_c, c_pct_symbiont, c_pct_dbscc, c_desc))
table_out_kegg_c_handle.close()

########################################################################################################################
