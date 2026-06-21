# Expense Tracker API

A REST API for tracking personal expenses, built with FastAPI and PostgreSQL. Supports full CRUD operations and basic spending statistics grouped by category.

## Features

- Create, read, update, and delete expenses
- View total spending and a breakdown by category
- Interactive API documentation (Swagger UI) generated automatically

## Tech Stack

- **Python 3.13**
- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **PostgreSQL** — database
- **Pydantic** — data validation

## Getting Started

### Prerequisites
- Python 3.13+
- PostgreSQL installed and running

### Installation

1. Clone the repository
   \`\`\`
   git clone https://github.com/meruyert-backend/expense-tracker-api.git
   cd expense-tracker-api
   \`\`\`

2. Create and activate a virtual environment
   \`\`\`
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

3. Install dependencies
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Create the PostgreSQL database
   \`\`\`
   createdb expense_tracker
   \`\`\`

5. Run the server
   \`\`\`
   uvicorn main:app --reload
   \`\`\`

6. Open the interactive docs at `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /expenses/ | Create a new expense |
| GET | /expenses/ | List all expenses |
| GET | /expenses/{id} | Get a single expense |
| PUT | /expenses/{id} | Update an expense |
| DELETE | /expenses/{id} | Delete an expense |
| GET | /expenses/stats/summary | Get total spending and breakdown by category |

## Author

Meruyert Zhunuskanova — https://github.com/meruyert-backend/