
metadata_txt    = '/Users/songweizhi/Desktop/Sponge_r220/8_AOA_habitat/o__Nitrososphaerales_50_5_taxonomy_no_f__Nitrosopumilaceae_metadata/summary.txt'
op_txt          = '/Users/songweizhi/Desktop/Sponge_r220/8_AOA_habitat/o__Nitrososphaerales_50_5_taxonomy_no_f__Nitrosopumilaceae_metadata/summary_2.txt'


op_txt_handle = open(op_txt, 'w')
for each_line in open(metadata_txt):
    each_line_split = each_line.strip().split('\t')
    gnm_id = each_line_split[0]
    gnm_id = gnm_id.replace('_', '')
    gnm_id = gnm_id.replace('.', '_')

    gnm_habitat = ''
    if each_line_split.count('na') == 8:
        pass
    elif 'mine drainage' in each_line:
        gnm_habitat = 'mine drainage'
    elif 'soil' in each_line:
        gnm_habitat = 'soil'
    elif 'groundwater' in each_line:
        gnm_habitat = 'groundwater'
    elif 'marine' in each_line:
        gnm_habitat = 'marine'
    elif 'seawater' in each_line:
        gnm_habitat = 'marine'
    elif 'deep sea' in each_line:
        gnm_habitat = 'marine'
    elif 'river sediment' in each_line:
        gnm_habitat = 'sediment'
    elif 'hot spring' in each_line:
        gnm_habitat = 'hot spring'
    elif 'wastewater' in each_line:
        gnm_habitat = 'wastewater'
    elif 'mangrove' in each_line:
        gnm_habitat = 'marine'
    elif 'rhizosphere' in each_line:
        gnm_habitat = 'soil'
    elif 'freshwater' in each_line:
        gnm_habitat = 'freshwater'
    elif 'rhizoplane' in each_line:
        gnm_habitat = 'soil'
    elif 'cold seep' in each_line:
        gnm_habitat = 'cold seep'
    elif 'fossil' in each_line:
        gnm_habitat = 'fossil'
    elif 'Ocean' in each_line:
        gnm_habitat = 'marine'
    else:
        print(each_line_split)
    gnm_habitat = gnm_habitat.replace(' ', '_')
    if gnm_habitat != '':
        op_txt_handle.write('%s\t%s\n' % (gnm_id, gnm_habitat))
op_txt_handle.close()
