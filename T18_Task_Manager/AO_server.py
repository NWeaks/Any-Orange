
# Import necessary modules
from flask import Flask, request, jsonify
from AO_Database import AO_Database

# Initialize Flask application
app = Flask(__name__)
db = AO_Database()

# Define route to handle adding orders
@app.route('/add_order', methods=['POST'])
def add_order():
    order_details = request.json
    db.update_order_history(order_details)
    db.update_stock_from_order(order_details)  # Update stock from order
    return jsonify({"message": "Order details added successfully"}), 200

# Add a route to fetch stock data
@app.route('/get_stock', methods=['GET'])
def get_stock():
    stock = db.available_stock.get_stock()
    return jsonify(stock), 200

# Route to confirm purchase and deduct items from stock
@app.route('/confirm_purchase', methods=['POST'])
def confirm_purchase():
    order_details = request.json
    db.update_stock_from_order(order_details)  # Assuming you have a method to update stock from order in your database module
    return jsonify({"message": "Purchase confirmed and items deducted from stock."}), 200

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
