import os


########################################################################################################################

fun_id_list = ['arCOG08676', 'arCOG08675', 'arCOG08699', 'arCOG10586']
# arCOG08676	AmoA
# arCOG08675	AmoB
# arCOG08699	AmoC
# arCOG10586	AmoX

dir_in      = '/scratch/PI/ocessongwz/Sponge_r226/get_AOA_taxa/gnms_280_faa_arCOG_wd'
dir_out     = '/scratch/PI/ocessongwz/Sponge_r226/get_AOA_taxa/gnms_280_AmoABCX_stats'

########################################################################################################################

sub_dir_list = next(os.walk(dir_in))[1]

arcog_id_to_gene_dict = dict()
for sub_dir in sub_dir_list:
    gnm_id = sub_dir[:-9]
    query_to_cog_txt = '%s/%s/%s_query_to_cog.txt' % (dir_in, sub_dir, gnm_id)
    for each_line in open(query_to_cog_txt):
        each_line_split = each_line.strip().split('\t')
        if len(each_line_split) == 4:
            gene_id  = each_line_split[0]
            arcog_id = each_line_split[1]
            if arcog_id in fun_id_list:
                if arcog_id not in arcog_id_to_gene_dict:
                    arcog_id_to_gene_dict[arcog_id] = set()
                arcog_id_to_gene_dict[arcog_id].add(gene_id)

for fun_id in arcog_id_to_gene_dict:
    gene_set = arcog_id_to_gene_dict[fun_id]
    op_txt= '%s/%s_genes.txt' % (dir_out, fun_id)
    with open(op_txt, 'w') as f:
        f.write('\n'.join(sorted(list(gene_set))))

