import sys
from Bio import SeqIO

######################################################### COI ##########################################################

if sys.argv[1] =='COI':

    # file in
    sponge_taxa_txt         = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/sponge_taxa_with_AOA.txt'
    refseq_organism_txt     = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeq_COI_wd/combined_organism.txt'
    refseq_combined_fasta   = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeq_COI_wd/combined.fasta'
    refseq_combined_faa     = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeq_COI_wd/combined_COI.faa'
    refseq_combined_ffn     = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeq_COI_wd/combined.ffn'
    faa_to_ignore_txt       = None
    get_faa                 = True
    ignore_plylum           = True

    # file out
    refseq_to_keep_txt      = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeqs_with_AOA_COI.txt'
    refseq_to_keep_fasta    = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeqs_with_AOA_COI.fasta'
    refseq_to_keep_faa      = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeqs_with_AOA_COI.faa'
    refseq_to_keep_ffn      = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/RefSeqs_with_AOA_COI.ffn'
    faa_ffn_taxa_txt        = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/COI/iTOL_COI_faa_ffn_taxa.txt'

######################################################### 28S ##########################################################

if sys.argv[1] =='28S':

    # file in
    sponge_taxa_txt         = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/sponge_taxa_with_AOA.txt'
    refseq_organism_txt     = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/28S/RefSeq_28S_wd/combined_organism.txt'
    refseq_combined_fasta   = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/28S/RefSeq_28S_wd/combined.fasta'
    refseq_combined_faa     = None
    faa_to_ignore_txt       = None
    get_faa                 = False
    ignore_plylum           = True

    # file out
    refseq_to_keep_txt      = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/28S/RefSeqs_with_AOA_28S.txt'
    refseq_to_keep_fasta    = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/28S/RefSeqs_with_AOA_28S.fasta'
    itol_refseq_taxa_txt    = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/28S/iTOL_RefSeq_taxa_28S.txt'
    faa_taxa_txt            = None
    refseq_to_keep_faa      = None

######################################################### 18S ##########################################################

if sys.argv[1] =='18S':

    # file in
    sponge_taxa_txt         = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/sponge_taxa_with_AOA.txt'
    refseq_organism_txt     = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/18S/RefSeq_18S_wd/combined_organism.txt'
    refseq_combined_fasta   = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/18S/RefSeq_18S_wd/combined.fasta'
    refseq_combined_faa     = None
    faa_to_ignore_txt       = None
    get_faa                 = False
    ignore_plylum           = True

    # file out
    refseq_to_keep_txt      = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/18S/RefSeqs_with_AOA_18S.txt'
    refseq_to_keep_fasta    = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/18S/RefSeqs_with_AOA_18S.fasta'
    itol_refseq_taxa_txt    = '/Users/songweizhi/Desktop/Sponge_r226/sponge_phylogeny/18S/iTOL_RefSeq_taxa_18S.txt'
    faa_taxa_txt            = None
    refseq_to_keep_faa      = None

########################################################################################################################

# get sponge_genus_with_aoa_set
sponge_genus_with_aoa_set = set()
for each_line in open(sponge_taxa_txt):
    each_line_split = each_line.strip().split(';')
    for each_rank in each_line_split:
        if each_rank.startswith('g__'):
            if each_rank != 'g__':
                sponge_genus_with_aoa_set.add(each_rank)
# print('Sponge taxa with AOA (%s)\t%s' % (len(sponge_genus_with_aoa_set), ','.join(sponge_genus_with_aoa_set)))
# print('g__Crambe' in sponge_genus_with_aoa_set)

# get refseq_to_keep_set
refseq_taxa_dict = dict()
refseq_to_keep_set = set()
for each_line in open(refseq_organism_txt):
    each_line_split = each_line.strip().split('\t')
    refseq_id = each_line_split[0]
    tax_str   = each_line_split[1]
    refseq_taxa_dict[refseq_id] = tax_str
    tax_str_split = tax_str.strip().split(';')
    refseq_genus = ''
    for each_rank in tax_str_split:
        if each_rank.startswith('g__'):
            if each_rank != 'g__':
                refseq_genus = each_rank
    if refseq_genus in sponge_genus_with_aoa_set:
        refseq_to_keep_set.add(refseq_id)

