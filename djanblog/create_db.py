from contextlib import closing
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# шаблон для создания базы данных

# используем контекст-менеджер, чтобы не беспокоиться о закрытии соединения и курсора
def create_db(usr='postgres', password='4250'):
    try:
        print('Подключение к PostgreSQL:')
        with closing(psycopg2.connect(user = usr, 
                                      password = password)) as connect:
            connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with connect.cursor() as cur:
                # создание новой базы данных
                create_db = f'create database djanblog_db'  # пример создания базы данных
                cur.execute(create_db)
                print(f'Создана база данных: djanblog_db')
            print('Отключение от PostgreSQL:')

    except (Exception, Error) as error:
        print('Ошибка при работе с PostgreSQL:', error)

create_db('djanblog_db')