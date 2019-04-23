
import unittest
from python_solution_10 import square

class SolutionTest(unittest.TestCase):

  def test_square_of_incorrect_data_type_failed(self):  
    self.assertFalse(square('a',5))
    print('Incorrect_data_type_failed - passed')

  def test_square_of_positive_data_type_successfull(self):
    self.assertTrue(square(8.8,3))
    print('Positive_data_type - passed')

  def test_square_of_positive_int_numbers_successfull(self):
    self.assertEqual(square(2,5),10)
    print('Positive integer numbers - passed')

  def test_square_of_positive_float_numbers_successfull(self):
    self.assertEqual(square(1.6,6.8),10.88)
    print('Positive float numbers - passed')


  def test_initial_conditions_checking_negative_number_failed(self):
    self.assertFalse(square(-4,5))
    print('Checking_negative_number_failed - passed')

  def test_initial_conditions_0_number_failed(self):
    self.assertFalse(square(8,0))
    print('Initial_conditions_0_number_failed - passed')

if __name__ == '__main__':
    unittest.main()


