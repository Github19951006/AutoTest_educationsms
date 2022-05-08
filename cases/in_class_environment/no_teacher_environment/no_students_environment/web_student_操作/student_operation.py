"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/05/05
@File   :student_operation.py
"""
from hytest import *
from lib.webUI.yjyx_webui_student_operation import student_operation

# 根据标签挑选
force_tags = ['学生登录','系统测试','UI测试','UI-StuLg000X']

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

	# 登录功能的数据驱动
	'''
	正确用户名 ：student_yuer
	正确密码   ：888888
	'''
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

		# 取出参数(变量解包)
		username, password,tips_info = self.para

		# 测试步骤如下
		STEP(1, '登录学生系统')
		student_operation.student_login(username,password)
		get_tips_info = student_operation.get_tips_info()
		INFO(get_tips_info)
		CHECK_POINT('检查错误提示信息',get_tips_info == tips_info)


# class Case_StuModif001:
# 	name = '学生登录 修改密码为8位 - UI-StuModify001'
#
# 	# 清除方法
# 	def teardown(self):
# 		student_operation.student_login('student_yuer', '999888')
# 		student_operation.modify_student_password('999888', '888888', '888888')
#
# 	def teststeps(self):
#
# 		# 测试步骤如下
# 		STEP(1, '登录学生系统')
# 		student_operation.student_login('student_yuer', '888888')
# 		STEP(2, '修改学生密码')
# 		student_operation.modify_student_password('888888','999888','999888')
# 		STEP(3,'获取提示信息')
# 		get_tips_info = student_operation.get_tips_info()
# 		tips_info = '用户密码修改成功，点击确定，重新登录'
# 		CHECK_POINT('检查错误提示信息', get_tips_info == tips_info)
# 		STEP(4, '重新登录学生系统')
# 		student_operation.student_login('student_yuer', '999888')
#
#
# class Case_StuModif002:
# 	name = '学生登录 修改密码为19位 - UI-StuModify002'
#
# 	# 清除方法
# 	def teardown(self):
# 		student_operation.student_login('student_yuer', '1234567890123456789')
# 		student_operation.modify_student_password('1234567890123456789', '888888', '888888')
#
# 	def teststeps(self):
# 		# 测试步骤如下
# 		STEP(1, '登录学生系统')
# 		student_operation.student_login('student_yuer', '888888')
# 		STEP(2, '修改学生密码')
# 		student_operation.modify_student_password('888888', '1234567890123456789', '1234567890123456789')
# 		STEP(3, '获取提示信息')
# 		get_tips_info = student_operation.get_tips_info()
# 		tips_info = '用户密码修改成功，点击确定，重新登录'
# 		CHECK_POINT('检查错误提示信息', get_tips_info == tips_info)
# 		STEP(4, '重新登录学生系统')
# 		student_operation.student_login('student_yuer', '1234567890123456789')

class Case_StuModif00x:
	
	# 修改密码功能的数据驱动
	'''
	正确用户名 ：student_yuer
	正确密码   ：888888
	'''
	ddt_cases = [
		{
			'name': '学生登录 密码为19位 - UI-StuModify001',
			'para': ['student_yuer', '999888', '999888', '用户密码修改成功，点击确定，重新登录']
		},
		{
			'name': '学生登录  密码为20位 - UI-StuModify002',
			'para': ['student_yuer', '1234567890123456789', '1234567890123456789', '用户密码修改成功，点击确定，重新登录']
		},
		{
			'name': '学生登录  密码为21位 - UI-StuModify003',
			'para': ['student_yuer', '1234567890123456789', '1234567890123456789', '用户密码修改成功，点击确定，重新登录']
		},
		{
			'name': '学生登录 密码包含英文 - UI-StuModify004',
			'para': ['student_yuer', 'password', 'password', '用户密码修改成功，点击确定，重新登录']
		},
		{
			'name': '学生登录 密码包含英文和数字 - UI-StuModify005',
			'para': ['student_yuer', 'password12345', 'password12345', '用户密码修改成功，点击确定，重新登录']
		},
		{
			'name': '学生登录 密码包含特殊字符 - UI-StuModify006',
			'para': ['student_yuer', '888%$@.,!', '888%$@.,!', '用户密码修改成功，点击确定，重新登录']
		},
		{
			'name': '学生登录 密码包含英文和数字 - UI-StuModify002',
			'para': ['student_yuer', 'password12345', 'password12345', '用户密码修改成功，点击确定，重新登录']
		}
	]
	
	def teststeps(self):
		
		# 初始密码：888888
		self.START_PASSWORD = '888888'
		
		# 取出参数(变量解包)
		username, password, confirm_password, tips_info = self.para
		
		# 测试步骤如下
		STEP(1, '登录学生系统')
		student_operation.student_login(username)
		STEP(2, '修改学生密码')
		student_operation.modify_student_password(self.START_PASSWORD, password, confirm_password)
		STEP(3, '获取提示信息')
		get_tips_info = student_operation.get_tips_info()
		CHECK_POINT('检查错误提示信息', get_tips_info == tips_info)
		STEP(4, '重新登录学生系统')
		student_operation.student_login(username, password)
		STEP(5, '修改学生密码')
		student_operation.modify_student_password(password, self.START_PASSWORD, self.START_PASSWORD)
		
	