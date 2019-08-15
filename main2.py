#coding=utf-8

import os
import sys
from datetime import datetime
import random

#random.randint(a,b)
#random.randshuffle(p)

sys_time = datetime.now().strftime("%Y%m%d")
filename = '日报_卞霏_'+sys_time + '.txt'

#the first item, 
phase1_1 = ['今日', '今天的']
chosen_phase1_1 = phase1_1[random.randint(0, len(phase1_1)-1)]

phase1_2 = ['备课内容为section%s, chapter%s。','完成了section%s, chapter%s的备课。','准备了section%s, chapter%s的课程。']
chosen_phase1_2 = phase1_2[random.randint(0, len(phase1_2)-1)]

phase1_3 = ['备课重点放在%s，','备课中着重考虑了%s，', '备课的主要着眼点在于%s，']
chosen_phase1_3 = phase1_3[random.randint(0, len(phase1_3)-1)]

phase1_4 = ['已在ppt中体现。','将会在课堂教学中强调。','已在备课中重点准备。']
chosen_phase1_4 = phase1_4[random.randint(0, len(phase1_4)-1)]

phase1_5 = ['整体备课进度良好。','备课进展顺利。','已完成今日备课进度。']
chosen_phase1_5 = phase1_5[random.randint(0, len(phase1_5)-1)]

#phase1 = [phase1_1, phase1_2, phase1_3, phase1_4]
phase1_section = raw_input('宝贝今天备了Section几呀:\n')
phase1_chapter = raw_input('宝贝今天备了chapter几呀:\n')
phase1_emphasis = raw_input('宝贝的备课的重点在哪里呀:\n')
phase1_other = raw_input('宝宝还有需要补充的吗:\n')

phase1 = chosen_phase1_1 + chosen_phase1_2%(phase1_section,phase1_chapter) if phase1_section!='no' else '' + chosen_phase1_3%phase1_emphasis if phase1_emphasis!= 'no' else '' + chosen_phase1_4 + chosen1_5 + '\n'

#print('第一部分完成啦～爱你～～')



#the second item

phase2_section = raw_input('宝贝今天讲了section几呀:\n')
phase2_chapter = raw_input('宝贝今天讲了chapter几呀:\n')
phase2_emphasis = raw_input('宝贝的讲课重点放在哪里了呀:\n')
phase2_cond = raw_input('学生们掌握情况怎么样呀，有什么问题吗:\n')
phase2_problem = raw_input('宝宝对教学效果满意吗:\n')
phase2_other = raw_input('宝贝还有几点需要补充呀:\n')
phase2_other_num = int(phase2_other)

phase2_other_str = []
for i in range(phase2_other_num):
	phase2_other_str.append(raw_input('第%s条：\n'%i))



phase2_1 = ['section%s，chapter%s的进度良好。', '完成了section%s,chapter%s的教学。', '进展相对顺利，完成了section%s,chapter%s。']
chosen_phase2_1 = phase2_1[random.randint(0, len(phase2_1)-1)]%phase2_section if phase2_section!= 'no' else ''

phase2_2 = ['%s需着重讲解','学生们对%s的理解还不到位']
chosen_phase2_2 = phase2_2[random.randint(0, len(phase2_2)-1)] if phase2_emphasis!='no' else ''

phase2_3 = ['学生们掌握情况%s', '学生们掌握得%s', '同学们学得%s']
chosen_phase2_3 = phase2_3[random.randint(0, len(phase2_3)-1)]

phase2_4 = ['教学效果比较%s', '今天的教学效果还%s', '今天的课堂教学比较%s', '教学效果很%s']
chosen_phase2_4 = phase2_4[random.randint(0, len(phase2_4)-1)]

#phase2_5 = ['学生掌握情况整体令人满意','学生们表现出了浓厚的兴趣','作为教师对课堂效果基本满意','学生掌握情况尚可']
#chosen_phase2_5 = phase2_5[random.randint(0, len(phase2_5)-1)]


phase2 = []
if phase2_section!= 'no':
	phase2.append(chosen_phase2_1)
if phase2_emphasis != 'no':
	phase2_emphasis.append(chosen_phase2_2)
if phase2_cond != 'no':
	phase2_cond.append(chosen_phase2_3)
if phase2_problem != 'no':
	phase2_problem.append(chosen_phase2_4)
phase2.append()
	



#the third item
phase3_1 = ['学生们全部到齐。','学生今日全部出勤。']
phase3_12 = ['学生除%s外全部到齐。', '除了%s请假，其他同学全部到齐。']
all_guys = raw_input('同学们都到齐了吗：\n')
chosen_phase3_1 = ''
if all_guys == 'yes':
	chosen_phase3_1 = phase3_1[random.randint(0, len(phase3_1)-1)]
else:
	who_absent = raw_input('谁今天没到呀：\n')
	chosen_phase3_1 = phase3_12[random.randint(0, len(phase3_12)-1)]


phase3_2 = ['%s同学作业中存在问题，已指出。','%s同学的作业完成情况不够理想，已批改提醒。']
who_good = raw_input('谁的作业完成不好呀\n')
chosen_phase3_2 = phase3_2[random.randint(0, len(phase3_2)-1)]%who_good if who_good != 'no' else ''

