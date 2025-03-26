# CRM Project

This is the project that I've completed during my internship at Haroon Technology.

## Overview

This project is a Customer Relationship Management (CRM) system built using the Django framework. It provides tools for managing customer interactions, tracking sales leads, and organizing customer data.

## Features

*   **Lead Management:** Create, track, and manage leads through various stages of the sales process.
*   **Customer Database:** Store and organize customer information, including contact details, communication history, and purchase records.
*   **User Authentication:** Secure user accounts with authentication and authorization.
*   **Intuitive Interface:** User-friendly design for easy navigation and efficient data management.

## Technologies Used

*   **Django:** A high-level Python web framework for rapid development.
*   **Python:** The primary programming language.
*   **HTML/CSS/JavaScript:** For front-end development and user interface design.
*   **SQLite (or other database):** For storing application data.

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd CRM_Project
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS and Linux
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Submit a pull request.

## License

[Specify the license under which the project is released, e.g., MIT License]
