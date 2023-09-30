# American Council of the Blind Website

Welcome to the American Council of the Blind (ACB) website! This website serves as a hub for our community, providing several key features to enhance our members' experience and streamline volunteer coordination. Below, you'll find detailed information on the website's features and the technologies used to develop it.

## Table of Contents

- [Features](#features)
  - [1. Event Scheduling](#1-event-scheduling)
  - [2. Volunteer Coordination](#2-volunteer-coordination)
  - [3. Email Reminders](#3-email-reminders)
- [Technologies Used](#technologies-used)
  - [1. Django Framework][def]
  - [2. Python Programming Language](#2-python-programming-language)
    - [3. HTML and CSS](#3-html-and-css)
    - [4. SQLite Database](#4-sqlite-database)
    - [5. EC2 Instance](#5-ec2-instance)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### 1. Event Scheduling

Our website allows ACB to schedule and manage events easily. Members can view upcoming events, details, and registration information. This feature simplifies event planning and ensures that the community is well-informed about upcoming activities.

### 2. Volunteer Coordination

We've integrated a volunteer coordination system to make it simple for ACB members to offer their assistance for events. Volunteers can sign up for specific tasks, helping to ensure that events run smoothly.

### 3. Email Reminders

To keep members and volunteers informed, our website can automatically send email reminders about upcoming events. This feature ensures that everyone is well-prepared and never misses an event they've signed up for.

---

## Technologies Used

### 1. Django Framework

Our website is built using the Django web framework, which provides a robust and secure foundation for web applications. Django's versatility allows us to create complex features like event scheduling and volunteer coordination.

### 2. Python Programming Language

Python is the primary programming language used for building the website. It's known for its simplicity and readability, making it ideal for web development tasks.

### 3. HTML and CSS

HTML and CSS are used for creating the website's frontend. HTML structures the content, while CSS ensures a visually appealing and responsive design.

### 4. SQLite Database

We utilize an SQLite database to store and manage data related to events, members, volunteers, and email reminders. SQLite is a lightweight, serverless database that suits our needs.

### 5. EC2 Instance

To host the website virtually, we've deployed it on an Amazon Elastic Compute Cloud (EC2) instance. This ensures high availability and scalability for our web application.

---

## Getting Started

To get started with the ACB website, follow these steps:

1. Clone this repository to your local machine.

```
git clone <repository_url>
```

2. Install the required dependencies. You may use a virtual environment to manage dependencies.

```
pip install -r requirements.txt
```

3. Move to the `fix` branch. This is our working branch

```
git checkout fix
```

4. Configure your Django settings, including database settings and email configuration, as needed.

5. Run migrations to create the database tables.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Start the development server.

```
python3 manage.py runserver
```

7. Access the website in your web browser at `http://localhost:8000`.

---

## Contributing

We welcome contributions from the ACB community and developers interested in improving our website. To contribute, please follow our [Contributing Guidelines](CONTRIBUTING.md).

---

## License

This project is licensed under the [MIT License](LICENSE.md).

---

Thank you for using the American Council of the Blind website! If you encounter any issues or have suggestions for improvement, please don't hesitate to [contact us](mailto:contact@acb.org). Your feedback is valuable to us.

[def]: #1-django-framework
