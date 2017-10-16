#coding:utf-8

path_source_file = '/Users/Alas/Documents/TalkingData/non_daily/asd_sample_201601-201611/asd_sample/' + \
            'asd_sample_201601.txt'

# 统计某文件经过拆分后, 所有子文件记录数之和是否等于源文件记录数
list_name_with_first_word = [str(i) for i in range(10)] + [chr(s) for s in range(97, 123)]
for s in list_name_with_first_word:
    path_iteration_1 = path_source_file[:-4] + '/' + s + '.txt'
    #print path_iteration_1
    with open(path_iteration_1) as f:
	





"""
# 得到某文件首字符的集合, 验证是否在 list_name_with_first_word 中
set_first_word = set()
with open(path_source_file) as f:
    for l in f:
	set_first_word.add(l[0])
print set_first_word
"""
