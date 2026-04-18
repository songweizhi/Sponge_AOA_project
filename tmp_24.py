from Bio import SeqIO


sponge_taxa_txt  = '/Users/songweizhi/Desktop/sponge_taxa.txt'
ref_seq_taxa_txt = '/Users/songweizhi/Desktop/aaa/accession_organism.txt'
interested_refseq_txt = '/Users/songweizhi/Desktop/aaa/interested_refseq.txt'


sponge_genus_set = set()
for each_line in open(sponge_taxa_txt):
    each_line_split = each_line.strip().split(';')
    for each_rank in each_line_split:
        if each_rank.startswith('g__'):
            if each_rank != 'g__':
                sponge_genus_set.add(each_rank)
print(sponge_genus_set)
print(len(sponge_genus_set))

refseq_set = set()
ref_seq_taxa_set = set()
for each_line in open(ref_seq_taxa_txt):
    each_line_split = each_line.strip().split('\t')
    tax_str = each_line_split[1]
    tax_str_split = tax_str.strip().split(';')
    genus = ''
    for each_tax in tax_str_split:
        if each_tax.startswith('g__'):
            if each_tax != 'g__':
                ref_seq_taxa_set.add(each_tax)
                genus = each_tax
    if genus in sponge_genus_set:
        refseq_set.add(each_line_split[0])

print(ref_seq_taxa_set)
print(len(ref_seq_taxa_set))


found_set = set()
unfound_set = set()
found_num = 0
unfound_num = 0
for each in sponge_genus_set:
    if each in ref_seq_taxa_set:
        found_num += 1
        found_set.add(each)
    else:
        unfound_num += 1
        unfound_set.add(each)

print('found_num', found_num)
print('unfound_num', len(unfound_set), ','.join(unfound_set))
print()

print(len(refseq_set))

with open(interested_refseq_txt, 'w') as f:
    f.write('\n'.join(refseq_set) + '\n')