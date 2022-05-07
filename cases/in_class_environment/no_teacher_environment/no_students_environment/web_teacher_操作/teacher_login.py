"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/07
@File   :teacher_login.py
"""
from hytest import *
from lib.webUI.yjyx_webui_teacher_operation import teacher_operation

# 根据标签挑选
force_tags = ['老师登录','系统测试','UI测试','UI-teacherLg']

class Case_teacherLg00x:
	# 登录功能的数据驱动
	'''
	正确用户名 ：student_yuer
	正确密码   ：888888
	'''
	ddt_cases = [
		{
			'name': '老师登录 不输入账号 - UI-TeacherLg001',
			'para': [None, '888888', '登录失败 : 用户或者密码错误']
		},
		{
			'name': '老师登录 不输入密码 - UI-TeacherLg002',
			'para': ['web_yuer', None, '登录失败 : 用户或者密码错误']
		},
		{
			'name': '老师登录 输入错误账号 - UI-TeacherLg003',
			'para': ['student', '88888888', '登录失败 : 用户或者密码错误']
		},
		{
			'name': '老师登录 输入错误密码 - UI-TeacherLg004',
			'para': ['web_yuer', '666666', '登录失败 : 用户或者密码错误']
		},
		{
			'name': '老师登录 输入错误密码 - UI-TeacherLg005',
			'para': [None, None, '登录失败 : 用户或者密码错误']
		}
	]
	
	def teststeps(self):
		
		# 取出参数(变量解包)
		username, password, tips_info = self.para
		
		# 测试步骤如下
		STEP(1, '登录老师系统')
		teacher_operation.teacher_login(username, password)
		get_tips_info = teacher_operation.get_tips_info()
		INFO(get_tips_info)
		CHECK_POINT('检查错误提示信息', get_tips_info == tips_info)