import re

# // Equations class
class Eq(object):
    def __init__(self):
        pass

    def __str__(self) -> str:
        pass


# // Text class
class Text(object):
    def __init__(self, content: str = "", bold: bool = False, italic: bool = False) -> None:
        self.content = re.sub("\s\s+", " ", content).strip()
        self.bold = bold
        self.italic = italic
    
    def clean_content(self, content: str) -> str:
        active = False
        content = list(content)
        for i in range(len(content)):
            if content[i] == "$":
                active = not active

            if active:
                if content[i] == " ":
                    content[i] = "$ $"
        return r"".join(c for c in content) + " "
        
    def __str__(self) -> str:
        self.content = self.clean_content(self.content)
        if self.bold:
            return f"\\textbf{{{self.content}}}"
        elif self.italic:
            return f"\\textit{{{self.content}}}"
        elif self.italic and self.bold:
            return f"\\textbf{{\\textit{{{self.content}}}}}"
        return f"{{{self.content}}}"
    
