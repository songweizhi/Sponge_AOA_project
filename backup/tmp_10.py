import os


def get_shared_uniq_elements(list_1, list_2):
    shared_set = set(list_1).intersection(list_2)
    list_1_uniq = []
    for e1 in list_1:
        if e1 not in shared_set:
            list_1_uniq.append(e1)
    list_2_uniq = []
    for e2 in list_2:
        if e2 not in shared_set:
            list_2_uniq.append(e2)
    return shared_set, list_1_uniq, list_2_uniq


fun_enriched_in_sym = set()
fun_enriched_in_the_rest = set()
all_fun_id = set()
enrich_dod = dict()
for each_file in open('/Users/songweizhi/Desktop/Sponge_r226/11_Functional_enrichment_analysis/a.txt'):
    each_file = each_file.strip()
    if 'KEGG' in each_file:
        pass
    if 'arCOG' in each_file:
        if 'Cenarchaeum_39_vs_JAWVZS01_15' not in each_file:

            if 'enriched_in_The_rest_symbionts' in each_file:
                for each_line in open(each_file):
                    if not each_line.startswith('ID\t'):
                        each_line_split = each_line.strip().split('\t')
                        fun_id = each_line_split[0]
                        fun_enriched_in_the_rest.add(fun_id)
            else:
                for each_line in open(each_file):
                    if not each_line.startswith('ID\t'):
                        each_line_split = each_line.strip().split('\t')
                        fun_id = each_line_split[0]
                        fun_enriched_in_sym.add(fun_id)


print(len(fun_enriched_in_sym))
print(len(fun_enriched_in_the_rest))
print()

shared_set, sym_uniq, the_rest_uniq = get_shared_uniq_elements(fun_enriched_in_sym, fun_enriched_in_the_rest)

print(len(shared_set))
print(len(sym_uniq))
print(len(the_rest_uniq))


print(fun_enriched_in_the_rest)