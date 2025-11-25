import matplotlib.pyplot as plt
import csv
import datetime
import numpy as np
import os

f = 'expenses.csv'

# Function to load expenses from the CSV file
def load_expenses():
    expenses = []
    try:
        print(f"Attempting to load expenses from {f}...")
        with open(f, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    row['Amount'] = float(row['Amount'])  # Convert 'Amount' to float
                    expenses.append(row)
                except ValueError as e:
                    print(f"Skipping row due to invalid amount value: {row}")
                    continue  # Skip malformed rows
        print(f"Loaded {len(expenses)} expense(s).")
    except FileNotFoundError:
        print(f"File {f} not found. Returning an empty list.")
    return expenses

# Function to save expenses to the CSV file
def save_expenses(expenses):
    print(f"Saving {len(expenses)} expense(s) to {f}...")
    with open(f, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category', 'Note']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()  # Write the header row
        for expense in expenses:
            writer.writerow(expense)
    print("Expenses saved successfully.")

# Function to get valid float input (used for amount)
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to add an expense
def add_expense(expenses):
    date = input('Enter date (YYYY-MM-DD) OR Leave blank for today: ')
    if not date:
        date = datetime.date.today().isoformat()
    amount = get_float_input('Enter amount: ')  # Use the function to get valid float input
    category = input('Enter Category: ')
    note = input('Enter note: ')
    
    expense = {'Date': date, 'Amount': amount, 'Category': category, 'Note': note}
    expenses.append(expense)
    
    print(f"Expense added: {expense}")

# Function to view the stored expenses
def view_expenses(expenses):
    if not expenses:
        print('No expenses recorded')
        return
    print(f"{'Date':<12}{'Amount':<10}{'Category':<15}{'Note'}")
    print('-' * 50)
    for exp in expenses:
        print(f"{exp['Date']:<12}{exp['Amount']:<10.2f}{exp['Category']:<15}{exp['Note']}")

# Function to plot expenses by category
def plot_expenses(expenses):
    if not expenses:
        print('No expenses to plot')
        return
    category_totals = {}
    for exp in expenses:
        category = exp['Category']
        category_totals[category] = category_totals.get(category, 0) + exp['Amount']
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())
    x_pos = np.arange(len(categories))

    plt.figure(figsize=(8, 6))
    plt.bar(x_pos, amounts, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Expenses by Category')
    plt.xticks(x_pos, categories, rotation=45)
    plt.tight_layout()
    plt.show()

# Main menu function
def menu():
    expenses = load_expenses()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Plot Expenses")
        print("4. Save and Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            plot_expenses(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    menu()
        
    






