#coding:utf-8
import os
import pandas as pd
from openpyxl import Workbook
from adding_data import list_app_name, trans_month

path_target_dir = '/Users/Alas/Documents/TalkingData/non_daily/asd_sample_201601-201611/fixed_asd_associated_apps/'
list_file_name = os.listdir(path_target_dir)
list_file_name.remove('.DS_Store')
list_file_name.remove('hand_in')
#print list_file_name

# 依次计算每月(文件)的中所有指定应用的
# 月安装量和月活跃量列表
# 月安装比例和月活跃比例列表
with open('test.csv', 'wb') as f1:
    # 写入表头信息
    to_write_strings = 'month' + ',' + 'asd' + ',' + 'Index' + ','
    for info in list_app_name:
	to_write_strings += (info + ',')
    to_write_strings += '\n'
    f1.write(to_write_strings)

    for file_name in list_file_name:
	df = pd.read_csv(path_target_dir + file_name, names=['Apps', 'MIns', 'MAU',])
	# 得到此批TDID关联应用中是基于哪个总量的值
	try:
	    asd = df[df['Apps']=='all']['MIns'].values[0]
	    #print asd
	except Exception, e:
	    print file_name, '\tasd\t', e

	# 得到指定APP的月安装量与月活跃量列表
	# 若根据名字得到的记录不只一条, 那么只选择排名最前的那条
	list_app_mins = []
	list_app_mau = []
	for app in list_app_name:
	    try: # 可能因为名字不匹配导致的查找不到
		list_app_mins_mau = list(df[df['Apps']==app][:1].values[0])
		# 输出该应用的名字、月安装量、月活跃量
		#for x in list_app_mins_mau:
		    #print x,
		#print '\r'
		# 将存放于一个列表的月安装和月活分开存放
		# 得到指定应用的月安装量和月活跃量列表
		list_app_mins.append(list_app_mins_mau[1])
		list_app_mau.append(list_app_mins_mau[2])
	    except Exception, e:
		print app, '\tlist_app_mins_mau\t', e
		continue
	# 得到指定应用的月安装比例和月活跃比例列表
	list_app_minspr = [s*1.0/asd for s in list_app_mins]
	list_app_maupr = [s*1.0/asd for s in list_app_mau]



	# 输出该月文件|文件名|中所有指定应用的|总活跃设备量|应用名列表|
	# |月安装量列表|月活跃量列表|月安装比例列表|月活跃比例列表|
	date = trans_month[file_name[19:24]]

	to_write_strings = date + ',' + str(asd) + ',' + 'MIns' + ','
	for info in list_app_mins:
	    to_write_strings += (str(info) + ',')
	to_write_strings += '\n'
	f1.write(to_write_strings)

	to_write_strings = date + ',' + str(asd) + ',' + 'MAU' + ','
	for info in list_app_mau:
	    to_write_strings += (str(info) + ',')
	to_write_strings += '\n'
	f1.write(to_write_strings)

	to_write_strings = date + ',' + str(asd) + ',' + 'MInsPR' + ','
	for info in list_app_minspr:
	    to_write_strings += (str(info) + ',')
	to_write_strings += '\n'
	f1.write(to_write_strings)

	to_write_strings = date + ',' + str(asd) + ',' + 'MAUPR' + ','
	for info in list_app_maupr:
	    to_write_strings += (str(info) + ',')
	to_write_strings += '\n'
	f1.write(to_write_strings)
    





