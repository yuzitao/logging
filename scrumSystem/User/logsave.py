import logging
import pymysql

config = {
    'host': '39.96.61.39',
    'port': 3306,
    'user': 'root',
    'password': '123456789',
    'db': 'scrum',
    'charset': 'utf8'
}


def configmysql(data):
    data_list = data.split('\n')
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = "insert into log (record) values ('%s')" % data_list[len(data_list) - 2]
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def wrapper(func):
    def inner(*args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        res = func(*args, **kwargs)
        handler = logging.FileHandler('log.txt')
        formatter = logging.Formatter('%(levelname)s - %(message)s - %(asctime)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        if func.__name__ == 'index':
            logger.info('管理员删除了用户')
            print(1)
        elif func.__name__ == 'user':
            logger.info('管理员添加了用户')
            print(2)
        with open('log.txt', 'r+') as fp:
            data = fp.read()
            configmysql(data)
        return res

    return inner
