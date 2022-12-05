
# // Image class
class Image:
    def __init__(self, path: str, scale: int = 1) -> None:
        self.path = path
        self.scale = scale
    
    def _init(self) -> str:
        return f"\includegraphics[scale={self.scale}]{{{self.path}}}"
    