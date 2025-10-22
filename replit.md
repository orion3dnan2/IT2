# IT Asset Management System

## Overview

This is a bilingual (English/Arabic) IT Asset Management web application built with Python Flask. The system helps IT departments track and manage hardware assets including computers, monitors, printers, scanners, and network devices. It provides features for inventory management, asset assignment to employees, maintenance tracking, and reporting with a modern, responsive interface supporting both light and dark modes.

**Status**: Fully functional MVP with all core features implemented and tested.

## Recent Changes (October 22, 2025)

- ✅ Complete project setup with Flask, SQLAlchemy, Flask-Login, Flask-Babel
- ✅ Implemented all database models with proper relationships
- ✅ Created authentication system with role-based access control (Admin, Staff, Viewer)
- ✅ Built bilingual interface with Arabic/English support and RTL/LTR switching
- ✅ Developed responsive UI with TailwindCSS, dark mode, and modern design
- ✅ Implemented full CRUD operations for Assets, Employees, and Maintenance
- ✅ Created interactive dashboard with KPI cards and statistics
- ✅ Added search and filtering capabilities for all entities
- ✅ Set up PostgreSQL database with seed data
- ✅ Configured workflow and verified application runs successfully

## User Preferences

- Preferred communication style: Simple, everyday language
- Language support: Bilingual (Arabic/English)
- UI Design: Modern, clean, responsive with royal blue, silver gray, and emerald green color palette
- Dark mode: Fully supported with localStorage persistence

## System Architecture

### Backend Architecture

**Framework**: Flask with Blueprint-based modular architecture
- Blueprints organize features into separate modules: `auth`, `dashboard`, `assets`, `employees`, `maintenance`, and `main`
- Each blueprint handles its own routing and business logic independently

**ORM & Database**: SQLAlchemy ORM with PostgreSQL
- Database connection uses psycopg2-binary driver
- SQLAlchemy handles all database operations with model-based queries
- Flask-Migrate available for database schema migrations
- Configuration uses DATABASE_URL environment variable from Replit

**Authentication & Authorization**: Flask-Login
- Role-based access control with three levels: `admin`, `staff`, and `viewer`
- Password hashing using Werkzeug security utilities
- Session-based authentication with configurable session secrets
- Permission checking implemented through `User.has_permission()` method

**Internationalization**: Flask-Babel
- Supports English and Arabic with automatic RTL/LTR layout switching
- Translation directories managed through Babel configuration at `app/translations`
- Language selection stored in session and can be changed dynamically
- Locale detection from session or browser preferences

### Frontend Architecture

