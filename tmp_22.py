import os
import glob


def sep_path_basename_ext(file_in):
    f_path, f_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(f_name)
    f_ext = f_ext[1:]
    return f_name, f_path, f_base, f_ext


file_dir = '/Users/songweizhi/Desktop/777'
file_ext = 'treefile'
op_dir   = '/Users/songweizhi/Desktop/untitledfolder5_rooted'


file_re = '%s/*.%s' % (file_dir, file_ext)
file_list = glob.glob(file_re)

for each_tree in file_list:
    f_name, f_path, f_base, f_ext = sep_path_basename_ext(each_tree)
    root_tree_cmd = 'TreeSAK RootTreeGTDB226 -d ar -add_root -tree %s -o %s/%s.rooted.%s -tax /Users/songweizhi/Desktop/Sponge_r226/03_AOA_genomes_GTDB_Taxonomy_r226.txt -db /Users/songweizhi/DB/GTDB/r226' % (each_tree, op_dir, f_base, f_ext)
    os.system(root_tree_cmd)
