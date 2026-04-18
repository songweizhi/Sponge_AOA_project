
# arCOG08676	AmoA
# arCOG08675	AmoB
# arCOG08699	AmoC
# arCOG10586	AmoX

arCOG08675_genes_txt = '/Users/songweizhi/Desktop/Sponge_r226/get_AOA_taxa/gnms_280_AmoABCX_stats/arCOG08675_genes.txt'
arCOG08676_genes_txt = '/Users/songweizhi/Desktop/Sponge_r226/get_AOA_taxa/gnms_280_AmoABCX_stats/arCOG08676_genes.txt'
arCOG08699_genes_txt = '/Users/songweizhi/Desktop/Sponge_r226/get_AOA_taxa/gnms_280_AmoABCX_stats/arCOG08699_genes.txt'
arCOG10586_genes_txt = '/Users/songweizhi/Desktop/Sponge_r226/get_AOA_taxa/gnms_280_AmoABCX_stats/arCOG10586_genes.txt'
gtdb_gnm_txt         = '/Users/songweizhi/Desktop/Sponge_r226/get_AOA_taxa/o__Nitrososphaerales_50_5_in_GTDB_591.txt'

gtdb_gnm_set = set()
for each in open(gtdb_gnm_txt):
    gnm_id_renamed = each.strip().replace('_', '').replace('.', '_')
    gtdb_gnm_set.add(gnm_id_renamed)

amoa_genes_set = set()
for each in open(arCOG08676_genes_txt):
    gnm_id = '_'.join(each.split('_')[:-1])
    amoa_genes_set.add(gnm_id)
amob_genes_set = set()
for each in open(arCOG08675_genes_txt):
    gnm_id = '_'.join(each.split('_')[:-1])
    amob_genes_set.add(gnm_id)
amoc_genes_set = set()
for each in open(arCOG08699_genes_txt):
    gnm_id = '_'.join(each.split('_')[:-1])
    amoc_genes_set.add(gnm_id)
amox_genes_set = set()
for each in open(arCOG10586_genes_txt):
    gnm_id = '_'.join(each.split('_')[:-1])
    amox_genes_set.add(gnm_id)

for each in open('/Users/songweizhi/Desktop/Sponge_r226/get_AOA_taxa/o__Nitrososphaerales_50_5_taxonomy.txt'):
    if not each.startswith('Genome\t'):
        each_split = each.strip().split('\t')
        gnm_id = each_split[0]
        gnm_id_renamed = gnm_id.replace('_', '').replace('.', '_')
        gnm_tax = each_split[4]
        gnm_family = gnm_tax.split(';')[4]

        has_amoa = '0'
        if gnm_id_renamed in amoa_genes_set:
            has_amoa = '1'

        has_amob = '0'
        if gnm_id_renamed in amob_genes_set:
            has_amob = '1'

        has_amoc = '0'
        if gnm_id_renamed in amoc_genes_set:
            has_amoc = '1'

        has_amox = '0'
        if gnm_id_renamed in amox_genes_set:
            has_amox = '1'

        if 'f__Nitrosopumilaceae' not in gnm_tax:
            if gnm_id_renamed in gtdb_gnm_set:
                print('%s\t%s\t%s\t%s\t%s\t%s' % (gnm_id_renamed, has_amoa, has_amob, has_amoc, has_amox, gnm_family))
