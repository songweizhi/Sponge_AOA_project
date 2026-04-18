import os
import pandas as pd


def subset_df(file_in, rows_to_keep_file, cols_to_keep_file, sep_symbol, row_name_pos, column_name_pos, file_out):

    # read in rows_to_keep_file
    rows_to_keep_set = set()
    for each_r in open(rows_to_keep_file):
        rows_to_keep_set.add(each_r.strip())

    # read in cols_to_keep_file
    cols_to_keep_set = set()
    for each_c in open(cols_to_keep_file):
        cols_to_keep_set.add(each_c.strip())

    # turn sets into lists
    rows_to_keep_list_sorted = sorted(list(rows_to_keep_set))
    cols_to_keep_list_sorted = sorted(list(cols_to_keep_set))

    # read in df
    df = pd.read_csv(file_in, sep=sep_symbol, header=column_name_pos, index_col=row_name_pos)

    if len(rows_to_keep_list_sorted) == 0:
        if len(cols_to_keep_list_sorted) == 0:
            subset_df = df.loc[:, :]
        else:
            subset_df = df.loc[:, cols_to_keep_list_sorted]
    else:
        if len(cols_to_keep_list_sorted) == 0:
            subset_df = df.loc[rows_to_keep_list_sorted, :]
        else:
            subset_df = df.loc[rows_to_keep_list_sorted, cols_to_keep_list_sorted]

    subset_df.to_csv(file_out, sep=sep_symbol)


########################################################################################################################

# file in
# enriched_fun_txt    = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/13_enrich/arCOG_summary_enriched_in_symbionts.txt'
# skip_first_row      = True
# df_file_in          = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/13_enrich/6_combined_genomes_dereplicated_207_faa_arCOG_id_copy.txt'

# file out
# df_file_out         = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/13_enrich/6_combined_genomes_dereplicated_207_faa_arCOG_id_copy_enriched.txt'
# df_file_out_itol    = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/13_enrich/6_combined_genomes_dereplicated_207_faa_arCOG_id_copy_enriched.txt'

########################################################################################################################

# file in
enriched_fun_txt    = '/Users/songweizhi/Documents/Research/Sponge_AOA_project/13_enrich/arCOG_summary_enriched_in_symbionts.txt'
skip_first_row      = True
df_file_in          = '/Users/songweizhi/Documents/Research/Sponge/13_enrich/6_combined_genomes_dereplicated_207_faa_arCOG_id_copy.txt'

# file out
df_file_out         = '/Users/songweizhi/Documents/Research/Sponge/13_enrich/6_combined_genomes_dereplicated_207_faa_arCOG_id_copy_enriched.txt'
df_file_out_itol    = '/Users/songweizhi/Documents/Research/Sponge/13_enrich/6_combined_genomes_dereplicated_207_faa_arCOG_id_copy_enriched.txt'

########################################################################################################################

# read enriched functions into set
enriched_fun_set = set()
row_num_index = 0
for each_fun in open(enriched_fun_txt):
    each_fun_split = each_fun.strip().split('\t')
    if row_num_index == 0:
        if skip_first_row is False:
            enriched_fun_set.add(each_fun_split[0])
    else:
        enriched_fun_set.add(each_fun_split[0])
    row_num_index += 1


subset_df(df_file_in, [], sorted(list(enriched_fun_set)), '\t', 0, 0, df_file_out)





