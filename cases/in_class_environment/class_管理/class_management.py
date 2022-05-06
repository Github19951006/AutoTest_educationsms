"""
@Project ：AutoTest_education 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/22
@File   :class_management.py
"""
from hytest import *
from cfg.cfg import *
from lib.api.yjyx_class_api import *

force_tags = ['班级管理']

class Case_tc000002:
	name = '添加班级2 - tc000002'
	
	# 清除方法
	def teardown(self):
		gs_class.del_class(self.addClassId)
	
	def teststeps(self):
		# 测试步骤如下
		STEP(1,'创建一个班级')
		res_add_class = gs_class.add_class(SENIOR_THREE_GRADE_ID,'龙山理7班',89)
		ret_jsonObj = res_add_class.json()
		CHECK_POINT('添加结果回码',ret_jsonObj['retcode'] == 0)
		
		#** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addClassId = ret_jsonObj['id']
		
		STEP(2, '列出班级')
		res_list_class = gs_class.list_class(6)
		resList_jsonObj = res_list_class.json()
		INFO(resList_jsonObj['retlist'])
		
		# 预期结果
		expected = {
					"name": "龙山理7班",
					"grade__name": "高三",
					"invitecode": ret_jsonObj['invitecode'],
					"studentlimit": 89,
					"studentnumber": 0,
					"id": ret_jsonObj['id'],
					"teacherlist": []
				}
	
		CHECK_POINT('列出结果检查',str(expected) in str(resList_jsonObj['retlist']))


class Case_tc000003:
	name = '添加班级3（存在同年级的同名班级） - tc000003'
	
	def teststeps(self):
		# 测试步骤如下
		STEP(1, '创建一个班级')
		res_add_class = gs_class.add_class(SENIOR_THREE_GRADE_ID,
		                                   '2015龙山理22班', 44)
		ret_jsonObj = res_add_class.json()
		INFO(ret_jsonObj)
		expected = {
					"retcode": 1,
					"reason": "duplicated class name"
					}
		
		CHECK_POINT('添加结果回码', ret_jsonObj == expected)
		
		STEP(2, '列出班级')
		res_list_class = gs_class.list_class(SENIOR_THREE_GRADE_ID)
		resList_jsonObj = res_list_class.json()
		INFO(resList_jsonObj)
		
		# 调用全局共享 数据
		invitecode = GSTORE['invitecode']
		cid = GSTORE['id']
		
		# 预期结果
		expected = {
			"gradeid": 6,
			"retlist": [
				{
					"name": "2015龙山理22班",
					"grade__name": "高三",
					"invitecode": invitecode,
					"studentlimit": 69,
					"studentnumber": 0,
					"id": cid,
					"teacherlist": []
				}
			],
			"retcode": 0
		}
		CHECK_POINT('列出结果检查', resList_jsonObj == expected)


class Case_tc000051:
	name = '修改班级1 - tc000051'
	
	def teardown(self):
		cid = GSTORE['id']
		gs_class.modify_class(cid, '2015龙山理22班', 69)
	
	def teststeps(self):
		
		# 调用全局共享 数据
		invitecode = GSTORE['invitecode']
		cid = GSTORE['id']
		
		# 测试步骤如下
		STEP(1, '修改班级名字')
		res_modif_class = gs_class.modify_class(cid,'修改2015龙山理22班',69)
		retcode = res_modif_class.json()['retcode']
		CHECK_POINT('添加结果回码', retcode == 0)
		#

		STEP(2, '列出班级')
		res_list_class = gs_class.list_class(SENIOR_THREE_GRADE_ID)
		resList_jsonObj = res_list_class.json()
		INFO(resList_jsonObj)
		
		# 预期结果
		expected = {
			"gradeid": 6,
			"retlist": [
				{
					"name": "修改2015龙山理22班",
					"grade__name": "高三",
					"invitecode": invitecode,
					"studentlimit": 69,
					"studentnumber": 0,
					"id": cid,
					"teacherlist": []
				}
			],
			"retcode": 0
		}
		CHECK_POINT('列出结果检查', resList_jsonObj == expected)


