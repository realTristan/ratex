
# // Align class
class Align:
    # // flalign, fralign, align
    def __init__(self):
        pass


# // Adjust class
class Adjust:
    def __init__(self, size: int = 0, margin: int = 0, items: list[any] = []) -> None:
        self.size = size
        self.margin = margin
        self.items = items
    
    def _init(self) -> str:
        if len(self.items) > 0:
            return (
                f"\\begin{{adjustwidth}}{{{self.size}cm}}{{{self.margin}pt}}" +
                "".join(i._init() for i in self.items) +
                f"\\end{{adjustwidth}}\\leavevmode\\\\"
            )
        return ""
