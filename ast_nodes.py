
class ASTNode:
    """What do all the nodes need ? 1. __str__ function 2. value 3. children 4.base methods ?"""
    def __init__(self) -> None:
        pass # but what should come in the base class ? 
    

class Number(ASTNode):
    
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
    
    def __str__(self) -> str:
        return f"Number({self.value})"

class Variable(ASTNode):
    
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
    
    def __str__(self) -> str:
        return f"Variable({self.value})"

class BinaryOp(ASTNode):
    def __init__(self, operator, left, right) -> None:
        super().__init__()
        self.operator = operator
        self.left = left
        self.right = right
        
    def __str__(self) -> str:
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"