# mysite-django

A practical project in Python and Django template. All modules is needed to be remove according to your business.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About

Provide a more detailed description of your project. Explain what it does, why it exists, and any other relevant information.

## Features

List the key features of your project. You can use bullet points for better readability.

- For Django `5.0.1`
- Work with Python `3.12.0`
- Dockerize MySQL `8.2.0`

## Getting Started

Provide instructions on how to get your project up and running.

### Installation

1. Clone repo from github

   `git clone git@github.com:quy-np/mysite-django.git`

2. Open downloaded project, install all packages from requirements.txt

   `pip install -r requirements.txt`

3. To create a migration for the model, use the below-given command. Inside the migration folder, a migration file will be created.

   `python manage.py makemigrations`

4. Create a migration and then migrate it to reflect the database. Below is the migrate command.

   `python manage.py migrate`

5. If you would like to run the script sample by typing the below-given command.

   `python manage.py runserver`
