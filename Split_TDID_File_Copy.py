#coding:utf-8

from adding_data import list_name_with_first_word
import os

# 建立与待拆分文件的文件名相一致的文件夹
# 文件夹下存放以字符串首字母为名以剩余字符为内容的字符串文件
# 以此类推

# create_dir_with_file_name_and_split_file_with_first_word
def CreateDir_SplitFile(path_source_file):
    # 以 asd_somple_201601 文件为例
    #print path_source_file
    path_dir_with_file_name = path_source_file[:-4]
    #print path_dir_with_file_name
    os.mkdir(path_dir_with_file_name)

    for name_with_first_word in list_name_with_first_word:
	# ./asd_sample_201601/0.txt
	#print path_dir_with_file_name + '/' + name_with_first_word + '.txt' 
	#print path_source_file

	with open(path_dir_with_file_name + '/' + name_with_first_word + '.txt' , 'wb') as f1:
	    with open(path_source_file, 'rb') as f2:
		for l in f2:
		    if l[0] == name_with_first_word:
			f1.write(l[1:])
	f1.close()

# 待拆分文件及路径
path_source_file = '/Users/Alas/Documents/TalkingData/non_daily/asd_sample_201601-201611/asd_sample/' + \
	    'asd_sample_201611.txt'
# 拆分一次
CreateDir_SplitFile(path_source_file)
# 迭代一次 拆分二次(不够)
for s in list_name_with_first_word:
    path_iteration_1 = path_source_file[:-4] + '/' + s + '.txt'
    #print path_iteration_1
    CreateDir_SplitFile(path_iteration_1) 
    os.remove(path_iteration_1)
    # 迭代两次 拆分三次
    for s in list_name_with_first_word:
	path_iteration_2 = path_iteration_1[:-4] + '/' + s + '.txt'
	#print path_iteration_2
	CreateDir_SplitFile(path_iteration_2)
	os.remove(path_iteration_2)
	# 迭代三次 拆分四次
	for s in list_name_with_first_word:
	    path_iteration_3 = path_iteration_2[:-4] + '/' + s + '.txt'
	    #print path_iteration_3
	    CreateDir_SplitFile(path_iteration_3)
	    os.remove(path_iteration_3)




