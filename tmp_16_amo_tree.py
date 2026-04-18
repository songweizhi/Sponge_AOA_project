from Bio import SeqIO


gene_id_txt         = '/Users/songweizhi/Desktop/Sponge_r220/12_Amo_gene_tree/dRep99_406_AmoC_genes.bmge.maxgap40.aln'
gene_id_rename_txt  = '/Users/songweizhi/Desktop/Sponge_r220/12_Amo_gene_tree/dRep99_406_AmoC_genes_rename.txt'


gnm_to_gene_dict = dict()
for each_seq in SeqIO.parse(gene_id_txt, 'fasta'):
    gene_id = each_seq.id
    gnm_id = '_'.join(gene_id.split('_')[:-1])
    if gnm_id not in gnm_to_gene_dict:
        gnm_to_gene_dict[gnm_id] = set()
    gnm_to_gene_dict[gnm_id].add(gene_id)

single_copy_num = 0
multi_copy_num = 0
for each_gnm in gnm_to_gene_dict:
    gene_set = gnm_to_gene_dict[each_gnm]
    if len(gene_set) == 1:
        single_copy_num += 1
    elif len(gene_set) > 1:
        multi_copy_num += 1

gene_id_rename_txt_handle = open(gene_id_rename_txt, 'w')
for each_gnm in gnm_to_gene_dict:
    gene_list = list(gnm_to_gene_dict[each_gnm])
    if len(gene_list) == 1:
        gene_id = gene_list[0]
        gene_id_rename_txt_handle.write('%s\t%s\n' % (gene_id, each_gnm))
    else:
        gene_index = 1
        for each_gene in gene_list:
            gene_id_rename_txt_handle.write('%s\t%s_copy%s\n' % (each_gene, each_gnm, gene_index))
            gene_index += 1
gene_id_rename_txt_handle.close()

print('single_copy_num\t%s' % single_copy_num)
print('multi_copy_num\t%s'  % multi_copy_num)
