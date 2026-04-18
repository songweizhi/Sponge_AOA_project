import os
import glob
import argparse
from Bio import SeqIO


def sep_path_basename_ext(file_in):

    f_path, f_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'
    f_base, f_ext = os.path.splitext(f_name)
    f_ext = f_ext[1:]

    return f_name, f_path, f_base, f_ext


def get_origin_seq_from_gbk(gbk_file):

    after_origin_line = False
    before_slash_line = True
    concatenated_seq = ''
    for each_line in open(gbk_file):
        each_line = each_line.strip()
        if each_line == 'ORIGIN':
            after_origin_line = True
        if each_line == '//':
            before_slash_line = False
        if (after_origin_line is True) and (before_slash_line is True):
            if each_line != 'ORIGIN':
                each_line_split = each_line.split(' ')
                seq_str = ''.join(each_line_split[1:])
                seq_str = seq_str.upper()
                concatenated_seq += seq_str

    return concatenated_seq


def combine_esearch_op_organism(op_dir, tax_lineage_dict, op_txt):

    file_re = '%s/*_organism.txt' % op_dir
    file_list = glob.glob(file_re)

    op_txt_handle = open(op_txt, 'w')
    for each_file in file_list:
        f_name, f_path, f_base, f_ext = sep_path_basename_ext(each_file)
        accession_id = f_base.split('_organism')[0]

        organism_info = ''
        full_lineage_str = ''
        with open(each_file) as f:
            organism_info = f.readline().replace('ORGANISM', '').strip()

            if organism_info != '':
                organism_g = organism_info.split()[0]
                g_full_lineage = tax_lineage_dict.get(organism_g, ('g__' + organism_g))
                full_lineage_str = '%s;s__%s' % (g_full_lineage, organism_info)

        if len(tax_lineage_dict) == 0:
            if organism_info != '':
                op_txt_handle.write('%s\t%s\n' % (accession_id, organism_info))
        else:
            if full_lineage_str != '':
                op_txt_handle.write('%s\t%s\n' % (accession_id, full_lineage_str))
    op_txt_handle.close()


def combine_esearch_op_voucher(op_dir, op_txt):

    file_re = '%s/*_voucher.txt' % op_dir
    file_list = glob.glob(file_re)

    op_txt_handle = open(op_txt, 'w')
    for each_file in file_list:
        f_name, f_path, f_base, f_ext = sep_path_basename_ext(each_file)
        accession_id = f_base.split('_voucher')[0]

        voucher_info = ''
        with open(each_file) as f:
            #voucher_info = f.readline().replace('ORGANISM', '').strip()
            voucher_info = f.readline().strip()
            if 'specimen_voucher=' in voucher_info:
                voucher_info = voucher_info.replace('/specimen_voucher="', '')[:-1]
        if voucher_info != '':
            op_txt_handle.write('%s\t%s\n' % (accession_id, voucher_info))
    op_txt_handle.close()


op_dir                      = '/Users/songweizhi/Desktop/aaa'
tax_file                    = '/Users/songweizhi/DB/taxdump_20250321/ncbi_taxonomy.txt'
tmp_dir                     = '%s/tmp'                      % op_dir
combined_fa                 = '%s/accession_sequence.fasta' % op_dir
combined_organism_info_txt  = '%s/accession_organism.txt'   % op_dir
combined_voucher_info_txt   = '%s/accession_voucher.txt'    % op_dir


tax_lineage_dict = dict()
for each_line in open(tax_file):
    each_line_split = each_line.strip().split('\t')
    tax_lineage_dict[each_line_split[0]] = each_line_split[1]

os.system('cat %s/*.fasta > %s' % (tmp_dir, combined_fa))
combine_esearch_op_organism(tmp_dir, tax_lineage_dict, combined_organism_info_txt)
combine_esearch_op_voucher(tmp_dir, combined_voucher_info_txt)
