# -*- coding: utf-8 -*-

import os
import psutil
from datetime import datetime
from random import randint
import logging


logging.basicConfig(handlers=[logging.FileHandler(filename="logger.txt", encoding='utf-8', mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%F %A %T",level=logging.INFO)
logger = logging.getLogger(__name__)


class Test_case:
    """
    Родительский класс общий для всех Тест-кейсов
    """

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        """
        Функция подготовки к тестированию
        :return:
        """
        return

    def run(self):
        """
       Функция выполнения теста
       :return:
       """
        return

    def clean_up(self):
        """
       функция очистки данных после тестирования
       :return:
       """
        return

    def execute(self):
        """
       Главная функция запуска тестов
       :return:
       """
        if self.prep:
            self.run()
            self.clean_up()


class Test_1(Test_case):
    """
    класс наследующий родительский класс, описывающий Тест-кейс 1
    """
    def __init__(self, tc_id, name):
        super().__init__(tc_id, name)

    def prep(self):
        """
        функиця подготовки к тесту, выполняющая проверку системного времени на четность, является триггером
        для выполения теста в случае выполнения условия
        :return: True False
        """
        if datetime.now().timestamp().__round__() % 2 != 0:
            logger.info(f'Тест {self.tc_id} - {self.name}: Текущее системное время в секундах не кратно двум.')
            # print(f'Тест {self.tc_id} - {self.name}: Текущее системное время в секундах не кратно двум.')
            return False
        else:
            logger.info(f'Тест {self.tc_id} - {self.name}: Текущее системное время в секундах кратно двум. Тест пройден')
            # print(f'Тест {self.tc_id} - {self.name}: Текущее системное время в секундах кратно двум. Тест пройден')
            return True

    def run(self):
        """
        функиция тестирования, вывод списка файлов из домашней директории текущего пользователя
        :return: True Fals
        """
        path_home = os.listdir(os.path.expanduser("~"))
        logging.info(f"Тест {self.tc_id} - {self.name} выдвод списка домашней директории пользователя: \n {path_home}")
        # print(f"Тест {self.tc_id} - {self.name} выдвод списка домашней директории пользователя: ", '\n',
        #       os.listdir(os.path.expanduser("~")))
        return True

    def clean_up(self):
        """
        функция очистки данных после тестирования
        :return:
        """
        return

    def execute(self):
        """
        Главная функция запуска тестов
        :return:
        """
        prep_res = self.prep()
        if prep_res:
            self.run()
            self.clean_up()
            logging.info(f"Тест {self.tc_id} - {self.name} завершён")
            # print(f"Тест {self.tc_id} - {self.name} завершён")
        else:
            logging.info(f'Тест {self.tc_id} - {self.name} был прерван')
            # print(f'Тест {self.tc_id} - {self.name} был прерван')


class Test_2(Test_case):
    """
    класс наследующий родительский класс, описывающий Тест-кейс 2
    """
    def __init__(self, tc_id, name):
        super().__init__(tc_id, name)

    def prep(self):
        """
        функиця подготовки к тесту, проверка объема оперативной памяти компьютера, является триггером для выполения
        теста в случае выполнения условия
        :return: True False
        """
        total_ram = round(psutil.virtual_memory().total / (1024.0 ** 3))
        if total_ram < 1:
            logging.info(f"Тест {self.tc_id} - {self.name}: Оперативной памяти меньше 1 Гб.")
            # print(f'Тест {self.tc_id} - {self.name}: Оперативной памяти меньше 1 Гб.')
            return False
        else:
            logging.info(f"Тест {self.tc_id} - {self.name}: Оперативной памяти больше 1 Гб. Тест пройден")
            return True

    def run(self):
        """
        функиция тестирования, создание файла со случайным содержимым
        :return: True False
        """
        with open('test', 'w') as f:
            f.truncate(1024 * 1024)
            for i in range(1000):
                f.write(str(randint(1, 100)) + " ")
        logging.info(f"Тест {self.tc_id} - {self.name}: Файл 'test' создан")
        # print(f"Тест {self.tc_id} - {self.name}: Файл создан")
        return True

    def clean_up(self):
        """
        функция очистки данных после тестирования, удаляет созданный в тесте файл
        :return: True False
        """
        os.remove('test')
        logging.info(f"Тест {self.tc_id} - {self.name}: Файл 'test' удален")
        # print(f"Тест {self.tc_id} - {self.name}: Файл 'test' удален")
        return True

    def execute(self):
        """
        Главная функция запуска тестов
        :return:
        """
        prep_res = self.prep()
        if prep_res:
            self.run()
            self.clean_up()
            logging.info(f"Тест {self.tc_id} - {self.name} завершён")
            # print(f"Тест {self.tc_id} - {self.name} завершён")
        else:
            logging.info(f'Тест {self.tc_id} - {self.name} был прерван')
            # print(f'Тест {self.tc_id} - {self.name} был прерван')


if __name__ == '__main__':

    test1 = Test_1('t1', 'test1')
    test1.execute()

    test2 = Test_2('t2', 'test2')
    test2.execute()

