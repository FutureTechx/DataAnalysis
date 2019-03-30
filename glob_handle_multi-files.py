'''# 1 glob 简介：
#   1）使用glob读取多个文本文件
#   2）glob 模块之所以强大就是因为他处理的是文件夹
# solution:
# 读取多个文件的一种方法是在命令行中包含输入文件目录的路径写在python脚本名称之后
# 创建一个文本文件，包含几个txt文件
'''

import sys
import glob
import os

inputPath = sys.argv[1]

for input_file in glob.glob(os.path.join(inputPath,"*.txt")):
    with open(input_file,'r',newline='') as f:
        for row in f:
            print("{}".format(row.strip))



# cmd :jianchaos-MacBook-Pro:DataAnalysis t_maj$ python glob_handle_multi-files.py multi-files/
'''output:
multi-files/
life is short
I use python
I like Python
life is long
I use C++
I like C++
'''