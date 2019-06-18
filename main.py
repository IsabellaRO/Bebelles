from lexer import Lexer
from parser import Parser

text_input = """
a = 5
print(3==5)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()