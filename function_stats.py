
file_in = '/Users/songweizhi/Desktop/user_ko.txt'
op_dir  = '/Users/songweizhi/Desktop/user_ko'


gnm_to_anno_dict = dict()
for each_line in open(file_in):
    each_line_split = each_line.strip().split('\t')
    gnm_id = '_'.join(each_line_split[0].split('_')[:-1])
    if gnm_id not in gnm_to_anno_dict:
        gnm_to_anno_dict[gnm_id] = set()
    gnm_to_anno_dict[gnm_id].add(each_line.strip())

for each_gnm in gnm_to_anno_dict:
    gene_to_ko_txt = '%s/%s.txt' % (op_dir, each_gnm)
    with open(gene_to_ko_txt, 'w') as gene_to_ko_txt_handle:
        gene_to_ko_txt_handle.write('\n'.join(sorted(list(gnm_to_anno_dict[each_gnm]))))
