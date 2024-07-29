import pandas as pd
from io import BytesIO
from flask import Flask, render_template, request, redirect, url_for, send_file
from models import db, User, Expense, UserExpense  # Corrected import

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            address=request.form['address']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user'))
    users = User.query.all()
    return render_template('user.html', users=users)

@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.phone = request.form['phone']
        user.address = request.form['address']
        db.session.commit()
        return redirect(url_for('user'))
    return render_template('edit_user.html', user=user)

@app.route('/user/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user'))

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        description = request.form['description']
        total = float(request.form['total'])
        mode = request.form['mode']
        selected_users = request.form.getlist('users')
        new_expense = Expense(description=description, total=total, mode=mode)
        db.session.add(new_expense)
        db.session.commit()

        if mode == 'equal':
            amount_per_user = total / len(selected_users)
            for user_id in selected_users:
                user_expense = UserExpense(user_id=user_id, expense_id=new_expense.id, amount=amount_per_user)
                db.session.add(user_expense)

        elif mode == 'exact':
            for user_id in selected_users:
                amount = float(request.form.get(f'amounts[{user_id}]', 0))
                user_expense = UserExpense(user_id=user_id, expense_id=new_expense.id, amount=amount)
                db.session.add(user_expense)

        elif mode == 'percentage':
            total_percentage = sum(float(request.form.get(f'amounts[{user_id}]', 0)) for user_id in selected_users)
            if total_percentage != 100:
                # Handle error: total percentage should be 100
                pass
            for user_id in selected_users:
                percentage = float(request.form.get(f'amounts[{user_id}]', 0))
                amount = (percentage / 100) * total
                user_expense = UserExpense(user_id=user_id, expense_id=new_expense.id, amount=amount)
                db.session.add(user_expense)

        db.session.commit()
        return redirect(url_for('expenses'))

    users = User.query.all()
    expenses = Expense.query.all()
    return render_template('expenses.html', users=users, expenses=expenses)

@app.route('/expenses/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('expenses'))

@app.route('/balance_sheet')
def balance_sheet():
    users = User.query.all()
    expenses = Expense.query.all()
    return render_template('balance_sheet.html', users=users, expenses=expenses)

@app.route('/download_balance_sheet')
def download_balance_sheet():
    users = User.query.all()
    expenses = Expense.query.all()

    # Create dataframes
    user_data = []
    for user in users:
        total_expense = sum(ue.amount for ue in user.user_expenses)
        user_data.append([user.id, user.name, total_expense])

    user_df = pd.DataFrame(user_data, columns=['User ID', 'User Name', 'Total Expenses'])

    expense_data = []
    for expense in expenses:
        for ue in expense.user_expenses:
            expense_data.append([expense.id, expense.description, expense.total, ue.user.name, ue.amount])

    expense_df = pd.DataFrame(expense_data, columns=['Expense ID', 'Description', 'Total Amount', 'User Name', 'User Amount'])

    # Create an Excel file
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        user_df.to_excel(writer, sheet_name='Users', index=False)
        expense_df.to_excel(writer, sheet_name='Expenses', index=False)

    output.seek(0)
    return send_file(output, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', attachment_filename='balance_sheet.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
