"""
    测试员工模块的增删改查实现
"""
# 1.导包
import logging
import unittest
import requests

import app
from api.EmpAPI import EmpCRUD


# 2.创建测试类


class Test_Emp(unittest.TestCase):

    # 3.初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 4.资源卸载函数
    def tearDown(self):
        self.session.close()

    # 5.测试函数1: 增
    #  直接执行该测试函数失败，为什么?
    #  原因：1.先执行登录操作  2.还需要提交银行卡(token)
    #  解决: 1.使用测试套件组织接口的执行顺序
    #        2.如何提交银行卡, 如何实现关联?
    #          核心步骤1: token 的提取
    #          核心步骤2: token 的提交
    def test_add(self):
        logging.info('新增员工日志信息')#设置日志级别
        # 1.请求业务
        response = self.emp_obj.add(self.session, username="hukus4933895960",
                                    mobile="18912345678")
        # 2.断言业务
        print("员工新增响应结果:", response.json())
        # 员工新增响应结果: {'code': 10000, 'data': {'id': '1193826140145668096'}, 'message': '操作成功！', 'success': True}
        # 提取 ID
        id = response.json().get("data").get("id")
        app.USER_ID = id
        print("新增员工的ID:", id)
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 6.测试函数2: 改
    def test_update(self):
        logging.debug('修改员工日志信息')  # 设置日志级别
        # 1.请求业务
        response = self.emp_obj.update(self.session, app.USER_ID, "aotuman11111739")
        # 2.断言业务
        print("修改后的员工信息:", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 7.测试函数3: 查
    def test_get(self):
        logging.debug('查询员工日志信息')  # 设置日志级别
        # 1.请求业务
        response = self.emp_obj.get(self.session, app.USER_ID)
        # 2.断言业务
        print("查询后的员工信息:", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 8.测试函数4: 删
    def test_delete(self):
        logging.warning('修改员工日志信息')  # 设置日志级别
        # 1.请求业务
        response = self.emp_obj.delete(self.session, app.USER_ID)
        # 2.断言业务
        print("删除后的员工信息:", response.json())

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
