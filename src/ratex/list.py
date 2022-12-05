
# // List class
class List:
    def __init__(self, type: str = "itemize", items: list[any] = []) -> None:
        self.type = type
        self.items = items
        
    def _init(self) -> str:
        return (
            f"\\begin{{{self.type}}}" +
            "".join(f"\\item {{{i._init()}}}" for i in self.items) +
            f"\\end{{{self.type}}}\\leavevmode"
        )
        