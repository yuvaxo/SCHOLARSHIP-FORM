# Scholarship Form Website Project: Setup and Installation Guide

Welcome to the comprehensive guide for setting up the development environment for the Scholarship Form Website project. This guide will walk you through the steps required to install and configure the necessary tools, databases, and libraries to get your project up and running. The project involves building a web application using Django, with Oracle DB 21c XE as the database backend. Visual Studio Code (VSC) will be used as the code editor.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Step 1: Installing Oracle Database 21c XE](#step-1-installing-oracle-database-21c-xe)
4. [Step 2: Installing Python](#step-2-installing-python)
5. [Step 3: Setting Up Visual Studio Code (VSC)](#step-3-setting-up-visual-studio-code-vsc)
6. [Step 4: Installing Django](#step-4-installing-django)
7. [Step 5: Configuring the Project Environment](#step-5-configuring-the-project-environment)
8. [Step 6: Running the Project](#step-6-running-the-project)
9. [Troubleshooting](#troubleshooting)
10. [Conclusion](#conclusion)

---

## Introduction

The Scholarship Form Website project is designed to manage and process scholarship applications. The application is built using the Django framework and utilizes Oracle Database 21c XE as the backend to store and manage data. This guide provides detailed instructions on setting up the development environment and configuring all necessary components.

## Prerequisites

Before you begin, ensure that you have the following:

- A machine running Windows, macOS, or Linux.
- Administrative privileges to install software.
- Internet access to download required packages and libraries.

## Step 1: Installing Oracle Database 21c XE

Oracle Database 21c XE (Express Edition) is a free, lightweight version of Oracle's powerful database system. It will be used to store and manage the scholarship data.

### Installation Steps:

1. *Download Oracle Database 21c XE*:
   - Visit the [Oracle Database XE download page](https://www.oracle.com/database/technologies/xe-downloads.html).
   - Download the installer for your operating system.

2. *Install Oracle Database 21c XE*:
   - Run the downloaded installer.
   - Follow the on-screen instructions to complete the installation.
   - During installation, you will be prompted to set up a password for the SYS and SYSTEM administrative accounts. Make sure to remember this password as it will be needed later.

3. *Configure Oracle Environment Variables*:
   - Add the Oracle DB environment variables to your system’s PATH. This will allow you to run Oracle commands from the command line.
   - Example for Windows: 
     - Open the System Properties and navigate to Environment Variables.
     - Add the Oracle bin directory (e.g., C:\app\user\product\21c\dbhomeXE\bin) to the PATH variable.

4. *Install Oracle Python Libraries*:
   - Open a command prompt and navigate to your project’s directory.
   - Run the following commands to install the necessary Python libraries:
     bash
     pip install oracledb
     pip install cx_oracle
     

## Step 2: Installing Python

Python is the programming language used to build the Django web application. If Python is not already installed on your system, follow these steps:

1. *Download and Install Python*:
   - Visit the [Python official website](https://www.python.org/downloads/) and download the latest version of Python.
   - Run the installer and make sure to check the option to add Python to your PATH.

2. *Verify Installation*:
   - Open a command prompt and type python --version to verify that Python is installed correctly.

## Step 3: Setting Up Visual Studio Code (VSC)

Visual Studio Code (VSC) is a lightweight, yet powerful code editor that will be used to write and manage the project’s code.

### Installation Steps:

1. *Download Visual Studio Code*:
   - Visit the [Visual Studio Code website](https://code.visualstudio.com/) and download the installer for your operating system.

2. *Install Visual Studio Code*:
   - Run the installer and follow the on-screen instructions to complete the installation.

3. *Install Required Extensions*:
   - Launch Visual Studio Code.
   - Navigate to the Extensions view by clicking on the Extensions icon in the sidebar or pressing Ctrl+Shift+X.
   - Install the following extensions:
     - Python
     - Django
     - Oracle Developer Tools for Visual Studio Code (optional)

4. *Install Visual C++ Build Tools*:
   - Some Python packages require C++ build tools to compile. Install Visual C++ Build Tools from the [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) website.

## Step 4: Installing Django

Django is the web framework that will be used to build the Scholarship Form Website.

### Installation Steps:

1. *Install Django*:
   - Open a command prompt and run the following command:
     bash
     pip install django
     

2. *Verify Installation*:
   - To verify that Django is installed correctly, type django-admin --version in the command prompt.

## Step 5: Configuring the Project Environment

### Setting Up the Django Project:

1. *Create a Virtual Environment*:
   - Navigate to your project’s directory in the command prompt.
   - Create a virtual environment by running:
     bash
     python -m venv myenv
     
   - Activate the virtual environment:
     - On Windows: myenv\Scripts\activate
     - On macOS/Linux: source myenv/bin/activate

2. *Install Django in the Virtual Environment*:
   - If Django is not installed in the virtual environment, install it by running:
     bash
     pip install django
     

3. *Create a New Django Project*:
   - Run the following command to start a new Django project:
     bash
     django-admin startproject scholarship_form
     

4. *Set Up Oracle DB in Django*:
   - Open the settings.py file in your Django project.
   - Modify the DATABASES section to configure Oracle DB as your database backend:
     python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.oracle',
             'NAME': 'XE',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '1521',
         }
     }
     

5. *Apply Migrations*:
   - Run the following commands to apply initial migrations:
     bash
     python manage.py makemigrations
     python manage.py migrate
     

## Step 6: Running the Project

After completing the setup, you can now run the Django development server to start the Scholarship Form Website.

1. *Run the Development Server*:
   - In the command prompt, navigate to the project directory where manage.py is located.
   - Run the following command:
     bash
     python manage.py runserver
     
   - Open a web browser and navigate to http://127.0.0.1:8000/ to view the project.

## Troubleshooting

- *Handling Exceptions*: If any exceptions occur during the setup or while running the project, check the Django logs for detailed error messages. This will help in identifying and fixing the issues.
- *Database Connection Issues*: Ensure that Oracle DB is running and that the connection details in settings.py are correct.
- *Login and Authentication*: After setting up the project, you may need to modify the default Django authentication system to fit your specific login requirements.

## Conclusion

This guide has walked you through the steps to set up a development environment for the Scholarship Form Website project. By following these instructions, you will have a fully functional Django application with Oracle DB 21c XE as the backend. This setup provides a solid foundation for further development and customization of your scholarship management system.
