from abc import ABC, abstractmethod
from datetime import datetime
'''
We have 3 types of tasks:
    0. AbstractTask (Parents: object)
        body = [text]
        state = [bool]
        created_time = [data_time]
        priority = [str]
        
    1. task (Parents: AbstractTask)
        body = [text]
        state = [bool]
        created_time = [data_time]
        priority = [str]

    2. timed_task (Parents: task)
        body = [text]
        state = [bool]
        created_time = [data_time]
        priority = [str]
        deadline = [data_time]

    3. complex_task (Parents: AbstractTask)
        task1 = [task]
        task2 = [timed_task]
        ...
'''

class TaskBase(ABC):
    def __init__(self, 
                 body: str, 
                 status: str='uncompleted', 
                 created_time: datetime=datetime.now(), 
                 prioity: str='medium') -> None:
        # constans must be keeped in another file

        # to add validation
        self._body = body
        self._status = status
        self._created_time = created_time
        self._priority = prioity 

    @property
    def body(self):
        return self._body
    
    @property
    def status(self):
        return self._status
    
    @property
    def created_time(self):
        return self._created_time
    
    @property
    def prioity(self):
        return self._priority
    
    @abstractmethod
    def ChangeTaskStatus(self): ...

    @abstractmethod
    def ShowInfo(self): ...


class Task(TaskBase):
    def __init__(self, 
                 body: str, 
                 status: str = 'uncompleted', 
                 created_time: datetime = datetime.now(), 
                 prioity: str = 'medium',
                 ) -> None:
        super().__init__(body, status, created_time, prioity)

    def ShowInfo(self):
        print(
            "Task:",
            f"Body: {self._body}"
            f"Status: {self._status}"
        )

    def ChangeTaskStatus(self) -> None:
        # Validation like "self.is_exist()" can be added
        if self._status == "completed": self._status = "uncompleted"
        else: 
            self._status = "completed"


class TimedTask(Task):
    def __init__(self, 
                 body: str, 
                 deadline: datetime,
                 status: str = 'uncompleted', 
                 created_time: datetime = datetime.now(), 
                 prioity: str = 'medium',
                 ) -> None:
        super().__init__(body, status, created_time, prioity)
        self._deadline = deadline

    @property
    def deadline(self):
        return self._deadline
    
    def ShowInfo(self):
        print(
            "Task:",
            f"Body: {self.body}",
            f"Status: {self.status}",
            f"Deadline: {self._deadline}",
            sep='\n'
        )

class ComplexTask:
    # first verison:
    # def __init__(self, *args) -> None:
    #     for ind, task in enumerate(args):
    #         setattr(self, f"task{ind + 1}", task)

    # def PrintRelatedTasks(self) -> None:
    #     for task_name in self.__dict__:
    #         print(f"{task_name}: {self.__dict__[task_name]}")
        
    #second verison
    def __init__(self, *args) -> None:
        self.__tasks: list = list(args)
    
    @property
    def tasks(self):
        return self.__tasks
    
    @tasks.setter
    def tasks(self, *args):
        for task in args:
            if isinstance(task, TaskBase):
                self.__tasks.append(task)
            else:
                raise TypeError("Incorrect Type: you gave not Task object")

    def PrintRelatedTasks(self) -> None:
        for task in self.__tasks:
            print(task)

        

t1 = TimedTask("body", datetime.now())
t2 = Task("dsdffd")

t3 = ComplexTask(t1, t2)

print(t3.tasks)

