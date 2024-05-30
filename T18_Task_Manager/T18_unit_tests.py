
import unittest
from AO_User_display import add_to_checkout
from AO_User_display import checkoutCount
from AO_User_checkout import confirm_purchase
from AO_User_checkout import checkout
from AO_User_order_confirmation import order_confirmation

class AddToCheckoutTest(unittest.TestCase):
    def setUp(self):
        add_to_checkout.testing = True
        self.app = add_to_checkout.test_client()

    def test_add_to_checkout(self):
        # Send a POST request to add an item to the checkout
        response = self.app.post('/add_to_checkout', json={'name': 'item1', 'value': 10})
        data = response.get_json()

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if checkout count has been incremented
        self.assertEqual(data['checkoutCount'], 1)

class InitialCheckoutCountTest(unittest.TestCase):
    def setUp(self):
        checkoutCount.testing = True
        self.app = checkoutCount.test_client()

    def test_initial_checkout_count(self):
        # Send a GET request to the home route
        response = self.app.get('/')

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the initial checkout count is 0
        self.assertEqual(response.json['checkoutCount'], 0)

class ConfirmPurchaseTest(unittest.TestCase):
    def setUp(self):
        confirm_purchase.testing = True
        self.app = confirm_purchase.test_client()

    def test_confirm_purchase(self):
        # Send a POST request to confirm purchase
        response = self.app.post('/confirm_purchase')

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected message
        self.assertEqual(response.json['message'], 'Purchase confirmed')

class RenderCheckoutTest(unittest.TestCase):
    def setUp(self):
        checkout.testing = True
        self.app = checkout.test_client()

    def test_render_checkout(self):
        # Send a GET request to the home route
        response = self.app.get('/')

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected template
        self.assertIn(b'AO_User_checkout.html', response.data)

class OrderConfirmationTest(unittest.TestCase):
    def setUp(self):
        order_confirmation.testing = True
        self.app = order_confirmation.test_client()

    def test_order_confirmation(self):
        # Send a POST request to the order confirmation route
        response = self.app.post('/confirm_purchase')

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
