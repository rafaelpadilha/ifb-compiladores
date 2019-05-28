from lexer_a import Lexer
from parser2 import Parser

text_input = """
proc main()
{
    var tmp, flg, dir, flg2 - int;
    var tm2 - float;
    prnt("OLA WORLD");
}
"""


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)


#for token in tokens:
#    print(token)
    
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

