
meta_txt_r220 = '/Users/songweizhi/DB/GTDB/r220/ar53_metadata_r220.tsv'
meta_txt_r226 = '/Users/songweizhi/DB/GTDB/r226/ar53_metadata_r226.tsv'


interested_gnm_set = set()
gnm_genus_dict_220 = dict()
genus_set = set()
stats_dict_r220 = dict()
col_index = dict()
line_num_index = 0
for each_line in open(meta_txt_r220):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        col_index = {key: i for i, key in enumerate(line_split)}
    else:
        gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
        if 'f__Nitrosopumilaceae' in gtdb_taxonomy:
            tax_split = gtdb_taxonomy.split(';')
            genus = tax_split[5]
            gnm_genus_dict_220[line_split[0]] = genus
            genus_set.add(genus)
            if genus not in stats_dict_r220:
                stats_dict_r220[genus] = 0
            stats_dict_r220[genus] += 1

gnm_genus_dict_226 = dict()
stats_dict_r226 = dict()
col_index = dict()
line_num_index = 0
for each_line in open(meta_txt_r226):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        col_index = {key: i for i, key in enumerate(line_split)}
    else:
        gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
        if 'f__Nitrosopumilaceae' in gtdb_taxonomy:
            tax_split = gtdb_taxonomy.split(';')
            genus = tax_split[5]
            gnm_genus_dict_226[line_split[0]] = genus
            genus_set.add(genus)
            if genus not in stats_dict_r226:
                stats_dict_r226[genus] = 0
            stats_dict_r226[genus] += 1
            if 'g__JBFJMG01' in gtdb_taxonomy:
                print(line_split)
                interested_gnm_set.add(line_split[0])

for each_g in sorted(list(genus_set)):
    gnm_num_220 = stats_dict_r220.get(each_g, 0)
    gnm_num_226 = stats_dict_r226.get(each_g, 0)
    if gnm_num_220 == 0:
        print('%s\t%s\t%s' % (each_g, gnm_num_220, gnm_num_226))
