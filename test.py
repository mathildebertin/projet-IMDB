import csv
import pandas


def open_tsv_file(file_title):
    tsv_open = open(file_title)
    return csv.reader(tsv_open, delimiter="\t")


def convert_dicts_to_lists(list_of_dicts):
    key_list = []
    list_of_lists = []
    for key in list_of_dicts[0]:
        key_list.append(key)
    for _dict in list_of_dicts:
        row_list_of_lists = []
        for key in key_list:
            row_list_of_lists.append(_dict[key])
        list_of_lists.append(row_list_of_lists)
    return list_of_lists


def create_dict_from_tsv(file, index_1, index_2):
    _dict = {}
    for row_file in file:
        _dict[row_file[index_1]] = row_file[index_2]
    return _dict

read_title = open_tsv_file("title.basics.tsv")

with open('title.series.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for row_title in read_title:
        if row_title[1] == 'tvSeries':
            tsv_writer.writerow([row_title[0], row_title[2]])

