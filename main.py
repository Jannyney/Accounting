import tkinter as tk
import sqlite3

connection = sqlite3.connect("account.db")
cur = connection.cursor()

root = tk.Tk()

Balance = tk.StringVar()

def get_balance():
    cur.execute("Select SUM(Income) from Account")
    Income = cur.fetchall()
    cur.execute("Select SUM(Expense) from Account")
    Expense = cur.fetchall()
    return Income[0][0]-Expense[0][0]

def add_income(Lists, Amounts):
    cur.execute("INSERT INTO Account values(?,?,?)", (Lists, int(Amounts), 0))
    connection.commit()
    Balance.set(get_balance())
    list_things.delete(0, 'end')
    amount.delete(0, 'end')

def add_expense(Lists, Amounts):
    cur.execute("INSERT INTO Account values(?,?,?)", (Lists, 0, int(Amounts)))
    connection.commit()
    Balance.set(get_balance())
    list_things.delete(0, 'end')
    amount.delete(0, 'end')

def clear_table():
    cur.execute("DELETE FROM Account")
    connection.commit()
    list_things.delete(0, 'end')
    amount.delete(0, 'end')
    Balance.set("")





Lists = tk.StringVar() #For displaying
Amount = tk.StringVar()

canvas = tk.Canvas(root, height = 300, width = 300)
canvas.pack()

frame = tk.Frame(root, bg = 'light blue')
frame.place(relwidth = 1, relheight = 1)

accounting = tk.Label(frame, text = "Accounting").grid(column = 2, row = 0)

list_things_label = tk.Label(frame, text ="List").grid(column=1, row = 1)
list_things = tk.Entry(frame)
list_things.grid(column=1, row= 2)

amount_label = tk.Label(frame, text ="Amount").grid(column=3, row = 1)
amount = tk.Entry(frame)
amount.grid(column=3, row= 2)


add_income_button = tk.Button(frame, text = "Income", command = lambda:add_income(list_things.get(), amount.get())).grid(column=1, row = 5)
add_expense_button = tk.Button(frame, text = "Expense", command = lambda:add_expense(list_things.get(), amount.get())).grid(column=3, row = 5)
clear_button = tk.Button(frame, text = "Clear All",command = lambda:clear_table()).grid(column=2, row = 10)

balance = tk.Label(frame, textvar =Balance).grid(column=2, row = 6)

table = tk.Label(frame).grid(column=2, row =7)


root.mainloop()