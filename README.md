# Diya Interactive Test

## Description

Provide a brief and clear description of your project. Explain its purpose, features, and what it does.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Admin Dashboard](#admin-dashboard)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Requirements

List the requirements for your project, including the Python version, Django version, and any external packages or libraries. You can provide an example `requirements.txt` file.

Example:

Python 3.8.x
Django 3.x
Django Rest Framework 3.x
MySQL 5.x / SQLite

Add other dependencies here
bash
Copy code

## Installation

Explain how to install and set up your project locally. Include any necessary steps or commands.

Example:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
Create a virtual environment (recommended) and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database in settings.py.

Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Usage
Explain how to use your project, including how to run the development server, access the API, and interact with the application.

Example:

Start the development server:

bash
Copy code
python manage.py runserver
Access the API:

Open your web browser or API client and access the API endpoints. For example, http://localhost:8000/api/get_all_active_patients/.

API Endpoints
Provide a list of your API endpoints, including a brief description of what each endpoint does.

Example:

/api/get_all_active_patients/: Active patients list.
/api/get_all_active_counsellors/: Active counsellors list.
/api/get_all_active_appointments/: Active appointments list.
Admin Dashboard
Explain how to access the admin dashboard for managing your application. Mention how to create an admin user.

Example:

Create a superuser:

bash
Copy code
python manage.py createsuperuser
Access the admin dashboard at http://localhost:8000/admin/.

Testing
Explain how to run the unit tests for your project.

Example:

To run the unit tests:

bash
Copy code
python manage.py test
Deployment
Provide instructions or recommendations for deploying your project to a production environment. You can include information about web servers, databases, and settings modifications.

Example:

Set DEBUG = False in your settings.py for production.

Configure a production database (e.g., PostgreSQL).

Serve your application with a production-ready web server (e.g., Gunicorn).

Set up a reverse proxy (e.g., Nginx).

Contributing
Explain how others can contribute to your project, including guidelines for submitting issues, feature requests, and pull requests.

License
Specify the license under which your project is released.

Example:

This project is licensed under the MIT License - see the LICENSE file for details.