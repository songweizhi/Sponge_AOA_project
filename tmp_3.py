import os

txt_file = '/Users/songweizhi/Documents/Research/Sponge/14_interested_functions/the_rest_29_enriched_fun_id.txt'
txt_file = '/Users/songweizhi/Documents/Research/Sponge/14_interested_functions_Shan_paper/fun_id_shan.txt'

for each_line in open(txt_file):

    fun_id = each_line.strip().split('\t')[0]
    print('# ' + fun_id)

    subset_cmd = ''
    add_desc_cmd = ''
    itol_cmd = ''
    if 'arCOG' in fun_id:
        subset_cmd      = 'BioSAK subset_df -c %s.txt -i ../6_combined_genomes_dereplicated_207_faa_arCOG_wd/6_combined_genomes_dereplicated_207_faa_arCOG.txt -o %s_PA_matrix.txt -m'      % (fun_id, fun_id)
        add_desc_cmd    = 'BioSAK add_desc -i %s_PA_matrix.txt -o %s_PA_matrix_desc.txt -d /Users/songweizhi/DB/arCOG18/arCOGdef.tab'                                                       % (fun_id, fun_id)
        itol_cmd        = 'BioSAK iTOL -Binary -lm %s_PA_matrix_desc.txt -lt Shan_%s -o %s_PA_matrix_desc_iTOL.txt' % (fun_id, fun_id, fun_id)
    else:
        subset_cmd      = 'BioSAK subset_df -c %s.txt -i ../6_combined_genomes_dereplicated_207_user_ko_KEGG_wd/6_combined_genomes_dereplicated_207_user_ko_D.txt -o %s_PA_matrix.txt -m'   % (fun_id, fun_id)
        add_desc_cmd    = 'BioSAK add_desc -i %s_PA_matrix.txt -o %s_PA_matrix_desc.txt -d /Users/songweizhi/DB/KEGG_2024_03_04/ko00001.keg'                                                % (fun_id, fun_id)
        itol_cmd        = 'BioSAK iTOL -Binary -lm %s_PA_matrix_desc.txt -lt Shan_%s -o %s_PA_matrix_desc_iTOL.txt' % (fun_id, fun_id, fun_id)

    print(subset_cmd)
    print(add_desc_cmd)
    print(itol_cmd)
    print()