**UI Framework**: TailwindCSS (CDN-based for development)
- Responsive design with mobile-first approach
- Dark mode support with localStorage persistence
- Custom color palette: royal blue (#1e3a8a), silver gray (#64748b), and emerald green (#10b981)
- Conditional RTL/LTR styling based on selected language

**Typography**:
- Arabic: Cairo font from Google Fonts
- English: Inter font from Google Fonts

**Icons**: Font Awesome 6.4.0 for consistent iconography

**JavaScript**: Vanilla JavaScript for:
- Dark mode toggle functionality
- Mobile sidebar menu toggle
- Client-side interactivity

**Templates**: Jinja2 templating with inheritance
- Base layout (`base/layout.html`) provides core HTML structure with language detection
- Dashboard layout (`base/dashboard_layout.html`) adds sidebar navigation
- Feature-specific templates extend dashboard layout

### Data Model

**Core Entities**:
- **User**: Authentication and authorization with roles (admin/staff/viewer)
- **Asset**: IT hardware with type, status, warranty tracking, and assignment
- **Employee**: Staff members who can be assigned assets
- **Department**: Organizational units for both employees and assets
- **Maintenance**: Service records linked to assets with bilingual descriptions
- **AssetHistory**: Audit trail for asset changes

**Relationships**:
- Assets can be assigned to employees and departments (many-to-one)
- Assets have multiple maintenance records and history entries (one-to-many with cascade delete)
- Employees belong to departments and can have multiple assigned assets
- Maintenance records link to assets and track who created them
- Asset history tracks all changes with user attribution

**Key Features**:
- Bilingual field support (name_en/name_ar, description_en/description_ar)
- Automatic timestamp tracking (created_at, updated_at)
- Soft delete support through is_active flags
- Warranty expiration tracking with computed property

### External Dependencies

**Python Packages**:
- `Flask`: Web framework (3.1.2)
- `Flask-SQLAlchemy`: ORM integration (3.1.1)
- `Flask-Login`: Authentication management (0.6.3)
- `Flask-Migrate`: Database migration tool (4.1.0)
- `Flask-Babel`: Internationalization support (4.0.0)
- `psycopg2-binary`: PostgreSQL database driver (2.9.11)
- `python-dotenv`: Environment variable management (1.1.1)
- `Werkzeug`: Password hashing utilities (3.1.3)
- `cryptography`: Security utilities (46.0.3)

**Database**: PostgreSQL (Neon-backed on Replit)
- Connection via DATABASE_URL environment variable
- Character set: UTF8 for full Unicode support including Arabic

**Frontend CDN Resources**:
- TailwindCSS: CSS framework (cdn.tailwindcss.com) - development only
- Font Awesome: Icon library (6.4.0 from cdnjs.cloudflare.com)
- Google Fonts: Cairo (Arabic), Inter (English)

**Optional Future Integrations** (mentioned in requirements but not yet implemented):
- Chart.js: For dashboard statistics visualization
- xlsxwriter: Excel report generation
- ReportLab: PDF report generation

## Default Login Credentials

The system comes pre-configured with three user accounts for testing different access levels:

- **Admin**: Username: `admin`, Password: `admin123` (Full access to all features)
- **Staff**: Username: `staff`, Password: `staff123` (Can view and edit, cannot delete)
- **Viewer**: Username: `viewer`, Password: `viewer123` (View-only access)

## Sample Data

The database is seeded with:
- 5 Departments (IT, Finance, HR, Marketing, Operations)
- 5 Employees across different departments
- 10 Assets (computers, monitors, printers, scanners, network devices)
- Realistic warranty dates and assignments

## Running the Application

The application is configured to run automatically via the Server workflow:
- Command: `python run.py`
- Port: 5000
- URL: Accessible via Replit webview

To reset the database:
```bash
python seed_data.py
```

## Project Structure

```
/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models/                  # Database models
│   │   ├── user.py
│   │   ├── asset.py
│   │   ├── employee.py
│   │   ├── department.py
│   │   ├── maintenance.py
│   │   └── asset_history.py
│   ├── blueprints/              # Application modules
│   │   ├── auth/                # Authentication
│   │   ├── dashboard/           # Main dashboard
│   │   ├── assets/              # Asset management
│   │   ├── employees/           # Employee management
│   │   ├── maintenance/         # Maintenance tracking
│   │   └── main/                # Main routes (home, language)
│   ├── templates/               # Jinja2 templates
│   │   ├── base/                # Base layouts
│   │   ├── auth/                # Login pages
│   │   ├── dashboard/           # Dashboard views
│   │   ├── assets/              # Asset CRUD pages
│   │   ├── employees/           # Employee CRUD pages
│   │   └── maintenance/         # Maintenance pages
│   └── translations/            # Babel translations
│       ├── en/LC_MESSAGES/      # English translations
│       └── ar/LC_MESSAGES/      # Arabic translations
├── config.py                    # Application configuration
├── run.py                       # Application entry point
├── seed_data.py                # Database seeding script
├── babel.cfg                    # Babel configuration
└── replit.md                   # This file

```

## Features Implemented

### ✅ Core Features (MVP)
1. User Authentication with role-based access control
2. Bilingual interface (Arabic/English) with RTL/LTR support
3. Asset Management (CRUD) with search and filtering
4. Employee Management with asset assignment
5. Maintenance logging and tracking
6. Dashboard with KPI cards and statistics
7. Asset history tracking
8. Responsive UI with dark mode
9. Mobile-friendly sidebar navigation

### 🔜 Future Enhancements
1. Excel and PDF report exports
2. Chart.js visualizations
3. Image upload for assets
4. Advanced report filtering
5. Warranty expiry notifications
6. Email notifications
7. Asset barcode/QR code generation
8. Advanced analytics and trends

## API Endpoints

### Authentication
- `GET /auth/login` - Login page
- `POST /auth/login` - Process login
- `GET /auth/logout` - Logout

### Dashboard
- `GET /dashboard/` - Main dashboard with statistics

### Assets
- `GET /assets/` - List all assets (with pagination, search, filters)
- `GET /assets/add` - Add asset form
- `POST /assets/add` - Create new asset
- `GET /assets/edit/<id>` - Edit asset form
- `POST /assets/edit/<id>` - Update asset
- `POST /assets/delete/<id>` - Delete asset (admin only)
- `GET /assets/view/<id>` - View asset details and history

### Employees
- `GET /employees/` - List all employees
- `GET /employees/add` - Add employee form
- `POST /employees/add` - Create new employee
- `GET /employees/edit/<id>` - Edit employee form
- `POST /employees/edit/<id>` - Update employee
- `POST /employees/delete/<id>` - Delete employee (admin only)
- `GET /employees/view/<id>` - View employee details

### Maintenance
- `GET /maintenance/` - List all maintenance records
- `GET /maintenance/add` - Add maintenance form
- `POST /maintenance/add` - Create maintenance record
- `GET /maintenance/edit/<id>` - Edit maintenance form
- `POST /maintenance/edit/<id>` - Update maintenance record
- `POST /maintenance/delete/<id>` - Delete record (admin only)

### Other
- `GET /` - Redirects to dashboard
- `GET /set_language/<language>` - Switch interface language

## Notes

- Production deployment requires:
  - Secure SECRET_KEY configuration
  - Production-grade WSGI server (Gunicorn recommended)
  - TailwindCSS build process (not CDN)
  - SSL/HTTPS configuration
  - Regular database backups
