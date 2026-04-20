import os


meta_txt_r226       = '/Users/songweizhi/DB/GTDB/r226/ar53_metadata_r226.tsv'
meta_txt_r232       = '/Users/songweizhi/DB/GTDB/r232/ar53_metadata_r232.tsv'
interested_taxon    = 'f__Nitrosopumilaceae'

stats_txt           = '/Users/songweizhi/Desktop/sankey/demo_sankey_sankey.txt'


gnm_to_genus_dict = dict()
col_index = dict()
line_num_index = 0
for each_line in open(meta_txt_r226):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        col_index = {key: i for i, key in enumerate(line_split)}
    else:
        gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
        gnm_accession = line_split[col_index['accession']]
        if interested_taxon in gtdb_taxonomy:
            tax_split = gtdb_taxonomy.split(';')
            genus = tax_split[5]
            genus_with_version = '%s_r226' % genus
            if gnm_accession not in gnm_to_genus_dict:
                gnm_to_genus_dict[gnm_accession] = set()
            gnm_to_genus_dict[gnm_accession].add(genus_with_version)

col_index = dict()
line_num_index = 0
for each_line in open(meta_txt_r232):
    line_num_index += 1
    line_split = each_line.strip().split('\t')
    if line_num_index == 1:
        col_index = {key: i for i, key in enumerate(line_split)}
    else:
        gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
        gnm_accession = line_split[col_index['accession']]
        if interested_taxon in gtdb_taxonomy:
            tax_split = gtdb_taxonomy.split(';')
            genus = tax_split[5]
            genus_with_version = '%s_r232' % genus
            if gnm_accession not in gnm_to_genus_dict:
                gnm_to_genus_dict[gnm_accession] = set()
            gnm_to_genus_dict[gnm_accession].add(genus_with_version)


count_dict = dict()
for each_ref in gnm_to_genus_dict:
    genus_assignment_set = gnm_to_genus_dict[each_ref]
    assign_226 = 'r226_NA'
    assign_232 = 'r232_NA'
    for i in genus_assignment_set:
        if i.endswith('_r226'):
            assign_226 = i
        if i.endswith('_r232'):
            assign_232 = i
    key_str = '%s___%s' % (assign_226, assign_232)
    if key_str not in count_dict:
        count_dict[key_str] = 0
    count_dict[key_str] += 1


stats_txt_handle = open(stats_txt, 'w')
for each_link in count_dict:
    each_link_split = each_link.split('___')

    assign_226 = each_link_split[0]
    assign_232 = each_link_split[1]
    link_num = count_dict[each_link]
    # stats_txt_handle.write('%s,%s,%s\n' % (assign_226, assign_232, link_num))

    if (assign_226 != 'r226_NA') and (assign_232 != 'r232_NA'):
        stats_txt_handle.write('%s,%s,%s\n' % (assign_226, assign_232, link_num))
    # elif (assign_226 == 'r226_NA') and (assign_232 != 'r232_NA'):
    #     stats_txt_handle.write('%s,%s,%s\n' % (assign_232, assign_226, link_num))


stats_txt_handle.close()

sankey_cmd = 'Rscript /Users/songweizhi/PycharmProjects/BioSAK/BioSAK/sankey.R -f %s' % stats_txt
print(sankey_cmd)


def meta_to_genus_dict(metadata_txt, interested_taxon):
    stats_dict = dict()
    col_index = dict()
    line_num_index = 0
    for each_line in open(metadata_txt):
        line_num_index += 1
        line_split = each_line.strip().split('\t')
        if line_num_index == 1:
            col_index = {key: i for i, key in enumerate(line_split)}
        else:
            gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
            if interested_taxon in gtdb_taxonomy:
                tax_split = gtdb_taxonomy.split(';')
                genus = tax_split[5]
                if genus not in stats_dict:
                    stats_dict[genus] = 0
                stats_dict[genus] += 1
    return stats_dict


genus_stats_r226        = meta_to_genus_dict(meta_txt_r226, interested_taxon)
genus_stats_r232        = meta_to_genus_dict(meta_txt_r232, interested_taxon)
genera_in_both_release  = (set(genus_stats_r226.keys())).union(set(genus_stats_r232.keys()))

for each_g in genera_in_both_release:
    print('%s\t%s\t%s' % (each_g, genus_stats_r226.get(each_g, 0), genus_stats_r232.get(each_g, 0) ))


# interested_gnm_set = set()
# gnm_genus_dict_220 = dict()
# genus_set = set()
# stats_dict_r220 = dict()
# col_index = dict()
# line_num_index = 0
# for each_line in open(meta_txt_r220):
#     line_num_index += 1
#     line_split = each_line.strip().split('\t')
#     if line_num_index == 1:
#         col_index = {key: i for i, key in enumerate(line_split)}
#     else:
#         gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
#         if 'f__Nitrosopumilaceae' in gtdb_taxonomy:
#             tax_split = gtdb_taxonomy.split(';')
#             genus = tax_split[5]
#             gnm_genus_dict_220[line_split[0]] = genus
#             genus_set.add(genus)
#             if genus not in stats_dict_r220:
#                 stats_dict_r220[genus] = 0
#             stats_dict_r220[genus] += 1
#
# gnm_genus_dict_226 = dict()
# stats_dict_r226 = dict()
# col_index = dict()
# line_num_index = 0
# for each_line in open(meta_txt_r226):
#     line_num_index += 1
#     line_split = each_line.strip().split('\t')
#     if line_num_index == 1:
#         col_index = {key: i for i, key in enumerate(line_split)}
#     else:
#         gtdb_taxonomy = line_split[col_index['gtdb_taxonomy']]
#         if 'f__Nitrosopumilaceae' in gtdb_taxonomy:
#             tax_split = gtdb_taxonomy.split(';')
#             genus = tax_split[5]
#             gnm_genus_dict_226[line_split[0]] = genus
#             genus_set.add(genus)
#             if genus not in stats_dict_r226:
#                 stats_dict_r226[genus] = 0
#             stats_dict_r226[genus] += 1
#             if 'g__JBFJMG01' in gtdb_taxonomy:
#                 print(line_split)
#                 interested_gnm_set.add(line_split[0])
#
# for each_g in sorted(list(genus_set)):
#     gnm_num_220 = stats_dict_r220.get(each_g, 0)
#     gnm_num_226 = stats_dict_r226.get(each_g, 0)
#     if gnm_num_220 == 0:
#         print('%s\t%s\t%s' % (each_g, gnm_num_220, gnm_num_226))
