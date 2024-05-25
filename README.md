# Yuhu API Challenge

## Table of Contents
- [Installation](#installation)
- [Documentation](#documentation)

## Installation
Requirements:
- Docker
- Docker compose
- Make

Instructions
  - Create a network with `docker network create yuhu`
  - Run the project with `make up`

## Documentation

This API allows you to manage tasks.

## Base URL
`http://54.198.216.230:8000/api/`

## Authentication
This API uses API keys for authentication. Include your API key in the `Authorization` header:


## Endpoints

### Get all task

**Endpoint: GET /tasks/**

**Description:**
Retrieve a list of all tasks.

**Request:**
- Headers:
  - `Authorization: Bearer YOUR_API_KEY`
- Query Parameters:
  - `page` (integer, optional): The page number to retrieve. Default is `1`.

**Response:**
- Status: `200 OK`
- Body:
```json
{
  "count": 5,
  "next": "http://localhost:8000/api/tasks/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Database Design",
      "description": "Create the database schema and define the necessary tables.",
      "email": "db.designer@example.com",
      "expiration_date": "2024-06-01"
    },
    {
      "id": 3,
      "title": "User Interface Development",
      "description": "Create the user interface using React and ensure responsiveness.",
      "email": "ui.designer@example.com",
      "expiration_date": "2024-06-15"
    }
  ],
  "total_pages": 3,
  "page_size": 2
}
```

___
### Get a single task

**Endpoint: GET /tasks/{id}/**

**Description:**
Retrieve details of a specific product by its ID.

**Request:**
- Headers:
  - `Authorization: Bearer YOUR_API_KEY`
- Parameters:
  - id (integer, required): The ID of the task.

**Response:**
- Status: `200 OK`
- Body:
```json

{
  "id": 1,
  "title": "Database Design",
  "description": "Create the database schema and define the necessary tables.",
  "email": "db.designer@example.com",
  "expiration_date": "2024-06-01"
}
```

___
### Create a new task

**Endpoint: POST /tasks/**

**Description:**
Create a new task.

**Request:**
- Headers:
  - `Authorization: Bearer YOUR_API_KEY`
  - `Content-Type: application/json`

- Body:
```json
{
  "title": "Database Design",
  "description": "Create the database schema and define the necessary tables.",
  "email": "db.designer@example.com",
  "expiration_date": "2024-06-01"
}
```

**Response:**
- Status: `201 Created`
- Body:
```json

{
  "id": 4,
  "title": "Integration Testing",
  "description": "Perform integration tests to ensure interoperability.",
  "email": "tester@example.com",
  "expiration_date": "2024-06-20"
}
```

___
### Update a task

**Endpoint: PUT /tasks/{id}/**

**Description:**
Update the details of an existing task.

**Request:**
- Headers:
  - `Authorization: Bearer YOUR_API_KEY`
  - `Content-Type: application/json`

- Parameters:
  - id (integer, required): The ID of the task.
- Body:
```json

{
  "title": "API Implementation",
  "description": "Develop the RESTful APIs for the application and document them.",
  "email": "api.dev@example.com",
  "expiration_date": "2024-06-10"
}
```

**Response:**
- Status: `200 OK`
- Body:
```json

{
  "id": 2,
  "title": "API Implementation",
  "description": "Develop the RESTful APIs for the application and document them.",
  "email": "api.dev@example.com",
  "expiration_date": "2024-06-10"
}
```

___
### Delete a task

**Endpoint: DELETE /tasks/{id}/**

**Description:**
Delete a task.

**Request:**
- Headers:
  - `Authorization: Bearer YOUR_API_KEY`

- Parameters:
  - id (integer, required): The ID of the task.

**Response:**
- Status: `204 No Content`

___
### Error Handling
**Common error responses**

400 Bad Request
```json
{
  "title": [
    "This field is required."
  ],
  "description": [
    "This field is required."
  ],
  "email": [
    "This field is required."
  ],
  "expiration_date": [
    "This field is required."
  ]
}
```

401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

404 Not Found
```json
{
  "detail": "No Task matches the given query."
}
```
