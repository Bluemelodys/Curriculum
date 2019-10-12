dict_temp = {}

# 打开文本文件
file = open('GB.txt','r')

# 遍历文本文件的每一行，strip可以移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
for line in file.readlines():
    line = line.strip()
    k = line.split('\t')[0]
    v = line.split('\t')[1]
    dict_temp[k] = v



#  可以打印出来瞅瞅
print(dict_temp)
print(dict_temp['110000'])