# Employee Management System

A Python-based desktop application for managing employee records with a graphical user interface and MySQL database integration.

## 📌 Project Overview

The Employee Management System is designed to simplify employee record management. It provides an easy-to-use graphical interface that allows users to add, view, search, update, and delete employee information.

The application is developed using Python and CustomTkinter, with MySQL used for storing employee records.

## 🚀 Features

### 1. Login System
- User login interface.
- Username and password validation.
- Empty-field validation.
- Error messages for invalid credentials.
- Opens the employee management dashboard after successful login.

### 2. Employee Management
- Add new employee records.
- View all employee records.
- Update existing employee information.
- Delete individual employee records.
- Delete all employee records.
- Clear employee input fields.
- Prevent duplicate employee IDs.

### 3. Search Functionality

Search employee records using:
- Employee ID
- Employee Name
- Phone Number
- Role
- Gender
- Salary

### 4. Database Management
- MySQL database connectivity.
- Automatic database creation.
- Automatic employee table creation.
- Insert employee records.
- Update employee records.
- Delete employee records.
- Retrieve employee records.
- Search employee records.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CustomTkinter | Modern graphical user interface |
| Tkinter | GUI components and message boxes |
| MySQL | Database management |
| PyMySQL | Python-MySQL connectivity |
| Pillow (PIL) | Image processing |
| Git | Version control |
| GitHub | Source code hosting |

## 📂 Project Structure

```text
employee-management-system/
│
├── .gitignore
├── README.md
├── bg.jpg
├── cover.jpg
├── database.py
├── ems.py
└── login.py
```

### File Description

| File | Description |
|---|---|
| `login.py` | Handles the application login interface and authentication |
| `ems.py` | Main employee management application and GUI |
| `database.py` | Handles MySQL database connectivity and CRUD operations |
| `bg.jpg` | Background image for the employee management dashboard |
| `cover.jpg` | Background image for the login page |
| `.gitignore` | Specifies files and directories ignored by Git |
| `README.md` | Project documentation |

## 🗄️ Database Structure

**Database Name:** `employee_data`

**Table Name:** `data`

The application automatically creates the database and employee table when the MySQL connection is successful.

### Employee Table Columns

| Column | Data Type | Description |
|---|---|---|
| Id | VARCHAR(20) | Unique employee identifier |
| Name | VARCHAR(50) | Employee name |
| Phone | VARCHAR(15) | Employee phone number |
| Role | VARCHAR(50) | Employee designation |
| Gender | VARCHAR(20) | Employee gender |
| Salary | DECIMAL(10,2) | Employee salary |

### Database Operations

The `database.py` file contains the following functions:

| Function | Description |
|---|---|
| `connect_database()` | Connects to MySQL and creates the database and table |
| `insert()` | Inserts a new employee record |
| `id_exists()` | Checks whether an employee ID already exists |
| `fetch_employees()` | Retrieves all employee records |
| `update()` | Updates existing employee information |
| `delete()` | Deletes an employee record |
| `search()` | Searches employee records |
| `deleteall_records()` | Deletes all records from the employee table |

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Dharshank8/employee-management-system.git
```

### Step 2: Navigate to the Project Directory

```bash
cd employee-management-system
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Dependencies

```bash
pip install customtkinter pymysql pillow
```

### Step 6: Configure MySQL

1. Install MySQL Server on your system.
2. Start the MySQL service.
3. Open the `database.py` file.
4. Configure your local MySQL host, username, and password.
5. Make sure your MySQL credentials are configured securely.

The application automatically creates the `employee_data` database and `data` table when the connection is successful.

**Security Note:** Do not commit database passwords or other sensitive credentials to GitHub. Use environment variables for database configuration.

### Step 7: Run the Application

Execute the following command:

```bash
python login.py
```

The login window will appear. After successful authentication, the Employee Management System dashboard will open.

## 🆔 Employee ID Format

Employee IDs must start with `EMP`.

Examples:

```text
EMP1
EMP2
EMP3
EMP101
```

Duplicate employee IDs are not allowed.

## 🔄 Application Workflow

1. Launch the application.
2. Enter login credentials.
3. Access the employee management dashboard.
4. Enter employee details.
5. Add employee records to the database.
6. View all employee records.
7. Search for employees using different fields.
8. Select an employee to update or delete information.
9. Delete all employee records when required.

## 🔮 Future Enhancements

- Implement secure password hashing.
- Add user registration functionality.
- Implement role-based access control.
- Add employee profile management.
- Add employee attendance tracking.
- Generate employee reports.
- Add salary report generation.
- Improve input validation and error handling.
- Add export functionality for employee records.

## 🔐 Security Considerations

- Store database credentials securely using environment variables.
- Avoid committing passwords and sensitive information to GitHub.
- Replace hardcoded login credentials with secure authentication.
- Use password hashing for user authentication.
- Validate user inputs before database operations.

## 👨‍💻 Author

**Dharshan KS**

GitHub: [Dharshank8](https://github.com/Dharshank8)

Project Repository: [Employee Management System](https://github.com/Dharshank8/employee-management-system)

## 📄 License

This project is developed for educational and learning purposes.