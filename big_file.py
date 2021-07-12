from pprint import pprint
import os

folder_path = os.getcwd()

def mk_txt_files_list(this_folder_path):
    text_files_list = [f for f in os.listdir(folder_path) if  f.endswith('.txt')]
    return text_files_list


def mk_1_data_structure(text_files_list):
    data_structure = {}
    for file_name in text_files_list:
        file_path = os.getcwd() + "/" + file_name
        with open (file_path, "r", encoding="utf-8") as file:
            count_of_lines = 0
            for each_line in file:
                count_of_lines += 1
        with open(file_path, "r", encoding="utf-8") as file:
            data_structure[file_name] = {'count': count_of_lines, 'data': file.read()}

    return data_structure


def mk_data_structure(text_files_list):
    data_structure_count = {}
    for file_name in text_files_list:
        file_path = os.getcwd() + "/" + file_name
        with open(file_path, "r", encoding="utf-8") as file:
            count_of_lines = 0
            for each_line in file:
                count_of_lines += 1
            data_structure_count[file_name] = {'count': count_of_lines}

    return (data_structure_count)


def sort_structure(data_structure_to_order):
    print("data_structure", data_structure_to_order)
    new_structure = {}
    key_list = []
    for item in (data_structure_to_order.keys()):
        key_list.append(item)
    print('это список key_list', key_list)
    value_list = []
    for item in data_structure_to_order.values():
        value_list.append(item.get('count'))
    print('это список value_list', value_list)
    sorted_by_len = sorted(value_list)
    print('sorted_by_len', sorted_by_len)
    pair_structure = list(zip(value_list, key_list))
    pair_structure.sort(key=lambda x: (x[0], x[1]))
    res = [j for i, j in pair_structure]
    print('res', res)
    return res


def mk_big_file(order_structure, mk_data):
    print('mk_data', mk_data)
    big_file_path = os.getcwd() + "/big/big_file"
    print(big_file_path)
    big_str = ''
    for i in order_structure:
        str1 = f"{i}\n"
        str2 = f"{mk_data[i]['count']}\n"
        str3 = f"{mk_data[i]['data']}\n"
        big_str += str1 + str2 + str3
        with open(big_file_path, "w", encoding="utf-8") as file:
            file.write(big_str)
        with open(big_file_path, "r", encoding="utf-8") as file:
            data = file.read()
    return data



    #     print(big_file_path)
    #     with open(big_file_path, "w", encoding="utf-8") as file:
    #         file.write('1-str' + 'mk_data[pair_structure(1)]' + '\n')
    #     with open(big_file_path, "r", encoding="utf-8") as file:
    #         data = file.read()
    # return data


txt_list = mk_txt_files_list(folder_path)
print(txt_list)
structure1 = mk_1_data_structure(txt_list)
print('это структура', structure1)
structure = mk_data_structure(txt_list)
print("это structure", structure)


pair_structure_dat = sort_structure(structure)
print("это sort_structure", pair_structure_dat)
print(mk_big_file(pair_structure_dat, structure1))


