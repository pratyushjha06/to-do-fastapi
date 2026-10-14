from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

task = []


class TODO(BaseModel):
    id: int
    title: str
    date: str
    status: bool

@app.get("/to-do")
def get_todo():
    return task

@app.post("/to-do")
def create_todo(todo: TODO):
    task.append(todo)
    return {"message": "Task added successfully", "Data": todo}


@app.get("/to-do/{task_id}")
def get_todo_by_id(task_id:int):
    for t in task:
        if t.id == task_id:
            return t
    
    return{"Error":"Task ID not found"}


@app.put("/to-do/{task_id}")
def update_todo(task_id: int, updated_todo: TODO):
    for index, todo in enumerate(task):
        if todo.id == task_id:
            task[index] = updated_todo

            return {
                "message": "Data Updated",
                "data": updated_todo
            }

    return {"message": "Todo not found"}


@app.delete("/to-do/{task_id}")
def delete_todo(task_id: int):
    for index, t in enumerate(task):
        if t.id == task_id:
            task.pop(index)
            return{"Message": "Task Deleted"}
    return {"Message":"Task not found"}