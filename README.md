# Bustan Altoor Technical Services Website

A professional Django website for **Bustan Altoor Technical Services** — a Dubai-based technical services company offering alternative energy equipment, tiling, carpentry, wood flooring, engraving, wallpaper, false ceiling, partition, and electrical fitting services.

## Features

- ✅ Professional Home page with hero section, services overview, why-choose-us, and CTA
- ✅ About Us page with company info, mission, vision, values, and stats
- ✅ Services page with detailed descriptions of all 7 services
- ✅ Contact Us page with working contact form and Google Map
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Modern animations using AOS (Animate On Scroll)
- ✅ Font Awesome icons throughout
- ✅ WhatsApp floating button
- ✅ Contact form that saves submissions to database
- ✅ Django admin to manage services and view contact messages

## Services Offered

1. Alternative Energy Equipment Installation and Maintenance
2. Floor & Wall Tiling Works
3. Carpentry & Wood Flooring Works
4. Engraving & Ornamentation Works
5. Wallpaper Fixing Works
6. False Ceiling & Light Partitions Installation
7. Electrical Fittings & Fixtures Repairing & Maintenance

## Tech Stack

- **Backend:** Django 5.0
- **Database:** SQLite (default)
- **Frontend:** HTML5, CSS3, JavaScript
- **Icons:** Font Awesome 6
- **Fonts:** Google Fonts (Poppins + Playfair Display)
- **Animations:** AOS Library

## Project Structure

```
baston-/
├── manage.py
├── requirements.txt
├── bostan_website/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                   # Main app
│   ├── models.py           # Service & ContactMessage models
│   ├── views.py            # Home, About, Services, Contact views
│   ├── forms.py            # Contact form
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── templates/main/         # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── services.html
│   └── contact.html
├── static/                 # Static files
│   ├── css/style.css
│   ├── js/script.js
│   └── images/             # Service images (download via script)
└── download_images.py      # Script to fetch professional images
```

## Setup & Installation

### 1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Download images (optional but recommended)

```bash
python download_images.py
```

### 5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Open your browser

Visit: **http://127.0.0.1:8000/**

## Pages

- **Home:** `http://127.0.0.1:8000/`
- **About:** `http://127.0.0.1:8000/about/`
- **Services:** `http://127.0.0.1:8000/services/`
- **Contact:** `http://127.0.0.1:8000/contact/`
- **Admin:** `http://127.0.0.1:8000/admin/`

## Customization

- **Company info:** Edit templates (phone, email, address in `base.html` and `contact.html`)
- **Colors:** Modify CSS variables in `static/css/style.css` (look for `:root`)
- **Services:** Add/edit services via Django admin
- **Images:** Replace images in `static/images/` folder

## Contact

For any questions or support, please contact Bustan Altoor Technical Services.
