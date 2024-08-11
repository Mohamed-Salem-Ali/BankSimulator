
```markdown
# BankSimulator

## Overview
**BankSimulator** is a simple Python-based simulation of banking operations using SQLite as a database. The project can manage users and their card transactions by reading from JSON files and updating the database accordingly. It includes options for continuous or one-time updates to the database.

## Features
- **User Management**: Add or update user data in the database from JSON files.
- **Transaction Management**: Add or update card transactions in the database from JSON files.
- **Database Operations**: Choose between continuous or single-time database updates.

## Requirements
- Python 3.x
- SQLite3
- Faker (`pip install faker`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd BankSimulator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Initialize the Database**: Create the necessary tables in the SQLite database by running:
   ```python
   python BankSimulator.py
   ```
2. **Run the Program**:
   - Follow the on-screen prompts to choose whether you want to update users, transactions, or both. You can choose between continuous updates or a one-time update.

## Code Structure
- **Database Operations**:
  - `addToUsers(users_data, db, cr)`: Adds or updates user data in the `USERS` table.
  - `addToCard(card_data, db, cr)`: Adds or updates transaction data in the `CARDS` table.
  - `createNewDataBase()`: Initializes the database and creates the necessary tables.

- **Data Update Functions**:
  - `updateUsersDataOnce()` and `updateUsersDataCont()`: Update user data once or continuously.
  - `updateCardDataOnce()` and `updateCardDataCont()`: Update transaction data once or continuously.
  - `updateDataBaseOnce()` and `updateDataBaseCont()`: Update both users and transactions once or continuously.

- **Main Function**:
  - `main()`: The entry point of the program, providing the user with options to interact with the database.

## JSON File Structure
The JSON files should be structured as follows:

- **User Data (`users.json`)**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "age": 30,
      "address": "1234 Main St"
    },
    ...
  ]
  ```

- **Transaction Data (`card.json`)**:
  ```json
  [
    {
      "transactionId": 1001,
      "amount": 500,
      "userId": 1
    },
    ...
  ]
  ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```