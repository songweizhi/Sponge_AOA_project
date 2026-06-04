
sample_group_txt    = '/Users/songweizhi/Desktop/D11d_biosample_group.txt'
df_txt              = '/Users/songweizhi/Desktop/D11d_T.txt'

grp_set = set()
sample_group_dict = dict()
for each_line in open(sample_group_txt):
    each_line_split = each_line.strip().split('\t')
    sample_group_dict[each_line_split[0]] = each_line_split[1]
    grp_set.add(each_line_split[1])

grp_list_sorted  = sorted(list(grp_set))

grp_set = set()
dod = dict()
line_num_index = 0
header_list = []
for each_line in open(df_txt):
    each_line_split = each_line.strip().split('\t')

    if line_num_index == 0:
        header_list = each_line_split
    else:
        gnm_id = each_line_split[0]
        current_gnm_dict= dict()
        for (sample, value) in zip(header_list[1:], each_line_split[1:]):
            sample_grp = sample_group_dict[sample]
            if sample_grp not in current_gnm_dict:
                current_gnm_dict[sample_grp] = 0
            if value != '0':
                current_gnm_dict[sample_grp] += 1
        dod[gnm_id] = current_gnm_dict
    line_num_index += 1


print('\t' + '\t'.join(grp_list_sorted))
for each_gnm in dod:
    gnm_dict = dod[each_gnm]
    value_list = [each_gnm]
    for each_grp  in grp_list_sorted:
        value_list.append(str(gnm_dict.get(each_grp, '0')))
    print('\t'.join(value_list))
