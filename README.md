# Task Manager Project Documentation

## Introduction

Task Manager is a web application developed in Python using the Flask framework. It allows users to manage their tasks efficiently, including adding, editing, and deleting tasks. The application uses an SQLite database to store task information and incorporates form validation and user feedback features.



## Functionalities

### 1. Add Tasks
    - Users can add new tasks by providing a title, description, due date, priority and status.
    - The application validates the data entered by the user before adding the task to the database.
    - Feedback messages are displayed to inform the user if the task was added successfully or if there was an error.

### 2. Edit Tasks
    - Users can edit information for an existing task, including title, description, due date, priority, and status.
    - Changes made are updated in the database and reflected immediately in the user interface.
    - Feedback messages are displayed to inform the user if the task was edited successfully or if there was an error.

### 3. Delete Tasks
    - Users can delete existing tasks, completely removing them from the system.
    - A confirmation prompt is displayed to ensure the user wants to delete the task before proceeding.
    - Feedback messages are displayed to inform the user if the task was deleted successfully or if there was an error.

### 4. Task Reminder
    - The application displays a reminder at the top of the page if there are tasks due on the current day.
    - This helps users remember the tasks that need to be completed for the day.

## Project Structure

### 1. Models
  The application uses SQLAlchemy to define data models. The main model is "Task", which represents a single task and its properties.

### 2. Forms
  Flask-WTF is used to create and validate web forms. The main form is the "TaskForm", which is used to add and edit tasks.

### 3. Routes
  Flask defines routes to handle HTTP requests. The main route ("/") is responsible for rendering the application's main page and processing task addition requests.

### 4. Templates
  The index.html and update.html templates are used to dynamically render HTML pages, incorporating data from templates and forms.
  
### 5. Database
  The SQLite database is used to store task information. SQLAlchemy is responsible for interacting with the database, executing queries and updating records.

## Front End

### 1. HTML
  HTML is used to structure the content of web pages, including forms, task lists and feedback messages.

### 2. CSS
  CSS is used to style the appearance of web pages, defining colors, fonts, layouts and other visual aspects.

### 3. Bootstrap
  Bootstrap is used to create responsive layouts and consistent user interface elements across the application.

## Technologies Used

- **Python**: Main programming language used to develop the application.
- **Flask**: Python web framework used to create the application structure and define routes.
- **SQLAlchemy**: ORM library used to interact with the SQLite database.
- **HTML**: Markup language used to structure the content of web pages.
- **CSS**: Styling language used to style the appearance of web pages.
- **Bootstrap**: Front-end framework used to facilitate responsive design and the creation of attractive user interfaces.
- **SQLite**: Relational database management system used to store task information.
- **Flask-WTF**: Flask extension used to create and validate web forms.
- **Jinja2**: Template engine used by Flask to render HTML templates with dynamic data.

## Conclusion

Task Manager is a robust and efficient web application for task management, developed with the best web programming practices in Python. Using Flask, SQLAlchemy and other modern technologies, the project offers a pleasant user experience and essential features for personal organization and productivity.
