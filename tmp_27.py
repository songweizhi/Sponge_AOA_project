import os


########################################################################################################################

meta_data_txt   = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260130.txt'
gnm_id_txt      = '/Users/songweizhi/Desktop/Sponge_r226/09_Dating/genome_for_dating_54_GTDB_Tree_r226_ar53.rooted.tree.txt'

out_txt         = '/Users/songweizhi/Desktop/a.txt'

########################################################################################################################

gnm_set = set()
for gnm in open(gnm_id_txt):
    gnm_set.add(gnm.strip())

out_txt_handle = open(out_txt, 'w')
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        gnm_dbscc               = each_gnm_split[col_index['DBSCC']]
        gnm_taxon               = each_gnm_split[col_index['GTDB_Taxon_r226']]
        gnm_taxon_split         = gnm_taxon.split(';')
        gnm_f                   = gnm_taxon_split[4]
        gnm_g                   = gnm_taxon_split[5]
        if gnm_id in gnm_set:
            if gnm_f == 'f__Nitrosopumilaceae':
                if gnm_dbscc != 'na':
                    print('%s\t%s' % (gnm_dbscc, gnm_id))
                    out_txt_handle.write('%s\t%s\n' % (gnm_dbscc, gnm_id))
                else:
                    print('%s\t%s' % (gnm_g, gnm_id))
                    out_txt_handle.write('%s\t%s\n' % (gnm_g, gnm_id))
out_txt_handle.close()
