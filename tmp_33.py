from Bio import SeqIO


leaf_taxonomy_txt                   = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/tax_to_tax_lineage.txt'


genus_set_18s_tree = set()
for each in open('/Users/songweizhi/Desktop/rename_leaf.txt'):
    genus_set_18s_tree.add(each.split('\t')[0])

tax_lineage_dict = dict()
for each_line in open(leaf_taxonomy_txt):
    each_line_split = each_line.strip().split('\t')
    tax_lineage_dict[each_line_split[0]] = each_line_split[1]

o_to_g_dict = dict()
for each in SeqIO.parse('/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_COI_iden95_g_representatives_JL.ffn', 'fasta'):
    seq_id = each.id
    #if seq_id not in genus_set_18s_tree:
    # print(seq_id, tax_lineage_dict[seq_id])
    lineage_str = tax_lineage_dict[seq_id]
    lineage_str_split = lineage_str.split(';')
    current_o = 'o__'
    for each in lineage_str_split:
        if each.startswith('o__'):
            current_o = each
    if current_o != 'o__':
        if current_o not in o_to_g_dict:
            o_to_g_dict[current_o] = set()
        o_to_g_dict[current_o].add(seq_id)

# for each_o in o_to_g_dict:
#     #if len(o_to_g_dict[each_o]) >= 3:
#     print(each_o, ','.join(o_to_g_dict[each_o]), sep='\t')

for each in tax_lineage_dict:
    if each.startswith('g__'):
        str_to_write = '%s\t%s' % (each, tax_lineage_dict[each])
        str_to_write = str_to_write.replace(';s__', '')
        print(str_to_write)