# write out itol_refseq_taxa_txt
itol_refseq_taxa_txt_handle = open(itol_refseq_taxa_txt, 'w')
itol_refseq_taxa_txt_handle.write('LABELS\nSEPARATOR TAB\nDATA\n')
for each_refseq in refseq_taxa_dict:
    refseq_tax = refseq_taxa_dict[each_refseq]
    refseq_tax = refseq_tax.replace('"', '')
    if ignore_plylum is True:
        refseq_tax = refseq_tax.replace('d__Eukaryota;k__Metazoa;p__Porifera;', '')
    itol_refseq_taxa_txt_handle.write('%s\t%s__%s\n' % (each_refseq, each_refseq, refseq_tax))
itol_refseq_taxa_txt_handle.close()

# write out refseq_to_keep_txt
with open(refseq_to_keep_txt, 'w') as f:
    f.write('\n'.join(sorted(list(refseq_to_keep_set))) + '\n')

# write out fasta
refseq_to_keep_fasta_handle = open(refseq_to_keep_fasta, 'w')
for each_seq in SeqIO.parse(refseq_combined_fasta, 'fasta'):
    seq_id = each_seq.id
    if seq_id in refseq_to_keep_set:
        refseq_to_keep_fasta_handle.write('>%s\n' % seq_id)
        refseq_to_keep_fasta_handle.write('%s\n' % str(each_seq.seq))
refseq_to_keep_fasta_handle.close()

# get faa
if get_faa is True:

    # write out faa
    cds_taxa_dict = dict()
    refseq_to_keep_faa_handle = open(refseq_to_keep_faa, 'w')
    for each_faa in SeqIO.parse(refseq_combined_faa, 'fasta'):
        faa_id = each_faa.id
        faa_refseq_id = faa_id.split('__')[0]
        cds_taxa_dict[faa_id] = refseq_taxa_dict.get(faa_refseq_id, 'na')
        if faa_refseq_id in refseq_to_keep_set:
            refseq_to_keep_faa_handle.write('>%s\n' % faa_id)
            refseq_to_keep_faa_handle.write('%s\n' % str(each_faa.seq))
    refseq_to_keep_faa_handle.close()

    # write out ffn
    refseq_to_keep_ffn_handle = open(refseq_to_keep_ffn, 'w')
    for each_ffn in SeqIO.parse(refseq_combined_ffn, 'fasta'):
        ffn_id = each_ffn.id
        ffn_refseq_id = ffn_id.split('__')[0]
        cds_taxa_dict[ffn_id] = refseq_taxa_dict.get(ffn_refseq_id, 'na')
        if ffn_refseq_id in refseq_to_keep_set:
            refseq_to_keep_ffn_handle.write('>%s\n' % ffn_id)
            refseq_to_keep_ffn_handle.write('%s\n' % str(each_ffn.seq))
    refseq_to_keep_ffn_handle.close()

    max_key_len = 0
    for each_key in cds_taxa_dict.keys():
        if len(each_key) > max_key_len:
            max_key_len = len(each_key)

    faa_ffn_taxa_txt_handle = open(faa_ffn_taxa_txt, 'w')
    faa_ffn_taxa_txt_handle.write('LABELS\nSEPARATOR TAB\nDATA\n')
    for each_cds in cds_taxa_dict:
        cds_taxa = cds_taxa_dict[each_cds]
        if ignore_plylum is True:
            cds_taxa = cds_taxa.replace('d__Eukaryota;k__Metazoa;p__Porifera;', '')
        cds_id_same_len = each_cds + '_'*(max_key_len - len(each_cds))
        faa_ffn_taxa_txt_handle.write('%s\t%s__%s\n' % (each_cds, cds_id_same_len, cds_taxa))
    faa_ffn_taxa_txt_handle.close()
