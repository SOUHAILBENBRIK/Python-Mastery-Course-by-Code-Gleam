from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'expenses.json'

# Helper function to load and save data
def load_data():
    file_path = "expenses.json"
    
    # Check if the file exists and is not empty
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        print(f"Warning: '{file_path}' is either missing or empty. Returning an empty list.")
        return []

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON content in '{file_path}'. Returning an empty list.")
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Home Page - Display All Expenses
@app.route('/')
def index():
    expenses = load_data()
    total = sum(expense['amount'] for expense in expenses)
    return render_template('index.html', expenses=expenses, total=total)

# Add a New Expense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        expense_name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        
        # Create a new expense entry
        new_expense = {
            'name': expense_name,
            'amount': amount,
            'category': category,
            'date': date
        }
        
        # Save the new expense
        expenses = load_data()
        expenses.append(new_expense)
        save_data(expenses)
        
        return redirect(url_for('index'))

    return render_template('add_expense.html')

# Edit an Existing Expense
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_expense(index):
    expenses = load_data()
    if index < 0 or index >= len(expenses):
        return "Invalid expense index!", 404
    
    if request.method == 'POST':
        expenses[index]['name'] = request.form['name']
        expenses[index]['amount'] = float(request.form['amount'])
        expenses[index]['category'] = request.form['category']
        expenses[index]['date'] = request.form['date']
        
        save_data(expenses)
        return redirect(url_for('index'))

    return render_template('edit_expense.html', expense=expenses[index], index=index)

# Delete an Expense
@app.route('/delete/<int:index>', methods=['POST'])
def delete_expense(index):
    expenses = load_data()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_data(expenses)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
