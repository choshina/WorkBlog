#coding=utf-8

import os
import sys
from datetime import datetime
import random

#random.randint(a,b)
#random.randshuffle(p)

sys_time = datetime.now().strftime("%Y%m%d")
filename = '日报_卞霏_'+sys_time + '.txt'

with open(filename, 'w') as f:
	f.write(sys_time + ' 卞霏 工作日志\n')
	f.write('一、备课内容、进度\n')
#	n_1 = random.randint(3,5)
#	list_1 = []
#	for i in range(n_1):
#		list_1.append('')
#	random.randshuffle(list_1)
#	i = 1
#	for str_1 in list_1:
#		str_11 = str(i) + '、' + list_1[i-1]
#		i = i + 1
#		f.write(str_11)

	f.write('二、教学及课堂\n')
	n_2 = random.randint(3,5)
	list_2 = []
	for i in range(n_2):
		list_2.append('')
	random.randshuffle(list_2)
	i = 1
	for str_2 in list_2:
		str_22 = str(i) + '、' + list_2[i-1] + '\n'
		i = i + 1
		f.write(str_22)
	
	f.write('三、学生考勤和作业和测试情况\n')
	
	f.write('四、学生沟通&家长沟通\n')
	n_4 = random.randint(3,5)
	list_4 = []
	for i in range(n_4):
		list_4.append()
	random.randshuffle(list_4)
	i = 1
	for str_4 in list_4:
		str_44 = str(i) + '、' + list_4[i-1]
		i = i + 1
		f.write(str_44)

	f.write('五、班级问题\n')
	n_5 = random.randint(3,5)
	list_5 = []
	for i in range(n_5):
		list_5.append()
	random.randshuffle(list_5)
	i = 1
	for str_5 in list_5:
		str_55 = str(i) + '、' + list_5[i-1]
		i = i + 1
		f.write(str_55)

	f.write('六、其他工作和问题\n')

