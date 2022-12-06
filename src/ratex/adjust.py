
# // Align class
class Align(object):
    # // flalign, fralign, align
    def __init__(self, type: str = "align", items: list[any] = []):
        self.type = type
        self.items = items

    def __str__(self):
        # \begin{flalign*}
        pass

# // Adjust class
class Adjust(object):
    def __init__(self, width: int, items: list[any]) -> None:
        self.width = width
        self.items = items
    
    def __str__(self) -> str:
        if len(self.items) > 0:
            return (
                f"\\begin{{adjustwidth}}{{{self.width}cm}}{{0pt}}" +
                "".join(str(i) for i in self.items) +
                f"\\end{{adjustwidth}}\\leavevmode\\\\"
            )
        return ""
