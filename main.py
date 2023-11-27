import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class CalculatorApp(App):
    def build(self):
        self.expression_input = Label(font_size=32, halign='right', text='0', size_hint_y=None, height=50)
        self.result_display = Label(font_size=32, halign='right', text='', size_hint_y=None, height=50)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.expression_input)
        layout.add_widget(self.result_display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', 'C',
            'sin', 'cos', 'tan', 'asin',
            'acos', 'atan', 'sqrt', '^',
            'log', 'fac', 'cmtoin','mtoft','kgtolb'
        ]

        button_grid = GridLayout(cols=4, spacing=10, size_hint_y=None, height=500)

        for button_text in buttons:
            button = Button(text=button_text, on_press=self.on_button_press)
            button_grid.add_widget(button)

        layout.add_widget(button_grid)
        return layout

    def on_button_press(self, instance):
        current_text = self.expression_input.text

        if instance.text == '=':
            try:
                input_text = self.expression_input.text
                input_stream = InputStream(input_text)
                lexer = ExprLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = ExprParser(stream)
                tree = parser.prog()
                res = MyExprVisitor().visitProg(tree)
                self.result_display.text = str(res)
            except Exception as e:
                self.result_display.text = "Error"
        elif instance.text == 'C':
            self.expression_input.text = '0'
            self.result_display.text = ''
        else:
            if current_text == '0' or '=' in current_text:
                self.expression_input.text = instance.text
            else:
                self.expression_input.text += instance.text


def main(argv):
    CalculatorApp().run()


if __name__ == '__main__':
    main(sys.argv)
