from Bio import SeqIO


gnm_id_txt  = '/Users/songweizhi/Desktop/Sponge_r220/12_Amo_gene_tree/3_combined_genomes_50_5_614_dRep99_406.txt'
seq_in      = '/Users/songweizhi/Desktop/Sponge_r220/12_Amo_gene_tree/AmoX_genes.fa'
seq_out     = '/Users/songweizhi/Desktop/Sponge_r220/12_Amo_gene_tree/dRep99_406_AmoX_genes.fa'


interested_gnm_set = set()
for each_gnm in open(gnm_id_txt):
    interested_gnm_set.add(each_gnm.strip())

seq_out_handle = open(seq_out, 'w')
for each_seq in SeqIO.parse(seq_in, 'fasta'):
    gene_id = each_seq.id
    gnm_id = '_'.join(gene_id.split('_')[:-1])
    if gnm_id in interested_gnm_set:
        seq_out_handle.write('>%s\n%s\n' % (gene_id, each_seq.seq))
seq_out_handle.close()
