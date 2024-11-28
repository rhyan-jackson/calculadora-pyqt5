import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from PyQt5.QtWidgets import QApplication
from calculadora import Calculadora

app = QApplication([])

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_1(self):
        self.calc.display.setText('2+2')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '4')

    def test_2(self):
        self.calc.display.setText('8x(2+3)')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '40')

    def test_3(self):
        self.calc.display.setText('(2+3x(4-1')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '11')

    def test_4(self):
        self.calc.display.setText('10÷0')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), 'Conta inválida.')

    def test_5(self):
        self.calc.display.setText('8x(')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '8')
        
    def test_6(self):
        self.calc.display.setText('(')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '0')

    def test_7(self):
        self.calc.display.setText('12+(6-')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '18')

    def test_8(self):
        self.calc.display.setText('(45+(8x(-6x((((')
        self.calc.eval_igual()
        self.assertEqual(self.calc.display.text(), '-3')

    def tearDown(self):
        self.calc.close()

if __name__ == "__main__":
    unittest.main()