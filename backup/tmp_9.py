import os


def sep_path_basename_ext(file_in):

    f_path, f_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(f_name)
    f_ext = f_ext[1:]

    return f_name, f_path, f_base, f_ext


all_fun_id = set()
enrich_dod = dict()
for each_file in open('/Users/songweizhi/Desktop/Sponge_r226/11_Functional_enrichment_analysis/a.txt'):
    each_file = each_file.strip()
    f_name, f_path, f_base, f_ext = sep_path_basename_ext(each_file)
    current_enrich_dict = dict()
    for each_line in open(each_file):
        each_line_split = each_line.strip().split('\t')
        if not each_line.startswith('ID\tP_value\t'):
            fun_id = each_line_split[0]
            value_to_report = ''
            fold_diff = each_line_split[4]
            pct_1 = float(each_line_split[2])
            pct_2 = float(each_line_split[3])
            if fold_diff == 'NA':
                value_to_report = abs(pct_1 - pct_2)
            else:
                value_to_report = '%sx' % fold_diff
            current_enrich_dict[fun_id] = value_to_report
            all_fun_id.add(fun_id)
    enrich_dod[f_base] = current_enrich_dict

print(enrich_dod)









