
for each_line in open('/Users/songweizhi/Desktop/blastp.txt'):
    each_line = each_line.strip().split('\t')
    iden = float(each_line[2])
    len = int(each_line[3])
    gnm_id = '_'.join(each_line[1].split('_')[:-1])
    if len >= 235:
        print(gnm_id + '\t1')
