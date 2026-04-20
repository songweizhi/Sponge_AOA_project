
meta_data_txt                       = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/AOA_metadata_20260419.txt'
gnm_id_txt                          = '/Users/songweizhi/Desktop/Sponge_r226/00_metadata/gnm_id_2287.txt'


gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])


n = 0
col_index = dict()
for each_gnm in open(meta_data_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id = each_gnm_split[col_index['Genome']]
        if gnm_id in gnm_id_set:
            gnm_tax_226        = each_gnm_split[col_index['GTDB_Taxon_r226']]
            gnm_tax_232        = each_gnm_split[col_index['GTDB_Taxon_r232']]
            gnm_dbscc        = each_gnm_split[col_index['DBSCC']]

            gnm_tax_226_genus = 'g__'
            for each in gnm_tax_226.split(';'):
                if each.startswith('g__'):
                    gnm_tax_226_genus = each

            gnm_tax_232_genus = 'g__'
            for each in gnm_tax_232.split(';'):
                if each.startswith('g__'):
                    gnm_tax_232_genus = each

            if 'f__Nitrosopumilaceae' in gnm_tax_226:

                if gnm_tax_232_genus == 'g__CAYWRD01':
                    print(gnm_dbscc, gnm_tax_226_genus, gnm_tax_232_genus, gnm_id, sep='\t')

                # # print(gnm_id, gnm_tax_226, gnm_tax_232)
                # if gnm_tax_226_genus != gnm_tax_232_genus:
                #     print(gnm_dbscc, gnm_tax_226_genus, gnm_tax_232_genus, gnm_id, sep='\t')
                #     n += 1

print(n)


'''

f__Nitrosopumilaceae    1389
changed                 56



na	g__	g__JBBDNF01	GCA050749365_1
na	g__	g__JBBDNF01	GCA050749445_1
na	g__JACQFM01	g__JBBDNF01	GCA016200035_1

na	g__JAWVZS01	g__CAYWRD01	GCA964460675_1
na	g__JAWVZS01	g__CAYWRD01	GCA033722055_1

'''