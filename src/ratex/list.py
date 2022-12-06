
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


# // Line List class
class LineList(object):
    def __init__(self, type: str = "itemize", content: str = ""):
        self.type = type
        self.content = content

    def __str__(self) -> str:
        self.content = self.content.strip().split("\n")
        return str(List(
            type=self.type, items=[i for i in self.content if len(i) > 0]
        ))