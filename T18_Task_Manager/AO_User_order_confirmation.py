
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Add order to database
@app.route('/add_order', methods=['POST'])
def add_order():
    # In a real application, you would handle adding the order to the database here
    # This is a placeholder function for demonstration purposes
    return jsonify({'message': 'Order added to database'})

# Home route
@app.route('/')
def order_confirmation():
    return render_template('AO_User_order_confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
