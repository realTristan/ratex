import re

# // Equation class
class Equation(object):
    def __init__(self, content: str) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()

    def __str__(self) -> str:
        self.content = self.content.replace(" ", "\\;")
        return f"\\begin{{equation}}{self.content}\\end{{equation}}"

# // Eq class
class Eq(object):
    def __init__(self, content: str) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()

    def __str__(self) -> str:
        self.content = self.content.replace(" ", "\;")
        return f"\\[{self.content}\\]"


# // Text class
class Text(object):
    def __init__(self, content: str, b: bool = False, it: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.bold = b
        self.italic = it
    
    def __str__(self) -> str:
        if self.bold:
            return f"\\textbf{{{self.content}}}"
        elif self.italic:
            return f"\\textit{{{self.content}}}"
        elif self.italic and self.bold:
            return f"\\textbf{{\\textit{{{self.content}}}}}"
        return f"{{{self.content}}}"
    
