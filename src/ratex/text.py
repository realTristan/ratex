import re

# // Equation class
class Equation(object):
    def __init__(self, content: str, enumerate: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.enumerate = enumerate

    def __str__(self) -> str:
        self.content = self.content.replace(" ", "\\;")
        type: str = '*' if self.enumerate else ''
        return f"\\begin{{equation{type}}}{self.content}\\end{{equation{type}}}"

# // Text class
class Text(object):
    def __init__(self, content: str, b: bool = False, it: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.b = b
        self.it = it
    
    def __str__(self) -> str:
        return f"\\text{'bf' if self.b else 'it' if self.it else ''}{{{self.content}}}"
    
