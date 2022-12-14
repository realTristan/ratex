
# // Header class
class Header(object):
    def __init__(self, content: str, enumerate: bool = False) -> None:
        self.content = content
        self.enumerate = enumerate
        
    def __str__(self) -> str:
        return f"\\section{'' if self.enumerate else '*'}{{{self.content}}}"

class Subheader(object):
    def __init__(self, content: str, enumerate: bool = False) -> None:
        self.content = content
        self.enumerate = enumerate
    
    def __str__(self) -> str:
        return f"\\subsection{'' if self.enumerate else '*'}{{{self.content}}}"