class Case_tc000052:
	name = '修改班级2（已有的班级同名） - tc000052'
	
	# 清除方法
	def teardown(self):
		gs_class.del_class(self.addClassId)
	
	def teststeps(self):
		# 调用全局共享 数据
		invitecode = GSTORE['invitecode']
		cid = GSTORE['id']
		
		# 测试步骤如下
		STEP(1, '创建一个班级')
		res_add_class = gs_class.add_class(SENIOR_THREE_GRADE_ID,
		                                   '莞工计科1班', 99)
		retAdd = res_add_class.json()
		CHECK_POINT('添加结果回码', retAdd['retcode'] == 0)
		
		# ** 保存id，存到self中，self是实例对象都能访问到的东西
		self.addClassId = retAdd['id']
		
		STEP(2, '修改班级名字')
		res_modif_class = gs_class.modify_class(self.addClassId,
		                                        '2015龙山理22班', 99)
		retObj = res_modif_class.json()
		retcode = retObj['retcode']
		INFO(retObj)
		CHECK_POINT('添加结果回码', retcode == 1)
		
		
		STEP(3, '列出班级')
		res_list_class = gs_class.list_class(SENIOR_THREE_GRADE_ID)
		resList = res_list_class.json()
		INFO(resList)
		
		# 预期结果
		expected = {
		    "gradeid": 6,
		    "retlist": [
		        {
		            "name": "2015龙山理22班",
		            "grade__name": "高三",
		            "invitecode": invitecode,
		            "studentlimit": 69,
		            "studentnumber": 0,
		            "id": cid,
		            "teacherlist": []
		        },
		        {
		            "name": "莞工计科1班",
		            "grade__name": "高三",
		            "invitecode": retAdd['invitecode'],
		            "studentlimit": 99,
		            "studentnumber": 0,
		            "id": retAdd['id'],
		            "teacherlist": []
		        }
		    ],
		    "retcode": 0
			}
		
		CHECK_POINT('列出结果检查', resList == expected)


class Case_tc000053:
	name = '修改班级3（ID为一个不存在的班级ID号） - tc000053'
	
	def teststeps(self):
		# 调用全局共享 数据
		invitecode = GSTORE['invitecode']
		cid = GSTORE['id']
		
		# 测试步骤如下
		STEP(1, '修改不存在的班级ID号')
		res_modif_class = gs_class.modify_class(3413, '2015龙山理22班', 69)
		retObj = res_modif_class.json()
		retcode = retObj['retcode']
		INFO(retObj)
		CHECK_POINT('添加结果回码', retcode == 404)
		
		STEP(3, '列出班级')
		res_list_class = gs_class.list_class(SENIOR_THREE_GRADE_ID)
		resList = res_list_class.json()
		INFO(resList)
		
		# 预期结果
		expected = {
			"gradeid": 6,
			"retlist": [
				{
					"name": "2015龙山理22班",
					"grade__name": "高三",
					"invitecode": invitecode,
					"studentlimit": 69,
					"studentnumber": 0,
					"id": cid,
					"teacherlist": []
				}
			],
			"retcode": 0
		}
		CHECK_POINT('列出结果检查', resList == expected)


class Case_tc000081:
	name = '删除班级1 - tc000081'
	
	def teststeps(self):
		# 调用全局共享 数据
		invitecode = GSTORE['invitecode']
		cid = GSTORE['id']
		
		# 测试步骤如下
		STEP(1, '删除不存在的班级ID号')
		res_del_class = gs_class.del_class(3413)
		retObj = res_del_class.json()
		retcode = retObj['retcode']
		INFO(retObj)
		CHECK_POINT('添加结果回码', retcode == 404)
		
		STEP(3, '列出班级')
		res_list_class = gs_class.list_class(SENIOR_THREE_GRADE_ID)
		resList = res_list_class.json()
		INFO(resList)
		
		# 预期结果
		expected = {
			"gradeid": 6,
			"retlist": [
				{
					"name": "2015龙山理22班",
					"grade__name": "高三",
					"invitecode": invitecode,
					"studentlimit": 69,
					"studentnumber": 0,
					"id": cid,
					"teacherlist": []
				}
			],
			"retcode": 0
		}
		CHECK_POINT('列出结果检查', resList == expected)

class Case_tc000082:
	name = '删除班级2 - tc000082'
	
	def teststeps(self):
		# 调用全局共享 数据
		invitecode = GSTORE['invitecode']
		cid = GSTORE['id']

		# 测试步骤如下
		STEP(1, '创建一个班级')
		res_add_class = gs_class.add_class(SENIOR_THREE_GRADE_ID,
		                                   '莞工计科1班', 99)
		retAdd = res_add_class.json()
		CHECK_POINT('添加结果回码', retAdd['retcode'] == 0)
		
		STEP(2, '删除存在的班级ID号')
		res_del_class = gs_class.del_class(retAdd['id'])
		retObj = res_del_class.json()
		retcode = retObj['retcode']
		INFO(retObj)
		CHECK_POINT('添加结果回码', retcode == 0)
		
		STEP(3, '列出班级')
		res_list_class = gs_class.list_class(SENIOR_THREE_GRADE_ID)
		resList = res_list_class.json()
		INFO(resList)
		
		# 预期结果
		expected = {
			"gradeid": 6,
			"retlist": [
				{
					"name": "2015龙山理22班",
					"grade__name": "高三",
					"invitecode": invitecode,
					"studentlimit": 69,
					"studentnumber": 0,
					"id": cid,
					"teacherlist": []
				}
			],
			"retcode": 0
		}
		CHECK_POINT('列出结果检查', resList == expected)

		
		