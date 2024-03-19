"""编写公共类，封装公共方法，比如读取用例文件内容、数据库操作等"""
import csv
import os.path

import pymysql
import yaml


class Utils:
    config_data = None
    yaml_data_cache = {}

    @classmethod
    def read_config(cls, section, file_path='E:\PycharmProjects\lkxtest1\WebAuto_Testing\Common\config.yml'):
        if cls.config_data is None:
            with open(file_path, 'r', encoding='utf-8') as file:
                cls.config_data = yaml.safe_load(file)
        return cls.config_data.get(section, {})

    @classmethod
    def read_yaml(cls, file_path):
        # 使用缓存避免重复读取
        if file_path not in cls.yaml_data_cache:
            with open(file_path, 'r', encoding='utf-8') as file:
                cls.yaml_data_cache[file_path] = yaml.safe_load(file)
        return cls.yaml_data_cache[file_path]

    base_path = os.path.dirname(os.path.abspath(__file__))
    page_path = os.path.join(base_path, "Pages")
    test_path = os.path.join(base_path, "TestPages")
    base_url = "http://192.168.102.123/zentaopms/www/index.php?m=user&f=login"

    @classmethod
    def get_cursor(cls):
        database_config = cls.read_config('database')
        db = pymysql.connect(host=database_config['host'],
                             user=database_config['user'],
                             password=database_config['password'],
                             db=database_config['dbname'],
                             port=3306)
        return db.cursor()

    @classmethod
    def read_csv(cls, file):
        """读取CSV文件内容"""
        with open(file=file) as f:
            return list(csv.reader(f))  # 读取文件中的所有行，每行作为一个列表，最终形成一个包含这些行的列表。

    @classmethod
    def execute_dql(cls, sql):
        """执行select语句，返回查询内容"""
        cls.cur.execute(sql)
        return cls.cur.fetchall()

    @classmethod
    def excute_dml(cls, sql):
        """执行dml语句并提交事务"""
        cls.cur.execute(sql)
        cls.db.commit()

    def __del__(self):
        self.cur.close()
        self.db.close()
