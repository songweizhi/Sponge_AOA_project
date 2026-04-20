
gnm_id_txt = '/Users/songweizhi/Desktop/AOA_genome_r232_uniq_449_uniq_130.txt'

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip().split()[0])



for each_line in open('/Users/songweizhi/Desktop/AOA_genome_r232_50_5_taxonomy.txt'):
    each_line_split = each_line.strip().split('\t')

    gnm_id = each_line_split[0].replace('_','').replace('.','_')

    if gnm_id in gnm_id_set:
        cpl = float(each_line_split[1])
        ctm = float(each_line_split[2])
        index = cpl - (5 * ctm)
        index = float("{0:.2f}".format(index))  # 123.45

        size_bp = int(each_line_split[3])
        size_Mbp = size_bp / (1024 * 1024)
        size_Mbp_adjust = size_Mbp * 100 / cpl

        size_Mbp = float("{0:.2f}".format(size_Mbp))  # 123.45
        size_Mbp_adjust = float("{0:.2f}".format(size_Mbp_adjust))  # 123.45

        print(gnm_id, index, size_Mbp, size_Mbp_adjust, each_line.strip(), sep='\t')



