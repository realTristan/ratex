import re

# // Equation class
class Equation(object):
    def __init__(self, content: str, enumerate: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.enumerate = enumerate

    def __str__(self) -> str:
        self.content = self.content.replace(" ", "\\;")
        type: str = '*'  if not self.enumerate else ''
        return f"\\begin{{equation{type}}}{self.content}\\end{{equation{type}}}\leavevmode"

# // Text class
class Text(object):
    def __init__(self, content: str, b: bool = False, it: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.bold = b
        self.italic = it
    
    def __str__(self) -> str:
        if self.italic and self.bold:
            return f"\\textbf{{\\textit{{{self.content}}}}}"
        elif self.bold:
            return f"\\textbf{{{self.content}}}"
        elif self.italic:
            return f"\\textit{{{self.content}}}"
        return f"{{{self.content}}}"
    
