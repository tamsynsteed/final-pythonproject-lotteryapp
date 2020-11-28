import unittest
class Agetest(unittest.TestCase):
    def testscenario(self):
        myage=int(input("Input enter age"))
        message="False"
        self.assertIn(myage, range(1, 100), message)
