# FastAPI MongoDB REST API

This project is a REST API built with FastAPI and MongoDB.

## Features

- FastAPI for building the API
- MongoDB for the database
- CRUD operations for managing data
- Pydantic for data validation
- Role-based access control

## Requirements

- Python 3.9+
- MongoDB

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-mongodb-restapi.git
    cd fastapi-mongodb-restapi
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the MongoDB server.

## Running the Application

1. Start the FastAPI server:
    ```bash
    python app/main.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI.
