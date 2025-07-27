class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value
        
    def __str__(self) -> str:
        return f"Token({self.type}, {self.value})"
    

class Lexer:
    """
    THe lexer class is what takes in a source code string and converts it into Token lists. 
    A lexer needs : 
    1. Constructor - takes the source code string 
    2. current position - track where you are in the string
    3. tokenize() method - returns the list of tokens.
    """
    def __init__(self, source_code) -> None:
        self.source = source_code
        self.position = 0
        
    def tokenize_I(self):
        """
        tokenize function basically outputs source code as tokens - of the class Token class - Token(type, value)
        """
        tokens = []
        for char in self.source:
            if isinstance(char, int):
                tokens.append(Token("NUMBER", char))
                
    def tokenize_II(self):
        """
        In the above one , One mistake we did was the source code itself is a string. THere is no point in then checking instance on it. Better to use isalpha or isdigit functions , built in ones in python hmmm. 
        Also, we need to use position apparantly, to manually control the iteration, instead of using for char in self.source. This is because we need to consume consecutive characters of the same type. Hmm I get why, let's implement. 
        """
        tokens = []
        KEYWORDS = ["if", "else", "while", "for", "def", "return", "true", "false"]
        OPERATORS = ["!", "=", "<", ">"]
        while self.position < len(self.source):
            char = self.source[self.position]
            
            if char.isdigit():
                temp = self.position + 1
                while  temp < len(self.source) and self.source[temp].isdigit():
                    temp +=1
                tokens.append(Token("NUMBER", self.source[self.position:temp]))
                self.position = temp
            
            elif char.isalpha():
                temp = self.position + 1
                while temp < len(self.source) and self.source[temp].isalpha():
                    temp +=1
                if self.source[self.position:temp] in KEYWORDS:
                    tokens.append(Token("KEYWORD", self.source[self.position:temp]))
                else:
                    tokens.append(Token("IDENTIFIER", self.source[self.position:temp]))
                self.position = temp
            
            elif char in "+-=!<>":
                if self.position +1 < len(self.source) and self.source[self.position + 1] in OPERATORS: 
                    tokens.append(Token("OPERATOR", self.source[self.position:self.position+2]))
                    self.position +=2
                else :
                    tokens.append(Token("OPERATOR", char))
                    self.position +=1
            else:
                # Skip whitespace or unknown characters
                self.position += 1
                
        return tokens
    

# token1 = Token("NUMBER", "32")
lexer = Lexer("x == y != z <= w")
tokens = lexer.tokenize_II()
for token in tokens:
    print(token)