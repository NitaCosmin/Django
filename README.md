# Django Portfolio Project

A personal portfolio website built with Django.

## Features
- User profiles with images
- CV/Resume upload and display
- User browsing system
- Authentication system (login/register)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NitaCosmin/Django.git
   cd Django
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file with:
   ```


5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
Django/
├── portfolio/          # Project config
├── main/               # Main app
├── manage.py
├── requirements.txt
└── README.md
```

## Deployment

For production deployment, see [Django deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/).

