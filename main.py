import os
from pprint import pprint

def get_files_data(files_list):
    if len(files_list) > 0:
        files_data = []
        for file in files_list:
            # files_data.append({'file_name': file_name})
            file_info = {'file_name': file}
            with open(file, 'r', encoding='utf-8') as f:
                file_lines = f.readlines()
                print(file_lines)
                file_info['lines_quantity'] = len(file_lines)
                file_info['lines_list'] = file_lines
                # for line in file_lines:
                #     file_info['lines_list'].append()
            files_data.append(file_info)
        # pprint(files_data)
        return files_data
    else:
        print('Список файлов пустой')
        return

def unite_files(files_list):
    files_data = get_files_data(files_list)
    if files_data != None:
        sorted_list = sorted(files_data, key=lambda k: k['lines_quantity'])
        # pprint('========SORTED======')
        # pprint(sorted_list)
        with open('my_file.txt', 'w+', encoding='utf-8') as f:
            first_line = True
            for file_data in sorted_list:
                if first_line:
                    first_line = False
                else:
                    f.write('\n')

                f.write(file_data['file_name'] + '\n')
                f.write(str(file_data['lines_quantity']) + '\n')
                f.write(''.join(file_data['lines_list']))




if __name__ == '__main__':
    files_list = ['1.txt','2.txt','3.txt']
    unite_files(files_list)