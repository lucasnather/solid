from abc import abstractclassmethod, ABC
from typing import Dict
from datetime import datetime

class TasksInterface(ABC):

    @abstractclassmethod
    def create_task(task: any) -> Dict:
        pass

    @abstractclassmethod
    def update_task(task: any, id: str) -> Dict:
        pass

    @abstractclassmethod
    def remove_task(id: str) -> None:
        pass

class Tasks(TasksInterface):
    def create_task(task: any):
        print("Create Tasks")
        return {
            "name": "Study Python",
            "date": datetime.now()
        }

    def update_task(task: any, id: str):
        print("Update Tasks")
        return {
            "name": "Study NextJs",
            "date": datetime.now()
        }

    def remove_task(id: str):
        print("Remove Tasks")