
# // Space class
class Space:
    def __init__(self, type: str = "v", size: int = 1) -> None:
        self.type = type
        self.size = size
        
    def _init(self) -> str:
        return f"\\{self.type}space{{{self.size}cm}}"
        
    