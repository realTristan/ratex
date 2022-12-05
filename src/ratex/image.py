
# // Image class
class Image(object):
    def __init__(self, path: str, scale: int = 1) -> None:
        self.path = path
        self.scale = scale
    
    def __str__(self) -> str:
        return f"\includegraphics[scale={self.scale}]{{{self.path}}}"
    