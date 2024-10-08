from interfaces import ITask


class Task(ITask):
    def get_detail(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}, Status: {status}"


class CompositeTask(ITask):
    def __init__(self, name: str):
        self.name = name
        self.completed = False
        self.subtasks = []

    def add_subtask(self, task: ITask):
        self.subtasks.append(task)

    def mark_complete(self):
        self.completed = True
        for task in self.subtasks:
            task.mark_complete()

    def get_detail(self):
        status = "Completed" if self.completed else "Pending"
        detail = f"Composite Task: {self.name}, Status: {status}\n\tSubtasks:\n"
        for task in self.subtasks:
            subtask_detail = task.get_detail()#.replace("\n", "\n\t") 
            detail += f"\t- {subtask_detail}\n"
        return detail
         
         
    
