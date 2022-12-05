
# // Flex class
class Flex(object):
    def __init__(self, width: int = 0.33, items: list[any] = []) -> None:
        self.width = width
        self.items = items
        
    def __str__(self) -> str:
        return "".join((
            f"\\begin{{minipage}}{{{self.width}\\textwidth}}" + str(i) +
            f"\\end{{minipage}}\\leavevmode"
        ) for i in self.items)
