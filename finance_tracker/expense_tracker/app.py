from flask import Flask, render_template, request, redirect
import sqlite3
from collections import defaultdict
from db import init_db
from models import add_transaction, get_all_transactions, get_summary

app = Flask(__name__)
init_db()


@app.route("/")
def index():
    conn = sqlite3.connect("data/budget.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions ORDER BY date DESC")
    transactions = cur.fetchall()

    # Chart data logic
    income_by_category = defaultdict(float)
    expense_by_category = defaultdict(float)

    for t in transactions:
        if t[5] == "income":
            income_by_category[t[3]] += t[2]
        elif t[5] == "expense":
            expense_by_category[t[3]] += t[2]

    chart_labels = list(
        set(income_by_category.keys()) | set(expense_by_category.keys())
    )
    income_data = [income_by_category[label] for label in chart_labels]
    expense_data = [expense_by_category[label] for label in chart_labels]

    return render_template(
        "index.html",
        transactions=transactions,
        chart_labels=chart_labels,
        income_data=income_data,
        expense_data=expense_data,
    )


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'date': request.form['date'],
            'amount': float(request.form['amount']),
            'category': request.form['category'],
            'note': request.form['note'],
            'type': request.form['type']
        }
        add_transaction(data)
        return redirect('/')
    return render_template('add.html')

@app.route('/summary')
def summary():
    data = get_summary()
    return render_template('summary.html', summary=data)

if __name__ == '__main__':
    app.run(debug=True)
