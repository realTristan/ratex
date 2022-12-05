
# // List class
class List(object):
    def __init__(self, type: str = "itemize", items: list[any] = []) -> None:
        self.type = type
        self.items = items
        
    def __str__(self) -> str:
        return (
            f"\\begin{{{self.type}}}" +
            "".join(f"\\item {{{i}}}" for i in self.items) +
            f"\\end{{{self.type}}}\\leavevmode"
        )
