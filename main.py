from lexer import Lexer
from parser import Parser

text_input = """
a = 7
print(a)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()