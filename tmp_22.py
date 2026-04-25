
aai_txt = '/Users/songweizhi/Desktop/aai_summary.tsv'

deep_sea_mag_list = ['GCA965197515_1', 'GCA965218725_1', 'GCA965224035_1']

for each_line in open(aai_txt):
    each_line_split = each_line.strip().split('\t')
    gnm_1 = each_line_split[0]
    gnm_2 = each_line_split[1]
    ani_value = float(each_line_split[2])

    gnm_1_habitat = 'shallow'
    if gnm_1 in deep_sea_mag_list:
        gnm_1_habitat = 'deep'

    gnm_2_habitat = 'shallow'
    if gnm_2 in deep_sea_mag_list:
        gnm_2_habitat = 'deep'


    if gnm_1_habitat != gnm_2_habitat:
        print(ani_value)
