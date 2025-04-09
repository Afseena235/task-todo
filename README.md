# 📝 To-Do List API

This is a simple RESTful API for managing to-do items built using **Django** and **Django REST Framework**. It allows users to create, read, update, and delete tasks.

---

## 🚀 Features

- List all to-do items
- View a single to-do item
- Create a new to-do
- Update an existing to-do
- Delete a to-do

---

## 🛠 Technologies Used

- Python 3.10
- Django
- Django REST Framework

---

## 📁 Project Structure

todolist/
├── api/
│   └── v1/
│       └── todo_list/
│           ├── serializers.py     # Serializers for ToDo model
│           ├── urls.py            # API URLs
│           └── views.py           # API views 
│
├── media/                         # Media files (if needed)
├── static/                        # Static files
│
├── todo_list/
│   ├── _init_.py
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── todoList/
│   ├── _init_.py
│   ├── admin.py                   # ToDo model registration
│   ├── apps.py
│   ├── migrations/                # Database migrations
│   ├── models.py                  # ToDo model definition
│   ├── tests.py                   # Unit tests
│   └── views.py                   # Additional views (if any)
│
├── manage.py                      # Django CLI
├── README.md
└── requirements.txt               # Project dependencies


## 🔧 Setup Instructions

## 📖 Setup Instructions

Follow these steps to set up and run the Django To-Do List API on your local environment:

1. *Clone the Repository*:
   ```bash
   git clone https://github.com/Afseena235/task-todo.git
   
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv

3. **Activate the virtual environment**:
   ```bash
   \venv\Scripts\activate
   
4. **Install Project Dependencies**:
   ```bash
   pip install -r requirements.txt
   
5. *Set Up the Database*:
   ```bash
   python manage.py migrate
   
6. **Start the Development Server**:
   ```bash
   python manage.py runserver

## 📌 API Endpoints

| **Method** | **Endpoint**                  | **Description**              |
|------------|-------------------------------|-------------------------------|
| `GET`      | `/api/v1/todo/`               | Retrieve all to-do items      |
| `POST`     | `/api/v1/todo/`               | Create a new to-do item       |
| `GET`      | `/api/v1/todo/details/<id>/`  | Retrieve a specific item      |
| `PUT`      | `/api/v1/todo/details/<id>/`  | Update an existing item       |
| `DELETE`   | `/api/v1/todo/details/<id>/`  | Delete a specific item        |
### 📥 Example Requests & Responses

#### ✅ Create a To-Do (POST `/api/v1/todo/`)

**Request:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2025-04-08T07:29:24.294938Z"
}
```

**Response:**
````json
{
  "statuscode": 201,
  "title": "To-Do Created",
  "data": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2025-04-08T07:29:24.294938Z"
  },
  "errors": "",
  "message": "To-Do item created successfully."
}
````
📋 Get All To-Dos (GET /api/v1/todo/)

**Response:**
````json
{
  "statuscode": 200,
  "title": "Data received",
  "data": [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2025-04-08T07:29:24.294938Z"
    },
    {
      "id": 2,
      "title": "Read a book",
      "description": "Finish reading The Alchemist",
      "completed": true,
      "created_at": "2025-05-08T07:29:24.294938Z"
    }
  ],
  "errors": "",
  "message": "To-Do items received successfully."
}

````
✏️ Update To-Do (PUT /api/v1/todo/details/1/)

**Request:**
````json
{
  "title": "Buy groceries and fruits",
  "description": "Milk, eggs, bread, apples",
  "completed": false,
  "created_at": "2025-04-08T07:29:24.294938Z"
}

````
**Response:**
````json
{
  "statuscode": 200,
  "title": "Item Updated",
  "data": {
    "id": 1,
    "title": "Buy groceries and fruits",
    "description": "Milk, eggs, bread, apples",
    "completed": false,
    "created_at": "2025-04-08T07:29:24.294938Z"
  },
  "errors": "",
  "message": "To-Do item updated successfully."
}

````
🗑️ Delete To-Do (DELETE /api/v1/todo/details/1/)

**Response:**
````json
{
  "statuscode": 204,
  "title": "Deleted",
  "data": "",
  "errors": "",
  "message": "To-Do item deleted successfully."
}
````
