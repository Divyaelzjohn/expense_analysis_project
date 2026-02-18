import mysql.connector
import pandas as pd
from db_connection import get_connection


def add_expense():
    conn = get_connection()
    cursor = conn.cursor()

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    query = """
    INSERT INTO expenses (date, category, amount, description)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (date, category, amount, description))
    conn.commit()

    print("Expense added successfully!\n")

    cursor.close()
    conn.close()


def view_analysis():
    conn = get_connection()

    query = "SELECT * FROM expenses"
    df = pd.read_sql(query, conn)

    if df.empty:
        print("No expenses found.\n")
        return

    print("\n----- Expense Data -----")
    print(df)

    print("\nTotal Expense:", df["amount"].sum())

    print("\nCategory Wise:")
    print(df.groupby("category")["amount"].sum())

    print("\nMonthly:")
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    print(df.groupby("month")["amount"].sum())

    print()

    conn.close()


def main():
    while True:
        print("1. Add Expense")
        print("2. View Analysis")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_analysis()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()