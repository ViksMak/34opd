import unittest
import main


class TestMortgageCalculator(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_calculate(self):
        response = self.app.post('/calculate', data=dict(loan_amount=100000, interest_rate=5, loan_term=30))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ежемесячный платеж:', response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
