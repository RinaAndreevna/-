import os
from typing import List

file_list = ['1.txt', '2.txt', '3.txt']
new_file_list = ['n1.txt', 'n2.txt', 'n3.txt']
new_data_from_files = []
step = 0
while step < len(file_list):
    for some_file in file_list:
        with open(file_list[step], encoding='utf -8') as f:
            data = f.readlines()
            qvon_str = len(data)
        with open(file_list[step], encoding='utf -8') as f:
            data_text = f.read()

    for some_file in new_file_list:
        with open(new_file_list[step], 'w', encoding='utf -8') as f:
            f.write(f'{file_list[step]}\n')
            f.write(f'{qvon_str}\n')
            f.write(f'{data_text}\n')
    step += 1
for some_file in new_file_list:
    with open(some_file) as f:
        new_data = f.read()
        new_data_from_files.append(new_data)
new_data_from_files.sort(key=len)
sorted(new_data_from_files, key=len)
print(new_data_from_files)

with open('finish_file.txt', 'a', encoding='utf -8') as f:
    for some_pat in new_data_from_files:
        f.write(f'{some_pat}')
