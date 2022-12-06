
# // Align class
class Align(object):
    # // flalign, fralign, align
    def __init__(self, type: str = "align", items: list[any] = []) -> None:
        self.type = type
        self.items = items

    def __str__(self) -> str:
        # \begin{flalign*}
        pass

# // Adjust class
class Adjust(object):
    def __init__(self, width: int = 0, margin: int = 0, items: list[any] = []) -> None:
        self.width = width
        self.margin = margin
        self.items = items
    
    def __str__(self) -> str:
        if len(self.items) > 0:
            return (
                f"\\begin{{adjustwidth}}{{{self.width}cm}}{{{self.margin}pt}}" +
                "".join(str(i) for i in self.items) +
                f"\\end{{adjustwidth}}\\leavevmode\\\\"
            )
        return ""
