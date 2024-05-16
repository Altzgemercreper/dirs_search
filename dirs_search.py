import subprocess  
import time

t_dir_0 = time.time()

dirs = []  
result_files = []  

for dir in dirs:  
    # запуск внешней команды для получения списка файлов в указанном каталоге и всех его подкаталогах
    # с фильтрацией по размеру файла от 0 до 134217728 байт (128 Мб) и сохранение имени последнего элемента в список files
    files = subprocess.check_output(f"hdfs dfs -ls -R {dir}" + "| awk '$5 >0 && $5 < 134217728  {print $NF}'", shell=True, universal_newlines=True).strip().split()
    files.extend(result_files)  

def truncate_str(input_list):  
    truncated_list = [s[:s.rfind('/') + 1] for s in input_list]  
    return truncated_list  

truncated_list = truncate_str(result_files)  

count_dict = {}  

for s in truncated_list: 
    if s in count_dict:  
        count_dict[s] += 1  
    else:  
        count_dict[s] = 1  
        
# определение списка дубликатов из словаря count_dict
duplicates = [i for i, s in count_dict.items() if s > 1]

spisok = duplicates

a_spisok = []

n_spisok = []

for word in spisok:
    if "dom" in word:
        a_spisok.append(word)
    else:
        n_spisok.append(word)

if '' in n_spisok:
    n_spisok.remove('')
    
if '' in a_spisok:
    a_spisok.remove('')


dirs_n = []
duplicates_n = n_spisok

for p in duplicates_n:
    dil = p.split('/')[6]
    dirs_n.append(dil)
    
dirs_n = set(dirs_n)

print('Way')
for way in duplicates_n:
    print(way)
    
print('Dirs')
for p in dirs_n:
    print(p)
    
final_list = []

final_way_list = a_spisok

final_way_list = set(final_way_list)

print('Way')
for x in final_way_list:
    print(x)
    

for d in a_spisok:
    duplicate_list = d.split('/')
    
    s2 = duplicate_list[2]
    s4 = duplicate_list[4]
    s5 = duplicate_list[5]
    s6 = duplicate_list[6]
    s7 = duplicate_list[7]
    s8 = duplicate_list[8]
    
    if s7 == "om":
        list_item = f'{s2}_{s4}_{s5}_{s6}.{s8}'
    elif s7 not in ["om", "pm", "im", "um", "ym", "tm", "rm", "em", "dm", "cm", "fm", "vm"]:
        s9 = duplicate_list[9]
        list_item = f'{s2}_{s4}_{s5}_{s6}_{s7}_{s8}.{s9}'
    else:
        list_item = f'{s2}_{s4}_{s5}_{s6}_{s7}.{s8}'
    
    final_list.append(list_item)
    
final_list = set(final_list)

print('схема.табличка')
for x in final_list:
    print(x)

t_dir_1 = time.time()
print('Время выполнения = ', round((t_dir_1 - t_dir_0)/60, 2))