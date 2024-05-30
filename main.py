from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('mortgage_calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    loan_amount = float(request.form['loan_amount'])
    interest_rate = float(request.form['interest_rate']) / 100
    loan_term = int(request.form['loan_term'])

    if loan_amount <= 0 or interest_rate <= 0 or loan_term <= 0:
        return 'Значения должны быть больше нуля'

    monthly_interest_rate = interest_rate / 12
    total_payments = loan_term * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)

    return f'Ежемесячный платеж: {round(monthly_payment, 2)}'


if __name__ == '__main__':
    app.run(debug=True)

