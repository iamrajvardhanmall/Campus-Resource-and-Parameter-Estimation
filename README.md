# Campus Resource & Parameter Estimation System

A Django-based web application for monitoring and analyzing campus resources — including courses, faculty workload, classroom utilization, and student enrollment — all from a single interactive dashboard.

---

## Features

- **Live Dashboard** — Overview of all campus resources at a glance
- **Course Analysis** — Tracks enrolled students, assigned faculty, classroom allocation, and credit hours per course
- **Faculty Workload Estimation** — Calculates total teaching credits and classifies workload (Light / Normal / Heavy / Overloaded)
- **Classroom Utilization** — Measures capacity usage per classroom and flags under/over-utilized rooms
- **Student Management** — Tracks student enrollments across multiple courses
- **Django Admin Panel** — Full CRUD management for all entities (Blocks, Classrooms, Faculty, Courses, Students)
- **Robust Error Handling** — Graceful fallback if any data calculation fails

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django 6.0.2 |
| Database | SQLite (via Django ORM) |
| Frontend | HTML5, CSS3, JavaScript |
| Icons | Font Awesome 6.4.0 |
| Environment | Python Virtual Environment |

---

## Project Structure

```
Campus-Resource-and-Parameter-Estimation/
├── Campus/                   # Python virtual environment
├── campus_system/            # Django project root
│   ├── manage.py
│   ├── db.sqlite3
│   ├── campus_system/        # Project settings & URL configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── core/                 # Main application
│       ├── models.py         # Data models (Block, Classroom, Faculty, Course, Student)
│       ├── views.py          # Dashboard view logic
│       ├── admin.py          # Admin panel registration
│       ├── urls.py           # App URL routes
│       ├── migrations/       # Database migrations
│       ├── templates/
│       │   └── dashboard.html
│       └── static/
│           ├── css/dashboard.css
│           └── js/dashboard.js
└── README.md
```

---

## Data Models

### Block
Represents a physical building/block on campus.

### Classroom
Belongs to a `Block`. Tracks room number and seating capacity. Computes:
- **Capacity Utilization (%)** — based on enrolled students vs. room capacity
- **Utilization Status** — `Empty` / `Under-utilized` / `Well-utilized` / `Fully-utilized` / `Over-capacity`

### Faculty
Stores name and department. Computes:
- **Total Workload** — sum of credits across all assigned courses
- **Workload Status** — `No Load` / `Light Load` / `Normal Load` / `Heavy Load` / `Overloaded`

### Course
Links `Faculty` and `Classroom`. Tracks credit hours and enrolled students. Computes:
- **Enrolled Count**
- **Capacity Utilization (%)**
- **Utilization Status**

### Student
Has a name, roll number, and a many-to-many relationship with `Course`.

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Campus-Resource-and-Parameter-Estimation.git
   cd Campus-Resource-and-Parameter-Estimation
   ```

2. **Activate the virtual environment**

   On Windows:
   ```bash
   Campus\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source Campus/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   cd campus_system
   python manage.py migrate
   ```

5. **Create a superuser** (for Django Admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to:
   - Dashboard: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Usage

1. Log in to the **Admin Panel** to add Blocks, Classrooms, Faculty, Courses, and Students.
2. Visit the **Dashboard** to see live statistics and utilization analysis.
3. The dashboard automatically calculates:
   - Per-course capacity and enrollment metrics
   - Per-faculty teaching credit loads and workload classification
   - Per-classroom utilization percentages and status badges

---

## Utilization & Workload Classification

### Classroom / Course Utilization
| Utilization | Status |
|-------------|--------|
| 0% | Empty |
| 1% – 50% | Under-utilized |
| 51% – 80% | Well-utilized |
| 81% – 100% | Fully-utilized |
| > 100% | Over-capacity |

### Faculty Workload
| Total Credits | Status |
|--------------|--------|
| 0 | No Load |
| 1 – 12 | Light Load |
| 13 – 18 | Normal Load |
| 19 – 24 | Heavy Load |
| > 24 | Overloaded |

---

## Author

Developed by **Rajvardhan Mall**

---

## License

This project is for academic and educational purposes.