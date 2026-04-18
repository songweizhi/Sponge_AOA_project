from Bio import SeqIO


def get_representative_seq(marker_fa, seq_tax, subsample_rank, fa_representative, tax_to_tax_lineage_txt):

    seq_set = set()
    for each_seq in SeqIO.parse(marker_fa, 'fasta'):
        seq_set.add(each_seq.id)

    tax_lineage_dict = dict()
    seq_to_grp_dict = dict()
    grp_to_seq_dict = dict()
    for each_line in open(seq_tax):
        each_line_split = each_line.strip().split('\t')
        if each_line_split[0] in seq_set:
            tax_str = each_line_split[1]
            tax_str_split = tax_str.split(';')
            taxon_name = '%s__' % subsample_rank

            lineage = []
            keep_value = True
            for each_r in tax_str_split:
                if keep_value is True:
                    lineage.append(each_r)
                else:
                    lineage.append(each_r.split('__')[0] + '__')

                if ' ' in each_r:
                    each_r = each_r.split(' ')[0]
                if each_r.startswith('%s__' % subsample_rank):
                    taxon_name = each_r
                    keep_value = False

            if taxon_name != ('%s__' % subsample_rank):
                if taxon_name not in grp_to_seq_dict:
                    grp_to_seq_dict[taxon_name] = set()
                grp_to_seq_dict[taxon_name].add(each_line_split[0])
                seq_to_grp_dict[each_line_split[0]] = taxon_name
                tax_lineage_dict[taxon_name] = ';'.join(lineage)

    representative_seq_set = set()
    for each_g in grp_to_seq_dict:
        current_g_seq_set = grp_to_seq_dict[each_g]
        representative_seq_set.add(list(current_g_seq_set)[0])

    fa_representative_handle = open(fa_representative, 'w')
    for each_seq in SeqIO.parse(marker_fa, 'fasta'):
        if each_seq.id in representative_seq_set:
            seq_grp = seq_to_grp_dict[each_seq.id]
            fa_representative_handle.write('>%s\n' % seq_grp)
            fa_representative_handle.write('%s\n' % each_seq.seq)
    fa_representative_handle.close()

    tax_to_tax_lineage_txt_handle = open(tax_to_tax_lineage_txt, 'w')
    for each_tax in tax_lineage_dict:
        tax_to_tax_lineage_txt_handle.write('%s\t%s\n' % (each_tax, tax_lineage_dict[each_tax]))
    tax_to_tax_lineage_txt_handle.close()


########################################################################################################################

# 18S
fa_18s                      = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/18S/RefSeqs_with_AOA_18S_iden99.fasta'
meta_18s                    = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/seq_taxa_18S.txt'
subsample_rank              = 'g'
fa_18s_representative       = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_18S_iden99_%s_representatives.fasta'   % subsample_rank
tax_to_tax_lineage_txt_18s  = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/tax_to_tax_lineage_18S_%s.txt'                          % subsample_rank

# COI
fa_coi                      = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/COI/RefSeqs_with_AOA_COI_iden95.ffn'
meta_coi                    = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/seq_taxa_COI.txt'
subsample_rank              = 'g'
fa_coi_representative       = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/RefSeqs_with_AOA_COI_iden95_%s_representatives.ffn'     % subsample_rank
tax_to_tax_lineage_txt_coi  = '/Users/songweizhi/Desktop/Sponge_r226/07_Sponge_tree/tax_to_tax_lineage_COI_%s.txt'                          % subsample_rank

########################################################################################################################

get_representative_seq(fa_18s, meta_18s, subsample_rank, fa_18s_representative, tax_to_tax_lineage_txt_18s)
get_representative_seq(fa_coi, meta_coi, subsample_rank, fa_coi_representative, tax_to_tax_lineage_txt_coi)
