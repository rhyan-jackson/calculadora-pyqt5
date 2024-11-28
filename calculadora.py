from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from settings.config import *

class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(500, 500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # nova variável que permite tratar o valor mostrado como sendo um resultado ou não depois de fazer uma conta:
        # se se pressionar um operador, continua a conta
        # se se pressionar um número, dá clear na tela
        self.result_displayed = False

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            f'* {{'
            f'background: {BACKGROUND_COLOR};'
            f'color: {TEXT_COLOR};'
            f'font-size: {FONT_SIZE};'
            f'font-family: {DISPLAY_FONT};'
            f'}}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.addbutton(QPushButton('7'), 1, 0, 1, 1)
        self.addbutton(QPushButton('8'), 1, 1, 1, 1)
        self.addbutton(QPushButton('9'), 1, 2, 1, 1)
        self.addbutton(QPushButton('+'), 1, 3, 1, 1)
        self.addbutton(
            QPushButton('Clear'), 1, 4, 1, 1, lambda: self.display.setText(''),
            f'background: {CLEAR_BUTTON_COLOR};'
            f'font-weight: {BUTTON_FONT_WEIGHT};'
            'color: white'
        )

        self.addbutton(QPushButton('4'), 2, 0, 1, 1)
        self.addbutton(QPushButton('5'), 2, 1, 1, 1)
        self.addbutton(QPushButton('6'), 2, 2, 1, 1)
        self.addbutton(QPushButton('-'), 2, 3, 1, 1)
        self.addbutton(
            QPushButton('<'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]),
            f'background: {OPERATOR_BUTTON_COLOR};'
            f'font-weight: {BUTTON_FONT_WEIGHT};'
            'color: white;'
        )

        self.addbutton(QPushButton('1'), 3, 0, 1, 1)
        self.addbutton(QPushButton('2'), 3, 1, 1, 1)
        self.addbutton(QPushButton('3'), 3, 2, 1, 1)
        self.addbutton(QPushButton('x'), 3, 3, 1, 1)
        self.addbutton(QPushButton('.'), 3, 4, 1, 1)    # mudança do sitio do divisor decimal

        self.addbutton(QPushButton('('), 4, 0, 1, 1)    #---
        self.addbutton(QPushButton('0'), 4, 1, 1, 1)    # adição de parênteses e 
        self.addbutton(QPushButton(')'), 4, 2, 1, 1)    # da operação de divisão
        self.addbutton(QPushButton('÷'), 4, 3, 1, 1)    #---
        self.addbutton(
            QPushButton('='), 4, 4, 1, 1, self.eval_igual,
            f'background: {BUTTON_COLOR};'
            f'font-weight: {BUTTON_FONT_WEIGHT};'
            'color: white'
        )

        self.setCentralWidget(self.cw)


    def addbutton(self, btn, row, col, rowspan, colspan, funcao = None, style = None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.handle_button_click(btn.text())
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


    # criação da função handle_button_click que permite tratar do input de forma a evitar ao máximo
    # erros, substituindo automaticamente operadores e tratando operações com parênteses
    def handle_button_click(self, text):
        display_text = self.display.text()
        last_char = display_text[-1] if display_text else ''
        second_last_char = display_text[-2] if display_text and len(display_text) > 1 else ''

        # se no ecrã aparecer 'Conta inválida' ou apenas um operador, o ecrã é substituido pela próxima entrada
        if display_text == 'Conta inválida.'or display_text in '+-x÷)':
            self.display.clear()
            self.result_displayed = False
            self.display.setText(text)
            return

        # controla se um número ou um parêntese se encontra ao lado de outro parêntese diferente e adiciona automáticamente um 'x'
        # ex: 3(5) = 3x(5)
        if last_char in '0123456789)' and text == '(':
            self.display.setText(display_text + 'x' + text)
            self.result_displayed = False
            return
        if last_char == ')' and text in '0123456789(':
            self.display.setText(display_text + 'x' + text)
            self.result_displayed = False
            return

        # impede que seja colocado um operador sem ser o '-' ao lado de um parênteses e elimina automaticamente parênteses vazios '()'
        if last_char == '(':
            if text in '+x÷':
                self.display.setText(display_text)
                self.result_displayed = False
                return
            elif text == ')':
                self.display.setText(display_text[:-1])
                self.result_displayed = False
                return
        
        # impede que sejam colocados múltiplos operadores seguidos   
        if last_char in '+-x÷' and text in '+-x÷)':
            # impede que quando a conta do ecrã acaba em '(-', não se aceitam mais entradas de operadores
            if second_last_char == '(':
                self.display.setText(display_text)
                self.result_displayed = False
                return
            self.display.setText(display_text[:-1] + text)
            self.result_displayed = False
            return

        # quando aparece o resultado de uma conta, se depois se pressionar um número o ecrã apaga e aparece o número pressionado.
        # mas se se adicionar um operador, continua com a conta.
        if display_text and (text.isdigit() or text == '.'):
            if self.result_displayed:
                self.display.clear()
                self.result_displayed = False
                self.display.setText(text)
                return
            self.display.setText(display_text + text)
            return

        self.display.setText(display_text + text)
        self.result_displayed = False


    # criação da função close_parentheses que permite fechar os parêntese abertos automaticamente
    # para que a função eval_igual funcione corretamente
    def close_parentheses(self, expression):
        balanced_expression = []
        parentheses_stack = []

        # para impedir erros, se o último elemento do código é um operador, usa-se a propriedade do
        # elemento neutro.
        if expression[-1] in 'x÷(':
            expression += '1'
        elif expression[-1] in '+-':
            expression += '0'

        for char in expression:
            if char == '(':
                parentheses_stack.append('(')
                balanced_expression.append('(')
            elif char == ')':
                if parentheses_stack:
                    parentheses_stack.pop()
                    balanced_expression.append(')')
                else:
                    pass
            else:
                balanced_expression.append(char)

        balanced_expression += [')'] * len(parentheses_stack)
        final_expression = ''.join(balanced_expression)

        # elimina () para que a função eval() funcione corretamente depois
        while '()' in final_expression:
            final_expression = final_expression.replace('()', '')

        return ''.join(final_expression)


    def eval_igual(self):
        self.result_displayed = True

        # caso seja pressionado '=' em que o input não tem digitos, o ecrã mostra 0
        if not any(char.isdigit() for char in self.display.text()):
            self.display.setText('0')
            return
        
        expression = self.close_parentheses(self.display.text())
        
        try:
            expression = expression.replace('x', '*').replace('÷', '/')     # para a função eval() funcionar
            result = str(eval(expression))
            self.display.setText(result)
        except Exception:
            self.display.setText('Conta inválida.')
