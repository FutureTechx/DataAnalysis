## CSV
又叫逗号分隔值，是一种非常简单的存储文件格式，csv将数据表格存储为纯文本，表格中的每一个单元都是一个字符串/数字
### 优点
很多程序都可以存储，转换和处理纯文本文件
### 缺点
CSV只能保存数据，不能保公式式，但是通常将数据存储（CSV文件）和数据处理（Python脚本）分离
## 基础python读取CSV，不适用模块
两个with，一个读取，一个写，more info: ReadCSVwithPython.py
’‘’python
with open(input_file, 'r') as filereader:
	with open(output_file, 'w') as filewriter:
		header = filereader.readline()
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
        //map将str函数应用于header_list的每一个元素，确保每个元素都是字符串
		filewriter.write(','.join(map(str,header_list))+'\n') 
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')
'''
### 使用csv模块
more info: csv_modul_handle.py
相比第一个的优点：可以正确处理数值中的嵌入逗号和其他复杂模式。从而正确的分析数据。
‘’‘python
        with open(input_file, 'r', newline='') as csv_in_file:
            with open(output_file, 'w', newline='') as csv_out_file:
                filereader = csv.reader(csv_in_file, delimiter=',') //第二个参数是默认分隔符，默认是逗号
                filewriter = csv.writer(csv_out_file, delimiter=',')
                for row_list in filereader:
                    filewriter.writerow(row_list)

## pandas 处理CSV文件
data_frame 是一种数据存储的方式，数据框中保留了”表格“，不需要用列表嵌套的形式分析数据
more info: pandas_parsing_and_write.py
’‘’python
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file,index=False)
'''
## 筛选特定的行
有时候并不需要所有的数据，有三种方法筛选特定的行：
1）行中的值满足某个条件
2）行中的值属于某个集合
3）行中的值匹配某个模式（正则表达式
### 1 行中的值满足某个条件
#### 1.1 基础python
有时候当行中的值满足一个条件时，才需要保留这些行
下面是验证行值是否满足具体条件，并把满足条件的行的子集写到一个输出文件中。
保留供应商是Supplier Z 或者成本大于￥600.0
’‘’python
with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader) # csv的next函数读出文件的第一行
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			cost = str(row_list[3]).strip('$').replace(',', '') #去除美元符号，，删除逗号
			if supplier == 'Supplier Z' or float(cost) > 600.0:
				filewriter.writerow(row_list)
'''
#### 1.2 pandas
pandas 提供了一个loc函数，可以同时选取特定的行和列，你需要在逗号前面设定行筛选条件，在逗号后设定列筛选条件。
‘’‘ python
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)
'''
### 行中的值属于某个集合
当行中的值属于某个集合时，才保留这些行。
’‘’ python
important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			a_date = row_list[4]
			if a_date in important_dates:
				filewriter.writerow(row_list)
'''
