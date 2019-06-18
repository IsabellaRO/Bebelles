from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Mult, Div, Assign, Ident, GreaterThan, LessThan, Equal


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['INT', 'PRINT', 'OPENPAR', 'CLOSEPAR', 'PLUS', 'MINUS', 'MULT', 'DIV', 'ASSIGN', 'BREAKLINE', 'IDENT', 'IF', 'END', 'ELSE', 'GREATERTHAN', 'LESSTHAN', 'COMMA', 'COLON' ,'AND', 'OR', 'NOT', 'DEF', 'VOID', 'INTEGER', 'BOOLEAN', 'TRUE', 'FALSE', 'WHILE', 'WEND', 'INPUT', 'AS', 'CALL', 'EQUAL']
        )

    def parse(self):
        @self.pg.production('program : expression')
        def program(p):
            return 
        @self.pg.production('program : expression PRINT OPENPAR expression CLOSEPAR')
        def program(p):
            return Print(p[3])
        @self.pg.production('program : PRINT OPENPAR expression CLOSEPAR')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression PLUS expression')
        @self.pg.production('expression : expression MINUS expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression ASSIGN expression')
        @self.pg.production('expression : expression GREATERTHAN expression')
        @self.pg.production('expression : expression LESSTHAN expression')
        @self.pg.production('expression : expression EQUAL expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'PLUS':
                return Sum(left, right)
            elif operator.gettokentype() == 'MINUS':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            elif operator.gettokentype() == 'ASSIGN':
                return Assign(left, right)
            elif operator.gettokentype() == 'GREATERTHAN':
                return GreaterThan(left, right)
            elif operator.gettokentype() == 'LESSTHAN':
                return LessThan(left, right)
            elif operator.gettokentype() == 'EQUAL':
                return Equal(left, right)

            

        @self.pg.production('expression : INT')
        def number(p):
            return Number(p[0].value)
        

        @self.pg.production('expression : IDENT')
        def ident(p):
            return Ident(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()