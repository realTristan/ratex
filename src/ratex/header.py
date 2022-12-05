
# // Header class
class Header(object):
    def __init__(self, content: str = "", enumerate: bool = False) -> None:
        self.content = content
        self.enumerate = enumerate
        
    def __str__(self) -> str:
        return f"\section{self.enumerate}{{{self.content}}}"
