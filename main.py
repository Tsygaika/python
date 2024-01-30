from lib import *
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='Чтение названия json файла')
parser.add_argument('fname', type=str)
args = parser.parse_args()
task_manager = manager()
task_manager.load(args.fname)

while True:
    choice = input("\n1)Создать новую задачу\n2)Изменить статус задачи\n3)Посмотреть историю задачи\n4)Посмотреть задачу\n5)Закрыть менеджер задач\nВведите номер действия:")
    print("")
    
    if choice == "1":
        print("Введите данные о новой задаче")
        name = input("Название:")
        description = input("Описание:")
        status = int(input("Выберите статус\n1)Новая\n2)Выполняется\n3)Ревью\n4)Выполнено\n5)Отменено\nВведите номер:"))
        while status not in [1,2,3,4,5]:
            print("Статуса с таким номером нет")
            status = int(input("Введите ещё раз:"))
        task_manager.add(Task(name, description, statuses[status-1], str(datetime.now())[:-7],str(datetime.now())[:-7]))
        task_manager.save(args.fname)
        print("Задача создана")
        
    elif choice == "2":
        name = input("Введите название задачи:")
        new_status = input("Как изменить статус?\n1)Вернуться в предыдущий статус\n2)Перейти к следующему статусу\n3)Перейти в статус отменено\nВведите номер:")
        task_manager.edit(name, new_status, str(datetime.now())[:-7], args.fname)

    elif choice == "3":
        name = input("Введите название задачи:")
        task_manager.view_history(name)

    elif choice == "4":
        name = input("Введите название задачи:")
        task_manager.view_task(name, args.fname)

    elif choice == "5":
        break

    else:
        print("Такого действия нет")
