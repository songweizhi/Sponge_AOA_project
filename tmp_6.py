import os

########################################################################################################################

# file in
enriched_fun_id_txt = '/Users/songweizhi/Desktop/enriched_fun_id.txt'
df_in_arcog         = '/scratch/PI/ocessongwz/Sponge_r220/3_combined_genomes_50_5_dRep97_291_arCOG_wd/3_combined_genomes_50_5_dRep97_291_faa_arCOG_id.txt'
df_in_kegg          = '/scratch/PI/ocessongwz/Sponge_r220/3_combined_genomes_50_5_dRep97_291_KEGG_wd/3_combined_genomes_50_5_dRep97_291_user_ko_D.txt'
db_arcog            = '/scratch/PI/ocessongwz/DB/arCOG/arCOGdef.tab'
db_kegg             = '/scratch/PI/ocessongwz/DB/KEGG_20240508/ko00001.keg'

# file out
op_dir              = '/Users/songweizhi/Desktop/test'

enriched_fun_id_txt = '/scratch/PI/ocessongwz/Sponge_r220/5_enrichment_analysis/enriched_fun_id.txt'
op_dir              = '/scratch/PI/ocessongwz/Sponge_r220/5_enrichment_analysis/individual_fun_id'

########################################################################################################################

for each_id in open(enriched_fun_id_txt):
    fun_id = each_id.strip()
    single_id_txt = '%s/%s.txt' % (op_dir, fun_id)

    print('Processing %s' %  fun_id)

    with open(single_id_txt, 'w') as single_id_txt_handle:
        single_id_txt_handle.write(fun_id)

    subset_df_arcog = 'BioSAK subset_df -b -m -c %s.txt -o %s_df.txt -i %s'             % (fun_id, fun_id, df_in_arcog)
    subset_df_kegg  = 'BioSAK subset_df -b -m -c %s.txt -o %s_df.txt -i %s'             % (fun_id, fun_id, df_in_kegg)
    add_desc_arcog  = 'BioSAK add_desc -i %s_df.txt -o %s_desc.txt -d %s'               % (fun_id, fun_id, db_arcog)
    add_desc_kegg   = 'BioSAK add_desc -i %s_df.txt -o %s_desc.txt -d %s'               % (fun_id, fun_id, db_kegg)
    itol_arcog      = 'TreeSAK iTOL -Binary -lt %s -lm %s_desc.txt -o %s_desc_iTOL.txt' % (fun_id, fun_id, fun_id)
    itol_kegg       = 'TreeSAK iTOL -Binary -lt %s -lm %s_desc.txt -o %s_desc_iTOL.txt' % (fun_id, fun_id, fun_id)

    if 'arCOG' in fun_id:
        os.system(subset_df_arcog)
        os.system(add_desc_arcog)
        os.system(itol_arcog)
    elif 'K' in fun_id:
        os.system(subset_df_kegg)
        os.system(add_desc_kegg)
        os.system(itol_kegg)
    else:
        print(fun_id)




