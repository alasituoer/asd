#coding:utf-8
import pandas as pd

df = pd.read_csv('nov16_yinyangshi.csv', names=['TDID'])

# 对TDID排序后导入新的CSV文件
#df.sort_values(by='TDID',)
#df['TDID'].to_csv('sorted_nov16_yinyngshi.csv', index=False)

df_t1 = df[:20000]
print df_t1, '\n'
#df_t2 = df_t1.sort_values(by='TDID')
#print df_t2

# 得到根据首字母拆分出来的 pd.Series 数据类型
def get_ss_fw(df):
    first_word_set = set()
    for i in range(len(df)):
	#print df.ix[i]['TDID']
	first_word_set.add(df.ix[i]['TDID'][:1])
    #print first_word_set

    # 依照顺序存放的首字母列表
    fw_list = []
    # 根据首字母不同而分类的TDID列表
    no_fw_tdid_list = []

    for j in first_word_set:
	for i in range(len(df)):
	    if df.ix[i]['TDID'][:1] == j:
		fw_list.append(j)
		no_fw_tdid_list.append(df.ix[i]['TDID'][1:])
	#print pd.DataFrame(no_fw_tdid_list, columns=[j])
    #print fw_list
    #print no_fw_tdid_list

    ss = pd.Series(no_fw_tdid_list, index=fw_list)
    return ss

# 根据第一个字母分类
ss_fw = get_ss_fw(df_t1)
for i in ss_fw.index.unique():
    print i
    try:
	print ss_fw[i].values
    except:
	print ss_fw[i]
    
    df_t3 = pd.DataFrame(ss_fw[i].values, columns=['TDID'])
    # 在第一个字母已分类的情况下，再根据第二个字母分类
    ss_sw = get_ss_fw(df_t3)
    print ss_sw
    for j in ss_sw.index.unique():
	print j
	try:
	    print ss_sw[j].values
	except:
	    print ss_sw[j]
    print '\n'