phase3_3 = ['%s同学作业完成情况非常理想。','%同学作业完成情况良好，已表扬。', '%s同学的作业完成情况非常好。']
who_bad = raw_input('谁的作业完成还不错呀\n')
chosen_phase3_3 = phase3_3[random.randint(0, len(phase3_3)-1)]%who_bad if who_bad!= 'no' else ''

phase3 = chosen_phase3_1 + chosen_phase3_2 + chosen_phase3_3 + '\n'


#the forth item
phase4_1 = ['提醒了%s同学关于%s的问题','与%s同学交流了关于%s的问题']

phase4_2 = ['%s同学%s，提出表扬', '表扬了%s同学%s']
phase4_3 = ['与%s同学的家长交流了%s的问题','和%s同学的家长通报了%s']

phase4 = []

phase4_remind = raw_input('提醒了几个同学呀\n')
for i in range(int(phase4_remind)):
	chosen_phase4_1 = phase4_1(random.randint(0, len(phase4_1)-1))
	who_reminded = raw_input('提醒了谁呀\n')
	what_reminded = raw_input('什么事呀\n')
	phase4.append(chosen_phase4_1%(who_reminded, what_reminded))


phase4_praise = raw_input('表扬了几个同学呀\n')
for i in range(int(phase4_praise)):
	chosen_phase4_2 = phase4_2(random.randint(0, len(phase4_2)-1))
	who_praised = raw_input('表扬了谁呀\n')
	what_praised = raw_input('什么事呀\n')
	phase4.append(chosen_phase4_2%(who_praised, what_praised))
	
phase4_parent = raw_input('和几个同学家长交流了呀\n')
for i in range(int(phase4_parent)):
	chosen_phase4_3 = phase4_3(random.randint(0, len(phase4_3)-1))
	who_parent = raw_input('和谁的家长交流了呀\n')
	what_parent = raw_input('什么事呀\n')
	phase4.append(chosen_phase4_3%(who_parent, what_parent))

#the fifth item
phase5_pre = raw_input('宝宝先选择有哪些问题：1，午休，2，课堂纪律，3，迟到，4，作业完成情况，5，注意力不集中，6，没有预习.\n')

phase5 = []

phase5_1 = ['%s同学午休不足，上课精神不足','%同学午休不够，上课瞌睡']
chosen_phase5_1 = phase5_1[random.randint(0, len(phase5_1)-1)]

phase5_2 = ['%s同学不遵守课堂纪律','%s同学不遵守纪律，影响了其他同学']
chosen_phase5_2 = phase5_2[random.randint(0, len(phase5_2)-1)]

phase5_3 = ['%s同学上课迟到了几分钟','%s同学没有准时上课']
chosen_phase5_3 = phase5_3[random.randint(0, len(phase5_3)-1)]

phase5_4 = ['%s同学作业完成情况不太理想','%s同学作业完成不到位']
chosen_phase5_4 = phase5_4[random.randint(0, len(phase5_4)-1)]

phase5_5 = ['%s同学上课开小差', '%同学上课注意力不集中']
chosen_phase5_5 = phase5_5[random.randint(0, len(phase5_5)-1)]

phase5_6 = ['%s同学没有提前预习','%同学课程预习不到位']
chosen_phase5_6 = phase5_6[random.randint(0, len(phase5_6)-1)]

for p in phase5_pre:
	if p == '1':
		sleep = raw_input('谁没午休呀\n')
		phase5.append(chosen_phase5_1%sleep)
	elif p == '2':
		violate = raw_input('谁不遵守纪律呀\n')
		phase5.append(chosen_phase5_2%violate)
	elif p == '3':
		late = raw_input('谁迟到了呀\n')
		phase5.append(chosen_phase5_3%late)
	elif p == '4':
		homework = raw_input('谁作业完成不理想呀\n')
		phase5.append(chosen_phase5_4%homework)
	elif p == '5':
		focus = raw_input('谁开小差了呀\n')
		phase5.append(chosen_phase5_5%focus)
	else:
		preview = raw_input('谁没有预习呀\n')
		phase5.append(chosen_phase5_6%preview)


phase5_post = raw_input('宝宝还要自己输入几条问题呀：\n')
for i in range(int(phase5_post)):
	phase5_other = raw_input('输入一条吧：\n')
	phase5.append(phase5_other)

#the sixth item
phase6_1 = []

with open(filename, 'w') as f:
	f.write(sys_time + ' 卞霏 工作日志\n')
	f.write('一、备课内容、进度\n')
	f.write(phase_1)
	f.write('\n')

	f.write('二、教学及课堂\n')
	random.shuffle(phase_2)
	i = 1
	for str_2 in phase_2:
		str_22 = str(i) + '、' + phase_2[i-1] + '\n'
		i = i + 1
		f.write(str_22)
	f.write('\n')

	
	f.write('三、学生考勤和作业和测试情况\n')
	f.write(phase_3)
	f.write('\n')


	f.write('四、学生沟通&家长沟通\n')
	random.shuffle(phase_4)
	i = 1
	for str_4 in phase_4:
		str_44 = str(i) + '、' + phase_4[i-1]  + '\n'
		i = i + 1
		f.write(str_44)
	f.write('\n')


	f.write('五、班级问题\n')
	random.shuffle(phase_5)
	i = 1
	for str_5 in phase_5:
		str_55 = str(i) + '、' + phase_5[i-1] + '\n'
		i = i + 1
		f.write(str_55)
	f.write('\n')

	f.write('六、其他工作和问题\n')

