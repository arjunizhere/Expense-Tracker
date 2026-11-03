import csv
from datetime import date

'''Adding an expense'''
def add_expense():
    today = date.today()
    category=input("Enter the category of expense: ")
    amount=float(input("Enter the amount of expense: "))
    description=input("Enter the description of expense: ")
    with open('expenses.csv','r') as file:
        reader=csv.reader(file)
        rows=list(reader)
        if len(rows)==0:
            id=1
        else:
            id=len(rows)

    with open('expenses.csv','a', newline='') as file:
        writer=csv.writer(file)
        writer.writerow([id,today, category, amount, description])
        print("Expense added successfully!")

'''Displaying all expenses'''
def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses found!")
        return

    print("\n" + "=" * 75)
    print("                      EXPENSE TRACKER")
    print("=" * 75)

    print(f"{'ID':<5} {'Date':<15} {'Description':<20} {'Amount':<12} {'Category':<15}")

    print("-" * 75)

    for row in rows[1:]:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<20} {row[3]:<12} {row[4]:<15}")

    print("=" * 75)

'''Calculating total expenses'''
def total_expenses():
    total=0
    with open('expenses.csv','r') as file:
        reader=csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            total+=float(row[3])
    print(f"Total expenses: {total}")

'''Deleting an expense'''
def delete_expense():
    with open('expenses.csv','r') as file:
        reader=csv.reader(file)
        rows=list(reader)
        if len(rows)<=1:
            print("No expenses to delete.")
            return
        view_expenses()
        id=int(input("Enter the ID of the expense to delete: "))
        found=False
        for row in rows:
            if row[0]==str(id):
                rows.remove(row)
                found=True
                break
        if found==True:
            for i in range(1,len(rows)):
                rows[i][0]=str(i)
            with open('expenses.csv','w', newline='') as file:
                writer=csv.writer(file)
                writer.writerows(rows)
            print("Expense deleted successfully!")
        else:
            print("Expense with the given ID not found.")

'''Editing an expense'''
def edit_expense():
    view_expenses()
    id=int(input("Enter the ID of the expense to edit: "))
    with open('expenses.csv','r') as file:
        reader=csv.reader(file)
        rows=list(reader)
        found=False
        for row in rows:
            if row[0]==str(id):
                found=True
                print("1. Edit Date")
                print("2. Edit Category")
                print("3. Edit Amount")
                print("4. Edit Description")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    new_date=input("Enter the new date (YYYY-MM-DD): ")
                    row[1]=new_date
                elif choice==2:
                    new_category=input("Enter the new category: ")
                    row[2]=new_category
                elif choice==3:
                    new_amount=float(input("Enter the new amount: "))
                    row[3]=new_amount
                elif choice==4:
                    new_description=input("Enter the new description: ")
                    row[4]=new_description
                else:
                    print("Invalid choice.")
    if found==True:
        with open('expenses.csv','w', newline='') as file:
            writer=csv.writer(file)
            writer.writerows(rows)
        print("Expense edited successfully!")
    else:
        print("Expense with the given ID not found.")

''' Main function'''
def main():
    while True:
        print("\n" + "=" * 75)
        print("                      EXPENSE TRACKER MENU")
        print("=" * 75)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Delete Expense")
        print("5. Edit Expense")
        print("6. Exit")
        print("-" * 75)

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            edit_expense()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()