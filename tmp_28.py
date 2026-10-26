a = '/Users/songweizhi/Desktop/Sponge_r226/11_Functional_enrichment_analysis/annotation_dbCAN3_id_order_218.txt'


fun_dict  = dict()
for each in open(a):
    id = each.rstrip()
    fun_cate = ''
    if 'CBM' in id:
        fun_cate = 'CBM'
    elif 'GT' in id:
        fun_cate = 'GT'
    elif 'GH' in id:
        fun_cate = 'GH'
    elif 'PL' in id:
        fun_cate = 'PL'
    elif 'CE' in id:
        fun_cate = 'CE'
    elif 'AA' in id:
        fun_cate = 'AA'
    else:
        print(id)

    if fun_cate not in fun_dict:
        fun_dict[fun_cate] = []
    fun_dict[fun_cate].append(id)

for each in fun_dict:
    print('\n'.join(fun_dict[each]))

