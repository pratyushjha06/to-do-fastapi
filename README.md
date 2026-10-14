# FastAPI TODO Application

A simple TODO REST API built using FastAPI and Pydantic. It supports creating, retrieving, updating, and deleting tasks.

1. Project Setup

Navigate to your project directory:

```
cd your-project-folder
```

2. Create a Virtual Environment

```
python -m venv venv
```

**Activate the Virtual Environment**

Windows (Command Prompt):

```
venv\Scripts\activate
```

Windows (PowerShell):

```
.\venv\Scripts\Activate.ps1
```

Linux / macOS:

```
source venv/bin/activate
```

3. Install Requirements

Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

Then run:

```
pip install -r requirements.txt
```

4. Run the Uvicorn Server

If your Python file is named main.py, start the server using:

```
uvicorn main:app --reload
```

The server will start at:

http://127.0.0.1:8000

5. API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

6. Available API Endpoints

**Method  Endpoint    Description**

GET /to-do  Retrieve all tasks

POST    /to-do  Create a new task

GET /to-do/{task_id}    Retrieve a task by ID

PUT /to-do/{task_id}    Update a task by ID

DELETE  /to-do/{task_id}    Delete a task by ID

7. Example Request Body

Use this JSON body when creating or updating a task:

{

  "id": 1,

  "title": "Learn FastAPI",

  "date": "2026-10-15",

  "status": false

}

8. Stop the Server

Press CTRL + C in the terminal to stop the server.

Note

Tasks are stored in an in-memory Python list.

All tasks will be lost when the server restarts.

No database is configured in this project.

##### **Project Structure**

your-project/

├── main.py

├── requirements.txt

├── README.md

└── venv/