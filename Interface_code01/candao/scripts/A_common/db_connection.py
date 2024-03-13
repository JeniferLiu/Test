import pymysql

from Interface_code01.candao.scripts.A_common.B_utils import load_config


class DataBaseConnection:
    def __init__(self, config_path):
        config = load_config(config_path)['database']
        self.connection = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            db=config['dbname'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, sql):  # DQL操作
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()  # 返回所有查询结果
        except Exception as e:
            print(f"数据库查询出错：{e}")
            return None

    def execute_dml(self, sql):  # DML操作
        try:
            self.cursor.execute(sql)
            self.connection.commit()  # 提交更改
        except Exception as e:
            print(f"数据库DML操作出错：{e}")
            raise e

    def close(self):
        self.cursor.close()
        self.connection.close()
