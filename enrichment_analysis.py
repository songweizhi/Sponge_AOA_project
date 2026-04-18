
gnm_id_txt      = '/Users/songweizhi/Desktop/Sponge_r220/metadata/gnm_id_291.txt'
gnm_id_txt_DBSC = '/Users/songweizhi/Desktop/Sponge_r220/metadata/gnm_id_291_DBSCs.txt'
metadata_txt    = '/Users/songweizhi/Desktop/Sponge_r220/metadata/metadata.txt'
cpl_cutoff      = 75

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip())

gnm_id_set_DBSC = set()
for each_gnm in open(gnm_id_txt_DBSC):
    gnm_id_set_DBSC.add(each_gnm.strip().split()[0])

col_index = {}
for each_gnm in open(metadata_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id  = each_gnm_split[col_index['Genome']]
        gnm_cpl = float(each_gnm_split[col_index['Completeness']])
