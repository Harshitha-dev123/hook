import unittest
#Application code
def add (a,b):
  return a+b
def substract (a,b):
  return a-b
def multiply (a,b):
  return a*b
#Automated test case
clas TestCalculator (unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,20),40)
  def test_substract(self):
    self.assertEqual(substract(20,10),10)
  def test_multiply(self):
    self.assertEqual(multiply(6,4),24)
# Main application
if_name_=="_main_":
  print("Student Calculator Application")
  print("Addition:",add(20,20))
  print("Substraction:",substract(20,10))
  print("Multiplication:",multiply(5,4))

  print("\n Executing Automated Tests...\n")
  unittest.main(argv =['first-arg-is-ignored'] exit =False )
