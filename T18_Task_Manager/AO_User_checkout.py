
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Confirm purchase and deduct items from stock
@app.route('/confirm_purchase', methods=['POST'])
def confirm_purchase():
    # In a real application, you would handle the purchase confirmation and stock deduction here
    # This is a placeholder function for demonstration purposes
    return jsonify({'message': 'Purchase confirmed'})

# Home route
@app.route('/')
def checkout():
    return render_template('AO_User_checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
