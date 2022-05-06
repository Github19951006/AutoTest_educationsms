"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/05
@File   :student_operation.py
"""
from hytest import *
from cfg.cfg import *
from lib.webUI.yjyx_webui_student_operation import student_operation
from lib.api.yjyx_student_api import gs_student
import time

# 根据标签挑选
force_tags = ['管理员登录','系统测试','UI测试','UI-StuLg000X']

class Case_tc005081:
	name = '学生登录1 - tc005081'
	
	# 清除方法
	def teardown(self):
		student_operation.student_sign_out()
	
	def teststeps(self):
		
		# 测试步骤如下
		STEP(1, '登录学生系统')
		student_operation.student_login('student_yuer')
		home_page_info_list = student_operation.get_home_page_info()
		INFO(home_page_info_list)
		# 获取注册码
		expected = ['精锐', '白月学院00002', f'{home_page_info_list[-3]}', '0', '0']
		CHECK_POINT('检查首页信息',expected == home_page_info_list)
		
		STEP(2, '点击 错题库 菜单')
		wrong_question_lib_info = student_operation.get_wrong_question_lib_info()
		INFO(wrong_question_lib_info)
		expected = '您尚未有错题入库哦'
		CHECK_POINT('检查错题入库信息', wrong_question_lib_info == expected)


class Case_StuLg000X:
	
	ddt_cases = [
		{
			'name': '学生登录 不输入账号 - UI-StuLg001',
			'para': [None, '888888', '登录失败 : 用户或者密码错误']
		},
		{
			'name': '学生登录 不输入密码 - UI-StuLg002',
			'para': ['student_yuer', None, '登录失败 : 用户或者密码错误']
		},
		{
			'name': '学生登录 输入错误账号 - UI-StuLg003',
			'para': ['student', '88888888', '登录失败 : 用户或者密码错误']
		},
		{
			'name': '学生登录 输入错误密码 - UI-StuLg004',
			'para': ['student_yuer', '666666', '登录失败 : 用户或者密码错误']
		},
		{
			'name': '学生登录 输入错误密码 - UI-StuLg005',
			'para': [None, None, '登录失败 : 用户或者密码错误']
		}
	]
	
	def teststeps(self):
		
		# 取出参数
		username, password,tips = self.para
		
		# 测试步骤如下
		STEP(1, '登录学生系统')
		student_operation.student_login(username,password)
		tips_info = student_operation.get_tips_info()
		INFO(tips_info)
		CHECK_POINT('检查提示信息',tips_info == tips)