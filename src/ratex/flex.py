
# // Flex class
class Flex:
    def __init__(self, width: int = 0.33, items: list[any] = []) -> None:
        self.width = width
        self.items = items
        
    def _init(self) -> str:
        return "".join((
            f"\\begin{{minipage}}{{{self.width}\\textwidth}}" +
            i._init() +
            f"\\end{{minipage}}\\leavevmode"
        ) for i in self.items)
