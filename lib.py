from dataclasses import dataclass
import json
from datetime import datetime
statuses=["новая", "выполняется", "ревью", "выполнено", "отменено"]

@dataclass
class Task:
    name: str
    description: str
    status: str
    date_status: str #дата последнего изменения статуса
    date: str

class manager():
    def __init__(self):
        self._tasks = []

    def add(self, task: Task):
        self._tasks.append(task)

    def save(self, fname):
        array = [task.__dict__ for task in self._tasks]
        with open(fname, 'w') as file:
            json.dump(array, file)

    def load(self, fname):
        with open(fname, 'r') as file:
            array = json.load(file)
        self._tasks = [Task(**task_data) for task_data in array]

    def view_task(self, name, fname):
        flag = 0
        for task in self._tasks:
            if task.name == name:
                flag += 1
                description = task.description
                status = task.status
                date_create = task.date.split(';')[-1]
                date_status = task.date_status
                print(f"\nЗадача «{name}»\nОписание: {description}\nСтатус: {status}\nДата последнего изменения статуса: {date_status}\nДата создания: {date_create}")
                task.date = str(datetime.now())[:-7] + ';' + task.date
                self.save(fname)
        if flag == 0:
            print(f"Задача {name} не найдена")
            
    def edit(self, name, new_status, date, fname):
        flag = 0
        for task in self._tasks:
            if task.name == name:
                flag += 1
                
                if new_status == "1" and task.status != "новая":
                    new_status = statuses[statuses.index( task.status.split(';')[0] )-1]
                    task.status = new_status
                    task.date_status = str(datetime.now())[:-7]
                    self.save(fname)
                    print(f"Статус для «{task.name}» изменен")
                    
                elif new_status == "1" and task.status == "новая":
                    print("Статус «новая» нельзя изменить на предыдущий")
                    
                elif new_status == "2" and task.status != "отменено":
                    new_status = statuses[statuses.index( task.status.split(';')[0] )+1]
                    task.status = new_status
                    task.date_status = str(datetime.now())[:-7]
                    self.save(fname)
                    print(f"Статус для «{task.name}» изменен")
                    
                elif new_status == "2" and task.status == "отменено":
                    print("Статус «отменено» нельзя изменить на следующий")
                    
                elif new_status == "3":
                    new_status = statuses[4]
                    task.status = new_status
                    task.date_status = str(datetime.now())[:-7]
                    self.save(fname)
                    print(f"Статус для «{task.name}» изменен")
                    
                else:
                    print("Неизвестное действие")
                    
                break
        if flag == 0:
            print(f"Задача {name} не найдена")

    def view_history(self, name):
        flag = 0
        for task in self._tasks:
            if task.name == name:
                flag += 1
                print(f"\nИстория задачи «{task.name}»\n")
                dates = task.date.split(';')
                print("  Дата  просмотра")
                if len(dates) == 1:
                    print("   История пуста")
                    break
                for i in range(0, len(dates)-1):
                    print("{}".format(dates[i]))
        if flag == 0:
            print(f"Задача {name} не найдена")
