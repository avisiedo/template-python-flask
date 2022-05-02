from unittest import TestCase
from app import create_app


class TestHello(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    # def test_hello_default(self):
    #     """
    #     Tests the route screen message
    #     """
    #     rv = self.app.get('/api/hello')

    #     # If we recalculate the hash on the block we should get the same result as we have stored
    #     self.assertEqual({"message": 'Hello World!'}, rv.get_json())

    def test_hello(self):
        """
        Tests the route screen message
        """
        rv = self.app.get('/api/hello/people')

        # If we recalculate the hash on the block we should get the same result as we have stored
        self.assertEqual({"message": 'Hello people!'}, rv.get_json())
