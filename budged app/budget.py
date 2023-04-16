import sqlite3

# Connect to the database
conn = sqlite3.connect('budget.db')
c = conn.cursor()

# Create the tables
c.execute('''CREATE TABLE IF NOT EXISTS income
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             source TEXT,
             amount REAL,
             date TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             category TEXT,
             amount REAL,
             date TEXT)''')

# Define the functions
def add_income(source, amount, date):
    c.execute('''INSERT INTO income (source, amount, date)
                 VALUES (?, ?, ?)''', (source, amount, date))
    conn.commit()

def add_expense(category, amount, date):
    c.execute('''INSERT INTO expenses (category, amount, date)
                 VALUES (?, ?, ?)''', (category, amount, date))
    conn.commit()

def get_income():
    c.execute('''SELECT * FROM income''')
    return c.fetchall()

def get_expenses():
    c.execute('''SELECT * FROM expenses''')
    return c.fetchall()

# Prompt the user for input
while True:
    choice = input('Select an option (1) Add income (2) Add expense (3) View income (4) View expenses (5) Exit: ')

    if choice == '1':
        source = input('Enter the source of the income: ')
        amount = input('Enter the amount of the income: ')
        date = input('Enter the date of the income (YYYY-MM-DD): ')
        add_income(source, amount, date)

    elif choice == '2':
        category = input('Enter the category of the expense: ')
        amount = input('Enter the amount of the expense: ')
        date = input('Enter the date of the expense (YYYY-MM-DD): ')
        add_expense(category, amount, date)

    elif choice == '3':
        income = get_income()
        for row in income:
            print(row)

    elif choice == '4':
        expenses = get_expenses()
        for row in expenses:
            print(row)

    elif choice == '5':
        break

# Close the connection
conn.close()
