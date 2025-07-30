from lexer import Lexer
from ast_nodes import *

class Parser:
    
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.position = 0
        
    def parse(self):
        """
        Here, we'll be parsing tokens and converting them to ASTs. For now we'll build for Binary exp only.
        """
        if len(self.tokens) == 3:
            left_token = self.tokens[0]    
            op_token = self.tokens[1]     
            right_token = self.tokens[2]   

            left_node = Number(left_token.value) if left_token.type == "NUMBER" else Variable(left_token.value)
            right_node = Number(right_token.value) if right_token.type == "NUMBER" else Variable(right_token.value)

            return BinaryOp(op_token.value, left_node, right_node)

lexer = Lexer("42 + 24")
tokens = lexer.tokenize()
parser = Parser(tokens)
ast = parser.parse()
print(ast)  # Should print: BinaryOp(+, Number(42), Number(24))

lexer = Lexer("x + y")
tokens = lexer.tokenize()
parser = Parser(tokens)
ast = parser.parse()
print(ast)  # Should print: BinaryOp(+, Variable(x), Variable(y))
