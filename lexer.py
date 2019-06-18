# Para a implementação dessa linguagem foram utilizados os tutoriais abaixo:
# https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
# https://www.dabeaz.com/ply/PLYTalk.pdf

from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPENPAR', r'\(')
        self.lexer.add('CLOSEPAR', r'\)')
        # Operators
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('EQUAL', r'\==')
        self.lexer.add('ASSIGN', r'\=')
        self.lexer.add('BREAKLINE', r'\\n')
        self.lexer.add('END', r'end')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('GREATERTHAN', r'\>')
        self.lexer.add('LESSTHAN', r'\<')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('COLON', r'\:')
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')
        self.lexer.add('NOT', r'not')
        self.lexer.add('DEF', r'def')
        self.lexer.add('VOID', r'void')
        self.lexer.add('INTEGER', r'integer')
        self.lexer.add('BOOLEAN', r'boolean')
        self.lexer.add('TRUE', r'true')
        self.lexer.add('FALSE', r'false')
        self.lexer.add('WHILE', r'while')
        self.lexer.add('WEND', r'wend')
        self.lexer.add('INPUT', r'input')
        self.lexer.add('AS', r'as')
        self.lexer.add('CALL', r'call')
        

        # Number
        self.lexer.add('INT', r'\d+')
        self.lexer.add('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()