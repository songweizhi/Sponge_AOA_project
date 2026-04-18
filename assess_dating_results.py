
genus_set = set()
genome_num = 0
for tax in open('/Users/songweizhi/DB/GTDB/ar53_taxonomy_r220.tsv'):
    tax_split = tax.strip().split('\t')
    tax_str = tax_split[1]
    tax_str_split = tax_str.split(';')
    genus = tax_str_split[5]
    if 'f__Nitrosopumilaceae' in tax:
        genus_set.add(genus)
        genome_num += 1

print('genus num: %s'  % len(genus_set))
print('genome num: %s' % genome_num)

genus_set = set()
genome_num = 0
for tax in open('/Users/songweizhi/DB/GTDB/ar122_taxonomy_r86.2.tsv'):
    tax_split = tax.strip().split('\t')
    tax_str = tax_split[1]
    tax_str_split = tax_str.split(';')
    genus = tax_str_split[5]
    if 'f__Nitrosopumilaceae' in tax:
        genus_set.add(genus)
        genome_num += 1

print('genus num: %s'  % len(genus_set))
print('genome num: %s' % genome_num)
