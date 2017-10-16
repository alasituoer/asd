#coding:utf-8
import pandas as pd
from adding_data import list_name_with_first_word

# 从经过拆分后的两个或多个文件中得到TDID交集

# 存放拆分文件的路径
source_path = '/Users/Alas/Documents/TalkingData/non_daily/asd_sample_201601-201611/asd_sample/'
# 拆分文件形成的文件夹名
dir_t1 = 'asd_sample_201601_201602_201603_201604_201605_201606_201607_201608_201609'
dir_t2 = 'asd_sample_201610'
# 上述TDID文件夹的TDID交集文件
final_file_name = 'asd_sample_' + dir_t1[11:] + '_' + dir_t2[11:] + '.txt'
#print final_file_name

with open(source_path + final_file_name, 'wb') as to_write_file:
    # 循环取得以TDID第一个字母为名的文件或文件夹: i
    for i in list_name_with_first_word:
	# 循环取得以TDID第二个字母为名的文件或文件夹: j
	for j in list_name_with_first_word:
	    for k in list_name_with_first_word:
		for l in list_name_with_first_word:
		    path_t1 = source_path + dir_t1 + \
				'/' + i + '/' + j + '/' + k + '/' + l + '.txt'
		    path_t2 = source_path + dir_t2 + \
				'/' + i + '/' + j + '/' + k + '/' + l + '.txt'
		    # 读入待比较的两个文件, 加上字段名
		    df_t1 = pd.read_csv(path_t1, names=['TDID'])
		    df_t2 = pd.read_csv(path_t2, names=['TDID'])
		    #print i, j, k, l
		    #print df_t1[:10]
		    #print df_t2[:10]
		    #print df_t2[:10]['TDID'].values

		    # 此处以较少循环次数选择待比较文件
		    # 循环得到第一个文件中的每一条记录
		    for r in df_t1['TDID']:
		    # 接着判断该记录是否在剩余文件中
			if r in df_t2['TDID'].values:
			    # 如果在, 则将其重构成完整的TDID存入结果文件
#			    print i + j + k + l + r
			    # 文件夹名同时也是路径名, 文件名同时也是TDID的一部分
			    to_write_file.write(i + j + k + l + str(r))
			    to_write_file.write('\n')
to_write_file.close()





