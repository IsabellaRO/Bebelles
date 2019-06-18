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
        self.lexer.add('ASSIGN', r'\=')
        self.lexer.add('BREAKLINE', r'\\n')
        self.lexer.add('END', r'end')
        self.lexer.add('IF', r'if')

        # Number
        self.lexer.add('INT', r'\d+')
        self.lexer.add('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()