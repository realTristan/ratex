
from .list import List

class LineList(object):
    def __init__(self, type: str = "itemize", content: str = ""):
        self.type = type
        self.content = content

    def __str__(self) -> str:
        self.content = self.content.strip().split("\n")
        return str(List(
            type=self.type, items=[i for i in self.content if len(i) > 0]
        ))
