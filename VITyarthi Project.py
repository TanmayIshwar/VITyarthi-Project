import matplotlib.pyplot as plt
import csv
import datetime

f='expenses.csv'
#Fucntion to open csv file
def load_expenses():
    expenses=[]
    try:
        with open(f,newline='') as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                row['amount']=float(row['amount'])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses
#Function save input data to the csv file 
def save_expenses(expenses):
    with open(f,'w',newline='') as csvfile:
        fieldnames=['date','amount','category','note']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
#Function to input expense data
def add_expense(expenses):
    date=input('Enter date(YYYY-MM-DD) OR Leave blank for today: ')
    if not date:
        date=datetime.date.today().isoformat()
    amount=float(input('Enter amount: '))
    category=input('Enter Category: ')
    note=input('Enter note: ')
    expense={'Date':date,'Amount':amount,'Category':category,'Note':note}
    expenses.append(expense)
    print('Expense added')
#Function to view the stored data from the csv file
def view_expenses(expenses):
    if not expenses:
        print('No expenses recorded')
        return
    print(f"{'Date':,12}{'Amount':<10}{'Category':<15}{'Note'}")
    print('-'*50)
    for exp in expenses:
        print(f"{exp['Date']:<12}{exp['Amount']:<10.2f}{exp['Category']:<15}{exp['Note']}")

#Function to plot and visualize expenses categorically 
def plot_expenses(expenses):
    if not expenses:
        print('No expenses to plot')
        return
    category_totals={}
    for exp in expenses:
        category=exp['Category']
        category_totals['Category']=category_totals.get(category,0)+exp['Amount']
    categories=list(category_totals.keys())
    amounts=list(category_totals.values())
    plt.figure(figsize=(8,6))
    plt.bar(categories,amounts,color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Expenses by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
#Command Line Main menu 
def menu():
    expenses=load_expenses()
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
if __name__=='__main__':
    menu()
        
    


