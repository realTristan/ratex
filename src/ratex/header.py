
# // Header class
class Header:
    def __init__(self, content: str = "", enumerate: bool = False) -> None:
        self.content = content
        self.enumerate = enumerate
        
    def _init(self) -> str:
        return f"\section{self.enumerate}{{{self.content}}}"
