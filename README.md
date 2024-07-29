# Expense Sharing App

Welcome to the **Expense Sharing App**! This web application is designed to simplify managing and tracking shared expenses among users. It features user management, expense tracking, and provides downloadable reports in Excel format.

## Features

- **User Management**: Add, edit, and delete users.
- **Expense Tracking**: Manage expenses, specifying sharing modes (equal, exact, percentage).
- **Dynamic Expense Calculation**: Automatically calculates how much each user owes based on the chosen sharing mode.
- **Balance Sheet**: View and download a comprehensive balance sheet of all expenses.
- **Responsive UI**: Modern and intuitive design using Bootstrap.

## Technologies

- **Python**: Programming language used for backend development.
- **Flask**: Lightweight web framework for Python.
- **SQLAlchemy**: ORM for database management.
- **Bootstrap**: Front-end framework for responsive design.
- **Pandas**: Data manipulation library for generating Excel reports.
- **OpenPyXL**: Library for reading and writing Excel files.

## Installation

To get started with the Expense Sharing App, follow these instructions:

### Prerequisites

Ensure you have Python and `pip` installed. You’ll also need to have `git` if you want to clone the repository.

### Clone the Repository

```sh
git clone https://github.com/bhuwanb23/ExpenseSharing.git
cd ExpenseSharing
```

### Set Up a Virtual Environment

Create and activate a virtual environment to manage dependencies:

```sh
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages:

```sh
pip install -r requirements.txt
```

### Initialize the Database

Set up the database schema:

```sh
flask shell
from app import db
db.create_all()
exit()
```

### Run the Application

Start the Flask development server:

```sh
python app.py
```

Visit `http://127.0.0.1:5000/` in your web browser to access the application.

## Usage

### Home Page

- **Welcome Screen**: Navigate to different sections of the app.

### User Management

- **Add Users**: Enter user details such as name, email, phone, and address.
- **Edit Users**: Modify existing user details.
- **Delete Users**: Remove users from the system.

### Expense Management

- **Add Expenses**: Record new expenses, select users, and specify the sharing mode.
- **Edit Expenses**: Modify existing expense details.
- **Delete Expenses**: Remove expenses from the system.
- **Calculate Amounts**: Depending on the sharing mode, automatically calculate the amount each user owes.

### Balance Sheet

- **View Summary**: See a summary of all expenses and user balances.
- **Download Report**: Generate and download an Excel file containing individual and overall expense details.

## Project Structure

- **`app.py`**: Main application logic and routes.
- **`models.py`**: Defines the database models for users, expenses, and user expenses.
- **`templates/`**: Contains HTML templates for rendering views.

## Contributing

We welcome contributions to the Expense Sharing App! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## Acknowledgements

- **Flask**: For the lightweight web framework.
- **SQLAlchemy**: For easy database interactions.
- **Bootstrap**: For the responsive and modern UI.
- **Pandas**: For handling data and generating reports.
- **OpenPyXL**: For reading and writing Excel files.

Thank you for exploring the Expense Sharing App! We hope it simplifies your expense management tasks and makes sharing costs with others easier.
