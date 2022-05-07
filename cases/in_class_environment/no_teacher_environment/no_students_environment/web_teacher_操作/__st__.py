"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/07
@File   :__st__.py
"""
from hytest import *
from cfg.cfg import *
from lib.api.yjyx_teacher_api import gs_teacher
from lib.webUI.yjyx_webui_teacher_operation import teacher_operation
from lib.api.yjyx_student_api import gs_student
from lib.api.yjyx_class_api import gs_class
import time

# 套件初始化方法
def suite_setup():
	# 班级id
	cid = GSTORE['id']
	STEP(1, '添加老师')
	res_add_teacher = gs_teacher.add_teachers('web_yuer', '老师数学老师-文跃锐',
	                                          SUBJECT_ID_HIGH_MATH, str(cid),
	                                          '13553896530', 'yuerwen@123.com',
	                                          '32092519830907899')
	ret_add_teacher_json_obj = res_add_teacher.json()
	
	# ** 保存id，存到self中，self是实例对象都能访问到的东西
	addTeacherId = ret_add_teacher_json_obj['id']
	GSTORE['addTeacherId'] = addTeacherId
	
# 清除方法
def suite_teardown():
	gs_teacher.del_teachers(GSTORE['addTeacherId'])
	teacher_operation.close_chrome()