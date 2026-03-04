# routers/tasks.py
from fastapi import APIRouter, HTTPException
from models import Task  # Импортируем нашу модель

# Создаем роутер. 
# Обратите внимание на prefix и tags — это супер-удобно!
router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)

fake_database =[]

# Теперь вместо @app.get("/tasks") мы пишем @router.get("")
# Путь "/tasks" подставится автоматически из prefix!
@router.get("")
def get_tasks():
    return fake_database

@router.post("")
def create_task(task: Task):
    new_task = task.model_dump() # или task.dict() для старых версий
    new_task["id"] = len(fake_database) + 1
    fake_database.append(new_task)
    return new_task

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for idx, t in enumerate(fake_database):
        if t["id"] == task_id:
            del fake_database[idx]
            return {"message": "Задача успешно удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")