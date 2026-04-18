import numpy as np
from statistics import mean
from scipy.stats import mannwhitneyu


########################################################################################################################

meta_txt        = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/metadata_614.txt'
gnm_id_txt      = '/Users/songweizhi/Desktop/Sponge_r220/0_metadata/gnm_id_291.txt'
gnm_cpl_cutoff  = 75

########################################################################################################################

col_index = {}
gnm_cpl_dict = dict()
gnm_host_dict = dict()
gnm_gc_dict = dict()
gnm_size_dict = dict()
gnm_size_cpl_dict = dict()
for each_gnm in open(meta_txt):
    each_gnm_split = each_gnm.strip().split('\t')
    if each_gnm.startswith('Genome\t'):
        col_index = {key: i for i, key in enumerate(each_gnm_split)}
    else:
        gnm_id                      = each_gnm_split[col_index['Genome']]
        gnm_cpl                     = float(each_gnm_split[col_index['Completeness']])
        gnm_size                    = float(each_gnm_split[col_index['Size_Mbp']])
        gnm_size_adjusted_by_cpl    = float(each_gnm_split[col_index['Size_Mbp_adjusted_by_cpl']])
        gnm_gc                      = float(each_gnm_split[col_index['GC']])
        gnm_host                    = each_gnm_split[col_index['Host']]

        gnm_source = gnm_host
        if gnm_host == 'nonsponge':
            gnm_source = 'nonsponge'
        elif 'coral' in gnm_host:
            gnm_source = 'coral'
        elif gnm_host == 'sponge':
            gnm_source = 'sponge'
        elif gnm_host == 'na':
            gnm_source = 'na'
        else:
            gnm_source = 'sponge'

        gnm_host_dict[gnm_id]       = gnm_source
        gnm_gc_dict[gnm_id]         = gnm_gc
        gnm_size_dict[gnm_id]       = gnm_size
        gnm_size_cpl_dict[gnm_id]   = gnm_size_adjusted_by_cpl
        gnm_cpl_dict[gnm_id]        = gnm_cpl

gnm_id_set = set()
for each_gnm in open(gnm_id_txt):
    gnm_id_set.add(each_gnm.strip())

gnm_gc_list_sponge = []
gnm_gc_list_nonsponge = []
gnm_size_list_sponge = []
gnm_size_list_nonsponge = []
gnm_size_cpl_list_sponge = []
gnm_size_cpl_list_nonsponge = []
high_cpl_gnm_size_list_sponge = []
high_cpl_gnm_size_list_nonsponge = []
for each_gnm in gnm_id_set:
    gnm_cpl = gnm_cpl_dict[each_gnm]
    gnm_gc = gnm_gc_dict[each_gnm]
    gnm_size = gnm_size_dict[each_gnm]
    gnm_size_cpl = gnm_size_cpl_dict[each_gnm]
    gnm_host = gnm_host_dict[each_gnm]
    if gnm_host == 'sponge':
        gnm_gc_list_sponge.append(gnm_gc)
        gnm_size_list_sponge.append(gnm_size)
        gnm_size_cpl_list_sponge.append(gnm_size_cpl)
        if gnm_cpl >= gnm_cpl_cutoff:
            high_cpl_gnm_size_list_sponge.append(gnm_size)
    elif gnm_host == 'nonsponge':
        gnm_gc_list_nonsponge.append(gnm_gc)
        gnm_size_list_nonsponge.append(gnm_size)
        gnm_size_cpl_list_nonsponge.append(gnm_size_cpl)
        if gnm_cpl >= gnm_cpl_cutoff:
            high_cpl_gnm_size_list_nonsponge.append(gnm_size)
    else:
        print('ignored\t%s\t%s' % (each_gnm, gnm_host))
print()


_, p_value_size = mannwhitneyu(gnm_size_list_sponge, gnm_size_list_nonsponge)
print('gnm_size_sponge(%s)\t%s +/- %s'    % (len(gnm_size_list_sponge), mean(gnm_size_list_sponge), np.std(gnm_size_list_sponge)))
print('gnm_size_nonsponge(%s)\t%s +/- %s' % (len(gnm_size_list_nonsponge), mean(gnm_size_list_nonsponge), np.std(gnm_size_list_nonsponge)))
print('p_value_size\t%s'                % p_value_size)
print()

_, p_value_size_cpl = mannwhitneyu(gnm_size_cpl_list_sponge, gnm_size_cpl_list_nonsponge)
print('gnm_size_cpl_sponge(%s)\t%s +/- %s'    % (len(gnm_size_cpl_list_sponge), mean(gnm_size_cpl_list_sponge), np.std(gnm_size_cpl_list_sponge)))
print('gnm_size_cpl_nonsponge(%s)\t%s +/- %s' % (len(gnm_size_cpl_list_nonsponge), mean(gnm_size_cpl_list_nonsponge), np.std(gnm_size_cpl_list_nonsponge)))
print('p_value_size_cpl\t%s'                % p_value_size_cpl)
print()

_, high_cpl_p_value_size = mannwhitneyu(high_cpl_gnm_size_list_sponge, high_cpl_gnm_size_list_nonsponge)
print('high_cpl_gnm_size_sponge(%s)\t%s +/- %s'    % (len(high_cpl_gnm_size_list_sponge), mean(high_cpl_gnm_size_list_sponge), np.std(high_cpl_gnm_size_list_sponge)))
print('high_cpl_gnm_size_nonsponge(%s)\t%s +/- %s' % (len(high_cpl_gnm_size_list_nonsponge), mean(high_cpl_gnm_size_list_nonsponge), np.std(high_cpl_gnm_size_list_nonsponge)))
print('high_cpl_p_value_size\t%s'              % high_cpl_p_value_size)
print()

_, p_value_gc = mannwhitneyu(gnm_gc_list_sponge, gnm_gc_list_nonsponge)
print('gnm_gc_sponge(%s)\t%s +/- %s'      % (len(gnm_gc_list_sponge), mean(gnm_gc_list_sponge), np.std(gnm_gc_list_sponge)))
print('gnm_gc_nonsponge(%s)\t%s +/- %s'   % (len(gnm_gc_list_nonsponge), mean(gnm_gc_list_nonsponge), np.std(gnm_gc_list_nonsponge)))
print('p_value_gc\t%s'                  % p_value_gc)
print()
