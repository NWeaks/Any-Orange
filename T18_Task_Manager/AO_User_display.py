
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Retrieve checkout count from localStorage or set it to 0 if not present
checkoutCount = 0

# Ensure checkout count is updated when the page loads
@app.before_first_request
def before_first_request():
    global checkoutCount
    checkoutCount = 0

# Add item to checkout
@app.route('/add_to_checkout', methods=['POST'])
def add_to_checkout():
    global checkoutCount
    data = request.get_json()
    name = data['name']
    value = data['value']

    checkoutCount += 1

    # Store updated checkout count in localStorage
    # (for a more persistent solution, consider using databases)
    # localStorage.setItem("checkoutCount", checkoutCount)

    # Retrieve existing checkout items from localStorage
    # let checkoutItems = JSON.parse(localStorage.getItem("checkoutItems")) || [];
    # Add the selected item to checkoutItems array
    # checkoutItems.push({ name: name, value: value });
    # Store the updated checkout items back to localStorage
    # localStorage.setItem("checkoutItems", JSON.stringify(checkoutItems));

    return jsonify({'checkoutCount': checkoutCount})

# Home route
@app.route('/')
def home():
    return render_template('AO_User_display.html')

if __name__ == '__main__':
    app.run(debug=True)
