# Artisan & Client Platform

## Introduction

This project is an online platform designed to connect artisans and clients efficiently and transparently. In a digital world where finding qualified craftsmen for renovation projects is challenging, this platform provides a reliable solution to bridge the gap between demand and supply. The application simplifies the discovery, booking, and communication between artisans and clients.

---

## Features

### For Clients
- **User Registration and Login**: Create and manage accounts securely.
- **Artisan Search and Navigation**: Find artisans by specialty or location.
- **Booking Services**: Book artisans for projects with specific dates and details.
- **Messaging System**: Communicate directly with artisans.
- **Ratings and Reviews**: Share feedback on completed services.

### For Artisans
- **Profile Management**: Showcase expertise, hourly rates, and project history.
- **Booking Management**: Accept or decline bookings.
- **Role Switching**: Alternate between client and artisan roles if needed.

---

## Technologies Used

- **Backend**: Python with Django framework.
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap for styling).
- **Database**: SQLite for lightweight and self-contained data management.
- **Tools**: 
  - StarUML for modeling diagrams.
  - Django's built-in admin interface for backend management.

---

## Architecture Overview

- **Frontend**: User-facing templates for login, profile management, booking, and reviews.
- **Backend**: Modular Django applications (`account`, `bookings`, etc.).
- **Database**: A single SQLite file for managing all application data.
- **Static Files**: CSS, JavaScript, and images stored under the `static/` directory.

---

## Key Functionalities

1. **Authentication**: Secure login and registration for both clients and artisans.
2. **Search and Filters**: Find artisans based on location and specialty.
3. **Booking System**: Reserve artisans with messaging support.
4. **Review System**: Rate artisans post-service.
5. **Profile Customization**: Modify artisan and client profiles as needed.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/artisan-client-platform.git
   cd artisan-client-platform
   ```

2. **Set Up the Environment**:
   - Install Python 3.10 or higher.
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # or venv\Scripts\activate on Windows
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open `http://127.0.0.1:8000` in your browser.

---

## Future Improvements

- Integration of real-time notifications.
- Expansion to include rural areas.
- Mobile application development for broader accessibility.

