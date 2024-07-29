from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    user_expenses = db.relationship('UserExpense', back_populates='user', cascade='all, delete-orphan')

class Expense(db.Model):
    # __tablename__ = 'expense'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    total = db.Column(db.Float, nullable=False)
    mode = db.Column(db.String(50), nullable=False)
    user_expenses = db.relationship('UserExpense', back_populates='expense', cascade='all, delete-orphan')

class UserExpense(db.Model):
    # __tablename__ = 'user_expense'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id'), primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user = db.relationship('User', back_populates='user_expenses')
    expense = db.relationship('Expense', back_populates='user_expenses')
