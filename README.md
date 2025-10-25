# Enterprise CRM System

[![Django](https://img.shields.io/badge/Django-5.1.6-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive **Customer Relationship Management (CRM)** system built with Django, designed for businesses to manage customer interactions, track sales leads, process orders, and maintain product catalogs. This enterprise-grade application features secure user authentication, responsive design, and scalable architecture.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Database Schema](#database-schema)
- [Security Features](#security-features)
- [Performance](#performance)
- [License](#license)

## Features

### **User Management & Authentication**
- **Secure User Registration & Login** with Django's built-in authentication
- **Role-based Access Control** with user-specific data isolation
- **Session Management** with automatic logout and security features
- **Password Validation** with Django's security validators

### **Customer Relationship Management**
- **Complete Customer Database** with comprehensive contact information
- **Advanced Search & Filtering** across customer records
- **Customer History Tracking** with order and interaction history
- **Geographic Data Management** (City, District, Country)
- **Contact Information Management** (Email, Phone, Address)

### **Product Catalog Management**
- **Product Database** with pricing and description management
- **Inventory Tracking** with creation date and user association
- **Product-Customer Relationship** mapping
- **Dynamic Product Updates** with real-time changes

### **Order Processing System**
- **Complete Order Lifecycle Management** (Pending → Shipping → Delivered → Cancelled)
- **Multi-Product Order Support** with many-to-many relationships
- **Order Status Tracking** with real-time updates
- **Customer-Order Association** for comprehensive tracking
- **Order Amount Validation** with business rules

### **Dashboard & Analytics**
- **Unified Dashboard** with customer and order overview
- **Real-time Search** across customers and orders
- **Data Visualization** with intuitive interfaces
- **Quick Actions** for common operations

### **User Experience**
- **Responsive Design** optimized for desktop and mobile
- **Intuitive Navigation** with Bootstrap 4 styling
- **Form Validation** with user-friendly error messages
- **Success/Error Notifications** for user feedback

## Technology Stack

### **Backend**
- **Django 5.1.6** - High-level Python web framework
- **Python 3.10+** - Core programming language
- **SQLite3** - Lightweight database for development
- **Django ORM** - Object-Relational Mapping for database operations

### **Frontend**
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling and responsive design
- **JavaScript** - Interactive user interface components
- **Bootstrap 4** - Responsive CSS framework
- **Crispy Forms** - Enhanced Django form rendering

### **Development Tools**
- **Django Admin** - Administrative interface
- **Django Debug Toolbar** - Development debugging
- **Git** - Version control system
- **Virtual Environment** - Dependency isolation

## Architecture

```
CRM_Project/
├── crm_project/                # Django project configuration
│   ├── settings.py             # Application settings
│   ├── urls.py                 # URL routing
│   └── wsgi.py                 # WSGI configuration
├── crmapp/                     # Main application
│   ├── models.py               # Database models
│   ├── views.py                # Business logic
│   ├── forms.py                # Form definitions
│   ├── urls.py                 # URL patterns
│   └── templates/              # HTML templates
├── static/                     # Static assets
│   ├── css/                    # Stylesheets
│   └── js/                     # JavaScript files
└── manage.py                   # Django management script
```

### **MVC Architecture**
- **Models**: Database schema and business logic (`models.py`)
- **Views**: Request handling and response logic (`views.py`)
- **Templates**: User interface presentation (`templates/`)
- **Forms**: Data validation and user input handling (`forms.py`)

## Installation

### **Prerequisites**
- Python 3.10 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### **Step 1: Clone the Repository**
    ```bash
git clone https://github.com/mertcaliskan34/CRM-Project.git
cd CRM-Project
```

### **Step 2: Create Virtual Environment**
```bash
# Create virtual environment
python -m venv myvenv

# Activate virtual environment
# On Windows:
myvenv\Scripts\activate
# On macOS/Linux:
source myvenv/bin/activate
```

### **Step 3: Install Dependencies**
    ```bash
pip install django==5.1.6
pip install django-crispy-forms
pip install crispy-bootstrap4
    ```

### **Step 4: Database Setup**
```bash
# Apply database migrations
python manage.py migrate

# Create superuser account
    python manage.py createsuperuser
    ```

### **Step 5: Run Development Server**
    ```bash
    python manage.py runserver
    ```

### **Step 6: Access Application**
Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage

### **Getting Started**
1. **Register** a new user account or use existing credentials
2. **Login** to access the dashboard
3. **Create Customer Records** with complete contact information
4. **Add Products** to your catalog with pricing and descriptions
5. **Process Orders** by linking customers with products
6. **Track Order Status** through the complete lifecycle

### **Key Workflows**

#### **Customer Management**
```python
# Create a new customer record
POST /create-record/
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@email.com",
    "phone": "+1234567890",
    "address": "123 Main St",
    "city": "New York",
    "district": "Manhattan",
    "country": "USA"
}
```

#### **Product Management**
```python
# Add a new product
POST /add-product/
{
    "name": "Premium Widget",
    "price": 99.99,
    "description": "High-quality widget for professional use"
}
```

#### **Order Processing**
```python
# Create a new order
POST /create-order/
{
    "order_number": "ORD001",
    "customer": "customer_id",
    "products": ["product_id1", "product_id2"],
    "amount": 2,
    "status": "pending"
}
```

## Database Schema

### **Core Models**

#### **Record Model** (Customer Management)
```python
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
```

#### **Product Model** (Inventory Management)
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
```

#### **Order Model** (Sales Processing)
```python
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=5)
    customer = models.ForeignKey(Record, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True)
```

## Security Features

### **Authentication & Authorization**
- **Django's Built-in Authentication** system
- **CSRF Protection** for all forms
- **User Session Management** with secure cookies
- **Password Hashing** with Django's PBKDF2 algorithm
- **Login Required Decorators** for protected views

### **Data Security**
- **User Data Isolation** - Users can only access their own data
- **SQL Injection Protection** through Django ORM
- **XSS Protection** with Django's template auto-escaping
- **Secure Headers** with Django's security middleware

### **Input Validation**
- **Form Validation** with Django forms
- **Model Validation** with field constraints
- **Business Rule Validation** (e.g., order amount limits)

## Performance

### **Database Optimization**
- **Efficient Queries** using Django ORM select_related and prefetch_related
- **Database Indexing** on frequently queried fields
- **Query Optimization** with minimal database hits

### **Frontend Performance**
- **Static File Optimization** with Django's static file handling
- **Responsive Design** for optimal mobile performance
- **Minimal JavaScript** for fast page loads

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Django Community** for the excellent framework
- **Bootstrap Team** for the responsive CSS framework
- **Haroon Technology** for the internship opportunity
- **Open Source Contributors** for the amazing tools and libraries

---

**If you found this project helpful, please give it a star!**

*This CRM system demonstrates enterprise-level Django development skills, including user authentication, database design, form handling, and responsive web design. Perfect for showcasing full-stack development capabilities to potential employers.*
