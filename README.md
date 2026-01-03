# Superheroes API

A Flask REST API for tracking heroes and their superpowers, built as part of Phase 4 Code Challenge.

## Author
**Kenneth Kipkosgei** - *Full Stack Developer*

## About

This project demonstrates proficiency in building RESTful APIs using Flask, SQLAlchemy, and related technologies. It showcases proper database design with relationships, data validation, email integration, and follows industry best practices for API development. The application provides a complete backend solution for managing superhero data with comprehensive CRUD operations and email notifications.

## Description

This API allows you to manage a database of superheroes and their powers. You can:
- View all heroes and their details
- Manage superpowers and their descriptions
- Create associations between heroes and powers with strength levels
- Send email notifications

## Features

- **Hero Management**: Create, read, and manage superhero profiles
- **Power Management**: Manage superpowers with detailed descriptions
- **Hero-Power Associations**: Link heroes to powers with strength ratings
- **Email Integration**: Send email notifications via Flask-Mail
- **Data Validation**: Comprehensive validation for all models
- **RESTful API**: Clean, RESTful endpoints following best practices

## Technology Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Email**: Flask-Mail with Gmail SMTP
- **Migrations**: Flask-Migrate
- **Serialization**: SQLAlchemy-serializer

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd phase-4-code-challange-1
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your email credentials
   ```

5. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Seed the database**
   ```bash
   python seed.py
   ```

7. **Run the application**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### Heroes

- **GET /heroes** - Get all heroes
- **GET /heroes/:id** - Get a specific hero with their powers

### Powers

- **GET /powers** - Get all powers
- **GET /powers/:id** - Get a specific power
- **PATCH /powers/:id** - Update a power's description

### Hero Powers

- **POST /hero_powers** - Create a new hero-power association

### Email

- **POST /send-email** - Send a test email

## Data Models

### Hero
- `id`: Primary key
- `name`: Hero's real name
- `super_name`: Hero's superhero name

### Power
- `id`: Primary key
- `name`: Power name
- `description`: Detailed description (min 20 characters)

### HeroPower
- `id`: Primary key
- `strength`: Power strength ('Strong', 'Weak', 'Average')
- `hero_id`: Foreign key to Hero
- `power_id`: Foreign key to Power

## Validation Rules

- **Power description**: Must be present and at least 20 characters long
- **HeroPower strength**: Must be one of 'Strong', 'Weak', or 'Average'

## Testing

You can test the API using the provided Postman collection:
1. Import `challenge-2-superheroes.postman_collection.json` into Postman
2. Run the collection to test all endpoints

## Email Configuration

To enable email functionality:
1. Use a Gmail account with 2-factor authentication enabled
2. Generate an App Password for your Gmail account
3. Set the following environment variables:
   - `MAIL_USERNAME`: Your Gmail address
   - `MAIL_PASSWORD`: Your Gmail App Password

## Deployment

For production deployment:
1. Set `DATABASE_URL` to your production database
2. Configure proper email credentials
3. Set a secure `SECRET_KEY`
4. Use a production WSGI server like Gunicorn

## Support

For support or questions, please contact:
- Email: kenneth.kipkosgei@example.com
- GitHub: [Kenneth Kipkosgei](https://github.com/Kenneth-kipkosgei)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Acknowledgments

- Built as part of Moringa School Phase 4 curriculum
- Thanks to the Flask and SQLAlchemy communities for excellent documentation