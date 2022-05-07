"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/03
@File   :teacher_operation.py
"""
from hytest import *
from cfg.cfg import *
from lib.api.yjyx_teacher_api import gs_teacher
from lib.webUI.yjyx_webui_teacher_operation import teacher_operation
from lib.api.yjyx_student_api import gs_student
from lib.api.yjyx_class_api import gs_class
import time

# 清除方法
# def suite_teardown():
	# gs_teacher.del_teachers(GSTORE['addTeacherId'])
	# teacher_operation.close_chrome()  # 关闭浏览器
	
class Case_tc005001:
	name = '老师登录1 - tc005001'
	
	def teststeps(self):
		
		# 测试步骤如下
		
		STEP(1,'登录老师系统')
		teacher_operation.teacher_login('web_yuer')
		home_page_info_list = teacher_operation.get_home_page_info()
		INFO(home_page_info_list)
		expected = ['白月学院00002', '老师数学老师-文跃锐', '高中数学', '0', '0', '0']
		CHECK_POINT('检查首页信息',expected == home_page_info_list)
		
		STEP(2,'点击 班级学生 菜单')
		class_student_info = teacher_operation.get_class_student_info()
		INFO(class_student_info)
		expected = '该班级还没有学生注册'
		CHECK_POINT('检查班级学生信息',class_student_info == expected)
		

class Case_tc005002:
	name = '老师登录2 - tc005002'
	
	# 初始化方法
	def setup(self):
		cid = GSTORE['id']
		result_add_student = gs_student.add_students(
			'laoliu', '老六', SENIOR_THREE_GRADE_ID, cid, '1345166666')
		GSTORE['student_id'] = result_add_student.json()['id']
		
	# 清除方法
	def teardown(self):
		gs_student.del_students(GSTORE['student_id'])
	
	def teststeps(self):
		
		# 测试步骤如下
		STEP(1, '检查首页信息')
		home_page_info_list = teacher_operation.get_home_page_info()
		INFO(home_page_info_list)
		expected = ['白月学院00002', '老师数学老师-文跃锐', '高中数学', '0', '0', '0']
		CHECK_POINT('检查首页信息', expected == home_page_info_list)
		
		STEP(2, '点击 班级学生 菜单')
		teacher_operation.web_driver_refresh()
		class_student_info = teacher_operation.get_class_student_info()
		student_name = class_student_info.replace('\n', ' ').replace(' ', ',').split('|')[-1].split(',')[-4]
		INFO(student_name)
		expected = '老六'
		CHECK_POINT('检查班级学生信息', student_name == expected)
		
		

		