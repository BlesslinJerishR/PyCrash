# 11.3
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employees = [Employee('Blesslin', 'Jerish', 300),
                          Employee('Blesslin', 'Jerish', 6500)]
    """Test for salary raise"""
    def test_default_raise(self):
        employee = self.employees[0]
        self.assertEqual(300, employee.salary)

    def test_custom_raise(self):
        employee = self.employees[1]
        self.assertEqual(6500, employee.salary)


if __name__ == '__main__':
    unittest.main()