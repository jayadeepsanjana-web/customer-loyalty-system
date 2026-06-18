# Customer Loyalty Points System

## Overview

A simple Customer Loyalty Points System built using Flask and SQLite. The application allows users to add customers, record purchases, calculate loyalty points, apply bonus points, and view customer summaries along with transaction history.

## Features

* Add customers
* Record purchases
* Calculate loyalty points
* Award bonus points for purchases above ₹5000
* Store data using SQLite
* View customer summary
* View transaction history
* Basic input validation

## Technology Stack

* Python
* Flask
* SQLite
* SQLAlchemy
* HTML
* CSS

## Points Calculation

* 1 point for every ₹100 spent
* Additional 50 bonus points for purchases above ₹5000

Example:

* Purchase Amount: ₹6000
* Base Points: 60
* Bonus Points: 50
* Total Points: 110

## Setup Instructions

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open:

```text
http://127.0.0.1:5000
```

## Assumptions

* Each customer has a unique email address.
* Spend amounts must be greater than zero.
* Bonus points are awarded only for purchases above ₹5000.

## AI-Assisted Development

AI-assisted development tools were used during the project to support implementation, debugging, and validation of the application. These tools were primarily used to explore approaches, troubleshoot issues, and improve development efficiency.
The application was developed through iterative coding, testing, and refinement, with manual verification of functionality, points calculations, database operations, and validation logic.

## Challenges Encountered

One challenge during development was extending the application to support transaction history while ensuring customer point totals remained accurate. Additional testing was required to verify that points, bonus points, and transaction records were stored correctly in the SQLite database and remained synchronized after each purchase.

Input validation was another area of focus, particularly handling duplicate customer emails, invalid purchase amounts, and missing data without causing application errors.

## Future Improvements

- Customer search and filtering
- Edit and delete customer records
- Dashboard analytics and reporting
- Authentication and user management
- Configurable loyalty point rules
- Export transaction history to CSV or Excel

