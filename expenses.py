import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Description", "Category", "Amount"])

def add_expense():
    """Add a new expense entry."""
    print("\n--- Add Expense ---")
    desc = input("Enter description: ").strip()
    if not desc:
        print("Description cannot be empty.")
        return

    print("Categories: Food, Transport, Shopping, Bills, Entertainment, Other")
    category = input("Enter category (or press Enter for 'Other'): ").strip().capitalize()
    if category not in ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]:
        category = "Other"

    try:
        amount = float(input("Enter amount (₹): "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, desc, category, f"{amount:.2f}"])

    print(f"✅ Expense '{desc}' of ₹{amount:.2f} added successfully!")

def view_expenses():
    """Display all saved expenses in a formatted table."""
    print("\n--- All Expenses ---")
    try:
        with open(FILENAME, "r") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("No expenses recorded yet.")
                return

            # Print header
            print(f"{'No.':<5} {'Date':<18} {'Description':<20} {'Category':<15} {'Amount':>10}")
            print("-" * 72)

            for i, row in enumerate(reader[1:], start=1):
                print(f"{i:<5} {row[0]:<18} {row[1]:<20} {row[2]:<15} ₹{float(row[3]):>9.2f}")

    except FileNotFoundError:
        print("No expenses file found.")

def view_total():
    """Calculate and display the total amount spent."""
    print("\n--- Total Expenses ---")
    try:
        total = 0.0
        category_totals = {}

        with open(FILENAME, "r") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("No expenses recorded yet.")
                return

            for row in reader[1:]:
                amount = float(row[3])
                total += amount
                cat = row[2]
                category_totals[cat] = category_totals.get(cat, 0) + amount

        print(f"\n{'Category':<20} {'Amount':>12}")
        print("-" * 34)
        for cat, amt in sorted(category_totals.items()):
            print(f"{cat:<20} ₹{amt:>10.2f}")
        print("-" * 34)
        print(f"{'TOTAL':<20} ₹{total:>10.2f}")

    except FileNotFoundError:
        print("No expenses file found.")

def delete_expense():
    """Delete a specific expense by its number."""
    view_expenses()
    try:
        with open(FILENAME, "r") as f:
            rows = list(csv.reader(f))

        if len(rows) <= 1:
            return

        num = int(input("\nEnter expense number to delete (0 to cancel): "))
        if num == 0:
            return
        if num < 1 or num >= len(rows):
            print("Invalid number.")
            return

        deleted = rows.pop(num)
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print(f"✅ Deleted: {deleted[1]} - ₹{float(deleted[3]):.2f}")

    except (ValueError, FileNotFoundError):
        print("Invalid input or file not found.")

def clear_all():
    """Clear all expense records after confirmation."""
    confirm = input("\n⚠️  Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    if confirm == "yes":
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Description", "Category", "Amount"])
        print("✅ All expenses cleared.")
    else:
        print("Cancelled.")

def main():
    initialize_file()
    print("=" * 40)
    print("   💰 Python Expense Tracker CLI")
    print("=" * 40)

    while True:
        print("\n📋 MENU")
        print("  1. Add Expense")
        print("  2. View All Expenses")
        print("  3. View Total Spent")
        print("  4. Delete an Expense")
        print("  5. Clear All Expenses")
        print("  6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            clear_all()
        elif choice == "6":
            print("\n👋 Goodbye! Stay on budget!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
