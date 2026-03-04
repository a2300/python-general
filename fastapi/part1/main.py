from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Наша Pydantic-модель
class Task(BaseModel):
    title: str
    description: str | None = None # Необязательное поле, по умолчанию None
    is_completed: bool = False     # По умолчанию задача не выполнена

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id, "task_name": f"Task {task_id}"}


@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return {
        "message": "Return list of tasks",
        "skip": skip,
        "limit": limit
    }

@app.post("/tasks")
def create_task(task: Task):
    # Здесь task — это уже готовый объект Pydantic, а не просто сырой словарь!
    # Мы можем обращаться к полям через точку: task.title, task.description
    
    # Имитируем сохранение в базу данных и возвращаем ответ
    return {
        "message": "Задача успешно создана",
        "task": task
    }
